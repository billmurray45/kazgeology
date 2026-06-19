from django.urls import path
from .views import (
    IndexView,
    BoardView,
    AboutView,
    InvestorsView,
    GovernanceView,
    ProjectsView,
    CareersView,
    ComplianceView,
    PrivacyPolicyView,
    board_doc_download
)

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('board/', BoardView.as_view(), name='board'),
    path('about/', AboutView.as_view(), name='about'),
    path('investors/', InvestorsView.as_view(), name='investors'),
    path('governance/', GovernanceView.as_view(), name='governance'),
    # path('procurement/', ProcurementView.as_view(), name='procurement'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('careers/', CareersView.as_view(), name='careers'),
    path('compliance/', ComplianceView.as_view(), name='compliance'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('board/docs/<str:filename>', board_doc_download, name='board_doc'),
]
