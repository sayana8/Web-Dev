from django.http import HttpResponse, JsonResponse
from api.models import Company, Vacancy

def get_companies(request):
    try:
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_company(request, id):
    try:
        company = Company.objects.get(pk=id)
        company_json = company.to_json()
        return JsonResponse(company_json)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_company_vacancies(request, id):
    try:
        company = Company.objects.get(pk=id)
        vacancies = Vacancy.objects.filter(company=company)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(pk=id)
        vacancy_json = vacancy.to_json()
        return JsonResponse(vacancy_json)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_top_ten_vacancies(request):
    try:
        top_ten_vacancies = Vacancy.objects.order_by('-salary')[:10]
        top_ten_vacancies_json = [vacancy.to_json() for vacancy in top_ten_vacancies]
        return JsonResponse(top_ten_vacancies_json, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
