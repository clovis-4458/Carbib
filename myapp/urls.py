from django.urls import path
from . import views

urlpatterns = [

    # ------------------- AUTH -------------------
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.home, name='register'),  # can create a dedicated registration view later
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    # ------------------- DASHBOARD -------------------
    path('dashboard/', views.dashboard_view, name='dashboard_view'),

    # ------------------- CLIENTS -------------------
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/view/', views.view_clients, name='view_clients'),
    path('clients/update/', views.update_candidates, name='update_candidates'),
    path('clients/<int:candidate_id>/', views.view_candidate, name='view_candidate'),

    # ------------------- EXCEL -------------------
    path('export-excel/', views.export_excel, name='export_excel'),
    path('import-excel/', views.import_excel, name='import_excel'),

    # ------------------- CV DOWNLOAD -------------------
    path('clients/<int:candidate_id>/download/pdf/', views.download_cv_pdf, name='download_cv_pdf'),
    path('clients/<int:candidate_id>/download/word/', views.download_cv_word, name='download_cv_word'),
]
