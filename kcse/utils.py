from kcse.models import Result


def get_last_year():
    """
    Returns the last year for which we have KCSE results
    """
    last_year = Result.objects.values('year').distinct().order_by('-year').first()
    return last_year['year']
