import os
from django.db.models import Prefetch
from django.views.generic import TemplateView
from django.http import FileResponse, Http404, HttpResponseRedirect
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme
from .models import FinancialReport, AffiliatedPersonsList, CorporateEvent, OrgChart, PrivacyPolicy
from modules.about.models import AboutHistoryEvent, AboutSection, AboutStatistic
from modules.board.models import BoardCommittee, BoardCommitteeMember, BoardMember, BoardSecretary


def _set_lang_prefix(path, lang):
    """Replace the language prefix of ``path`` with ``lang``'s prefix.

    The default language (``LANGUAGE_CODE``) has no prefix because the project
    uses ``i18n_patterns(prefix_default_language=False)``.
    """
    codes = [c for c, _ in settings.LANGUAGES]
    # Strip an existing language prefix, if any.
    parts = path.split('/', 2)  # ['', '<maybe-lang>', 'rest...']
    if len(parts) >= 2 and parts[1] in codes:
        rest = parts[2] if len(parts) > 2 else ''
        path = '/' + rest
    # Add the new prefix unless it is the default (unprefixed) language.
    if lang != settings.LANGUAGE_CODE:
        path = '/' + lang + path
    return path


def set_language(request):
    """Switch active language and redirect to the same page under the new
    language prefix.

    Django's built-in ``set_language`` redirects to ``next`` verbatim, so a
    path that already carries a language prefix (e.g. ``/en/about/``) keeps the
    old prefix and the switch appears to do nothing. We rebuild the target URL
    for the requested language with ``translate_url``.
    """
    lang = request.POST.get('language') or request.GET.get('language')
    next_url = request.POST.get('next') or request.GET.get('next') or '/'

    if not url_has_allowed_host_and_scheme(
        next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        next_url = '/'

    available = {code for code, _ in settings.LANGUAGES}
    if lang in available:
        next_url = _set_lang_prefix(next_url, lang)

    response = HttpResponseRedirect(next_url)
    if lang in available:
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME, lang,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
            secure=settings.LANGUAGE_COOKIE_SECURE,
            httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
            samesite=settings.LANGUAGE_COOKIE_SAMESITE,
        )
    return response


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
