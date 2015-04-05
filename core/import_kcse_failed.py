import csv
import itertools
from decimal import Decimal

from django.conf import settings

from schools.models import School
from places.models import County
from kcse.models import Result

from import_kcse import get_gender


def format_name(name):
    remove_list = ['SECONDARY', 'SCHOOL', 'SCH', 'SEC', 'SCH.', 'SEC.', 'ST', 'ST.', 'DR', 'DR.', 'FR.']
    words = [i for i in name.split() if i not in remove_list]
    # replace every word that ends with ' or 'S
    for c, w in enumerate(words):
        if w[-1] == "'":
            words[c] = w[:-1]
        if w[-2:] == "'S":
            words[c] = w[:-2]
    # remove ST.  or DR. or FR. OR MT. from begining of word
    for c, w in enumerate(words):
        if w[:3] == "ST." or w[:3] == "DR." or w[:3] == "FR." or w[:3] == "MT.":
            words[c] = w[3:]
    new_name = ' '.join(words)
    return new_name.strip()


def get_list_from_csv(csvname="failed"):
    filename = "%s/documentation/data/exams/%s.csv" % (settings.BASE_DIR, csvname)

    with open(filename, "rb") as ifile:
        reader = csv.reader(ifile)
        t = zip(reader)
    return t


def process_passed():
    classified_schools = classify_schools()
    school_match = classified_schools[4]
    t = get_list_from_csv()
    import_list = [x[0] for x in t]
    failed = []
    for row in import_list:
        if row[6].upper().strip() in school_match:
            school = School.objects.get(pk=school_match[row[6]])
            data = dict(year=int(row[0].strip()),
                        district_code=row[1].strip(),
                        school_code=row[4].strip(),
                        knec_code=row[5].strip(),
                        gender=get_gender(row[7].strip().upper()),
                        grade=row[8].strip(),
                        mean_grade=Decimal(row[9].strip()),
                        frequency=int(row[10].strip()),
                        school=school
                        )
            result = Result(**data)
            result.save()
        else:
            failed.append(row)
    # write failed to file
    if failed:
        with open("%s/documentation/data/exams/failed2.csv" % (settings.BASE_DIR), 'wb') as new_file:
            writer = csv.writer(new_file, delimiter=',')
            for item in failed:
                writer.writerow(item)


def classify_schools():
    # private_school_counties = {
    #     'CHANDARIA HALL MOMBASA PRIVATE': 'MOMBASA',
    #     'DIANI SECONDARY (PRIVATE)': 'MSAMBWENI',
    #     'DR. AGGREY HIGH SCHOOL (PRIVATE CENTRE)': 'TAITA TAVETA',
    #     'HOLA PRIVATE': 'TANA RIVER',
    #     'KILIFI PRIVATE': 'KILIFI',
    #     'KINANGO PRIVATE': 'KWALE',
    #     'KWALE PRIVATE': 'KWALE',
    #     'LAMU PRIVATE': 'LAMU',
    #     'MALINDI (PRIVATE)': 'KILIFI',
    #     'MOMBASA POLYTECHNIC PRIVATE': 'MOMBASA',
    #     'MOMBASA PRIVATE TWO (SINOGAL CENTRE)': 'MOMBASA',
    #     'TAITA PRIVATE': 'TAITA TAVETA',
    #     'WAA HIGH PRIVATE': 'KWALE'
    # }

    # southern_sudan = ["ST. JOSEPH'S SEC SCHOOL-GIDEL-SOUTHERN SAUDAN"]

    county_correction = {
        'ELGEYO MARAKWET': 'ELEGEYO-MARAKWET',
        'THARAKA NITHI': 'THARAKA - NITHI',
    }

    school_pk_match = {
        'AIC OL-KALOU SEC SCHOOL': 4083,
        'KALOU SECONDARY SCHOOL': 4087
    }

    t = get_list_from_csv()
    names = [[x[0][3].upper(), x[0][6]] for x in t]
    names.sort()
    names = list(names for names, _ in itertools.groupby(names))

    county = None
    passed, multiple, failed, private = [], [], [], []
    for name in names:
        county_name = name[0].upper().strip()
        origi_school_name = name[1].upper().strip()
        school_name = format_name(origi_school_name)

        if county_name in county_correction:
            county_name = county_correction[county_name]

        if not county or county.name != county_name:
            county = County.objects.filter(name=county_name).first()

        if county:
            schools_in_county = School.objects.filter(county=county).filter(level=School.SECONDARY)
            # try simple match
            possible_schools = schools_in_county.filter(name__icontains=school_name)
            if not possible_schools:
                failed.append(school_name)
            elif possible_schools.count() == 1:
                passed.append(school_name)
                school_pk_match[origi_school_name] = possible_schools.first().pk
            else:
                if school_name in school_pk_match:
                    passed.append(school_name)
                else:
                    multiple.append(school_name)  # MULSIM ACADEMY IS LEFT
            # nothing here
        else:
            private.append(school_name)  # this must be a private test centre

    return [passed, multiple, failed, private, school_pk_match]
