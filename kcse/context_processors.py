from kcse.models import Result


def year_processor(request):
    years = Result.objects.values('year').distinct().order_by('-year')
    return {'kcse_years': [year['year'] for year in years]}
