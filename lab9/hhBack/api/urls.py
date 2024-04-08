from django.urls import path
from api.views import (
    get_companies, get_company, get_company_vacancies, get_vacancies, get_vacancy, get_top_ten_vacancies
)

urlpatterns = [
    path('companies/', get_companies), 
    path('companies/<int:id>/', get_company),  
    path('companies/<int:id>/vacancies/', get_company_vacancies),  
    path('vacancies/', get_vacancies), 
    path('vacancies/<int:id>/', get_vacancy),  
    path('vacancies/top_ten/', get_top_ten_vacancies), 

]
