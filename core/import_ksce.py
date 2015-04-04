import csv
from decimal import Decimal

from django.conf import settings

from schools.models import School
from kcse.models import Result


def get_gender(data):
    if data == "M":
        return Result.MALE
    return Result.FEMALE


def import_kcse_results(csvname="kcse"):
    filename = "%s/documentation/data/exams/%s.csv" % (settings.BASE_DIR, csvname)
    n = 1
    failed = []
    with open(filename, "rb") as ifile:
        reader = csv.reader(ifile)
        for row in reader:
            if n > 1:
                if row[6]:
                    data = dict(year=int(row[0].strip()),
                                district_code=row[1].strip(),
                                school_code=row[4].strip(),
                                knec_code=row[5].strip(),
                                gender=get_gender(row[7].strip().upper()),
                                grade=row[8].strip(),
                                mean_grade=Decimal(row[9].strip()),
                                frequency=int(row[10].strip())
                                )

                    name = row[6].strip().upper()
                    try:
                        school = School.objects.get(name=name)
                        data['school'] = school
                        result = Result(**data)
                        result.save()
                    except:
                        failed.append(row)

            n += 1
    # write failed to file
    if failed:
        with open("%s/documentation/data/exams/failed.csv" % (settings.BASE_DIR), 'wb') as new_file:
            writer = csv.writer(new_file, delimiter=',')
            for item in failed:
                writer.writerow(item)
