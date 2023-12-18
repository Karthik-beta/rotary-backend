from django.urls import re_path, path
from report import views



urlpatterns = [
    
    re_path(r'^check_database_connection/$', views.check_database_connection),

    re_path(r'^material_transactions/$', views.MaterialTransactionsViewAll.as_view()),

]