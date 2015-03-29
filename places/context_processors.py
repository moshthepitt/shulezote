from places.models import County, Constituency


def county_processor(request):
    return {'all_counties': County.objects.all()}


def constituency_processor(request):
    return {'all_constituencies': Constituency.objects.all()}
