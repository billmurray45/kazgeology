#!/bin/sh
# One-time bootstrap for the initial Let's Encrypt certificate.
# After this succeeds, the certbot service in docker-compose auto-renews.
#
# Usage:
#   DOMAIN=kazgeology.kz EMAIL=admin@kazgeology.kz ./init-letsencrypt.sh
#
# Set STAGING=1 to test against Let's Encrypt staging (avoids rate limits).
set -e

DOMAIN="${DOMAIN:-kazgeology.kz}"
EMAIL="${EMAIL:?Set EMAIL=you@example.com}"
STAGING="${STAGING:-0}"

staging_arg=""
[ "$STAGING" != "0" ] && staging_arg="--staging"

echo "### Creating a temporary self-signed cert so nginx can start..."
docker compose run --rm --entrypoint "\
  sh -c 'mkdir -p /etc/letsencrypt/live/$DOMAIN && \
  openssl req -x509 -nodes -newkey rsa:2048 -days 1 \
    -keyout /etc/letsencrypt/live/$DOMAIN/privkey.pem \
    -out /etc/letsencrypt/live/$DOMAIN/fullchain.pem \
    -subj /CN=localhost'" certbot

echo "### Starting nginx..."
docker compose up -d nginx

echo "### Deleting dummy cert and requesting the real one..."
docker compose run --rm --entrypoint "\
  sh -c 'rm -rf /etc/letsencrypt/live/$DOMAIN /etc/letsencrypt/archive/$DOMAIN /etc/letsencrypt/renewal/$DOMAIN.conf'" certbot

docker compose run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    -d $DOMAIN -d www.$DOMAIN \
    --email $EMAIL --agree-tos --no-eff-email --force-renewal" certbot

echo "### Reloading nginx with the real certificate..."
docker compose exec nginx nginx -s reload

echo "### Done. Bring everything up with: docker compose up -d"
