from django.core.management import call_command
from django.core.management.base import BaseCommand

from modules.about.models import AboutSection
from modules.board.models import BoardMember
from modules.core.models import FinancialReport


class Command(BaseCommand):
    help = "Load initial fixture data once (idempotent — skips if data already present)."

    FIXTURE = "initial_data.json"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Load even if data already exists (may create duplicates).",
        )

    def handle(self, *args, **options):
        already = (
            AboutSection.objects.exists()
            or BoardMember.objects.exists()
            or FinancialReport.objects.exists()
        )
        if already and not options["force"]:
            self.stdout.write(self.style.WARNING("Data already present — skipping seed."))
            return

        call_command("loaddata", self.FIXTURE)
        self.stdout.write(self.style.SUCCESS("Initial data loaded."))
