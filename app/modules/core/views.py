import os
from django.db.models import Prefetch
from django.views.generic import TemplateView
from django.http import FileResponse, Http404
from django.conf import settings
from .models import FinancialReport, AffiliatedPersonsList, CorporateEvent, OrgChart, PrivacyPolicy
from modules.about.models import AboutHistoryEvent, AboutSection, AboutStatistic
from modules.board.models import BoardCommittee, BoardCommitteeMember, BoardMember, BoardSecretary


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['about_section'] = AboutSection.objects.first()
        ctx['about_stats'] = AboutStatistic.objects.all()
        return ctx


class BoardView(TemplateView):
    template_name = 'board.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['board_members'] = BoardMember.objects.filter(is_active=True)
        ctx['board_secretary'] = BoardSecretary.objects.filter(is_active=True).first()
        ctx['board_committees'] = BoardCommittee.objects.filter(is_active=True).prefetch_related(
            Prefetch('members', queryset=BoardCommitteeMember.objects.filter(is_active=True))
        )
        return ctx


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['org_chart'] = OrgChart.objects.first()
        history_groups = {}
        history_year_order = []

        for event in AboutHistoryEvent.objects.filter(is_active=True):
            if event.year not in history_groups:
                history_groups[event.year] = {'year': event.year, 'events': []}
                history_year_order.append(event.year)
            history_groups[event.year]['events'].append(event)

        ctx['history_groups'] = [history_groups[year] for year in history_year_order]
        return ctx


class InvestorsView(TemplateView):
    template_name = 'investors.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        reports = list(FinancialReport.objects.all())
        years = sorted({r.year for r in reports}, reverse=True)
        ctx['report_years'] = [
            (
                y,
                next((r for r in reports if r.year == y and r.report_type == 'consolidated'), None),
                next((r for r in reports if r.year == y and r.report_type == 'separate'), None),
            )
            for y in years
        ]
        ctx['affiliated'] = AffiliatedPersonsList.objects.all()
        ctx['events'] = CorporateEvent.objects.all()
        return ctx


class GovernanceView(TemplateView):
    template_name = 'governance.html'


class ProcurementView(TemplateView):
    template_name = 'procurement.html'


class ProjectsView(TemplateView):
    template_name = 'projects.html'


class CareersView(TemplateView):
    template_name = 'careers.html'


class ComplianceView(TemplateView):
    template_name = 'compliance.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['privacy_policy'] = PrivacyPolicy.objects.prefetch_related('sections').first()
        return ctx


def board_doc_download(request, filename):
    doc_dir = os.path.join(settings.BASE_PROJECT_DIR, 'reference', 'СД')
    file_path = os.path.join(doc_dir, filename)

    # Ensure the resolved path stays within doc_dir (prevent path traversal)
    if not os.path.abspath(file_path).startswith(os.path.abspath(doc_dir)):
        raise Http404

    if not os.path.exists(file_path):
        raise Http404

    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
