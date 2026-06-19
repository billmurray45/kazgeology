from whitenoise.storage import CompressedManifestStaticFilesStorage


class ForgivingManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """Manifest static storage that does not crash on missing referenced files.

    Third-party packages (e.g. django-jazzmin) ship minified JS/CSS whose
    ``sourceMappingURL`` points at ``.map`` files that are not bundled. The
    default WhiteNoise manifest storage raises ``MissingFileError`` for those
    during ``collectstatic``. We downgrade missing references to non-fatal so
    deploys are not blocked by absent source maps.
    """

    manifest_strict = False

    def url_converter(self, name, hashed_files, template=None):
        converter = super().url_converter(name, hashed_files, template)

        def forgiving_converter(matchobj):
            try:
                return converter(matchobj)
            except ValueError:
                # Referenced file (e.g. a missing .map) does not exist —
                # leave the original reference untouched instead of failing.
                return matchobj.group(0)

        return forgiving_converter
