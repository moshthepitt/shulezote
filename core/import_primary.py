#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import datetime

from django.conf import settings
from django.contrib.gis.geos import Point

from schools.models import School
from facts.models import Fact
from staff.models import Staff
from facilities.models import Facility, FacilityRecord
from places.models import County, Constituency, Province, District
from places.models import Division, Location


def get_ownership(data):
    if data == "PRIVATE":
        return School.PRIVATE
    return School.PUBLIC


def get_sponsor(data):
    if data == "CENTRAL GOVERNMENT/DEB":
        return School.GOVERNMENT
    elif data == "RELIGIOUS ORGANIZATION":
        return School.RELIGIOUS
    elif data == "COMMUNITY":
        return School.COMMUNITY
    elif data == "NGO/CBO":
        return School.NGO
    elif data == "PRIVATE INDIVIDUAL":
        return School.PRIVATE_INDIVIDUAL
    return School.NOT_KNOWN


def get_student_gender(data):
    if data == "BOYS ONLY":
        return School.BOYS
    elif data == "GIRLS ONLY":
        return School.GIRLS
    elif data == "MIXED":
        return School.MIXED
    else:
        return School.NOT_KNOWN


def get_school_type(data):
    if data == "DAY ONLY":
        return School.DAY
    elif data == "BOARDING ONLY":
        return School.BOARDING
    elif data == "DAY & BOARDING":
        return School.DAY_AND_BOARDING
    return School.NOT_KNOWN


def get_student_needs(data):
    if data == "ORDINARY":
        return School.ORDINARY
    elif data == "INTEGRATED":
        return School.INTEGRATED
    elif data == "SPECIAL SCHOOL":
        return School.SPECIAL
    return School.ORDINARY


def import_primary_schools():
    period = datetime.datetime(day=31, month=12, year=2007)
    filename = "%s/documentation/data/2007/primary.csv" % settings.BASE_DIR
    n = 1
    with open(filename, "rb") as ifile:
        reader = csv.reader(ifile)
        for row in reader:
            if n > 1:
                school = School()
                school.name = row[0].strip()
                school.level = School.PRIMARY
                school.ownership = get_ownership(row[2].strip())
                school.sponsor = get_sponsor(row[3].strip())
                school.student_gender = get_student_gender(row[4].strip())
                school.school_type = get_school_type(row[5].strip())
                school.student_needs = get_student_needs(row[6].strip())

                # location
                if row[29]:
                    county, created = County.objects.get_or_create(name=row[29].strip().upper())
                    school.county = county
                    province, created = Province.objects.get_or_create(name=row[28].strip().upper())
                    school.province = province

                    if row[33]:
                        constituency = Constituency.objects.filter(name=row[33].strip().upper()).first()
                        if not constituency:
                            constituency, created = Constituency.objects.get_or_create(
                                name=row[33].strip().upper(), county=county)
                        school.constituency = constituency
                    if row[30]:
                        district = District.objects.filter(name=row[30].strip().upper()).first()
                        if not district:
                            district, created = District.objects.get_or_create(
                                name=row[30].strip().upper(), province=province)
                        school.district = district
                    if row[31]:
                        division, created = Division.objects.get_or_create(
                            name=row[31].strip().upper(), district=district)
                        school.division = division
                    if row[32]:
                        location, created = Location.objects.get_or_create(
                            name=row[32].strip().upper(), division=division)
                        school.location = location

                    if row[34]:
                        coord = row[34].split(",")
                        x = float(coord[0][1:])
                        y = float(coord[1][1:-2])
                        school.coordinates = Point(y, x)

                    school.save()

                    # facilities
                    facility1, created = Facility.objects.get_or_create(name="Toilets")
                    facility2, created = Facility.objects.get_or_create(name="Classrooms")
                    facility3, created = Facility.objects.get_or_create(name="Enrollment")

                    facility_record1, created = FacilityRecord.objects.get_or_create(facility=facility1, school=school, period=period, boys=row[11].strip(),
                                                                                     girls=row[12].strip(), total=row[13].strip())
                    facility_record3, created = FacilityRecord.objects.get_or_create(facility=facility3, school=school, period=period, boys=row[15].strip(),
                                                                                     girls=row[16].strip(), total=row[17].strip())

                    # staff
                    if row[18]:
                        staff1, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.TSC_MALE,
                                                                      number=row[18].strip(), is_teacher=True)
                    if row[19]:
                        staff2, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.TSC_FEMALE,
                                                                      number=row[19].strip(), is_teacher=True)
                    if row[20]:
                        staff3, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.LOCAL_MALE,
                                                                      number=row[20].strip(), is_teacher=True)
                    if row[21]:
                        staff4, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.LOCAL_FEMALE,
                                                                      number=row[21].strip(), is_teacher=True)
                    if row[22]:
                        staff5, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.PTA_MALE,
                                                                      number=row[22].strip(), is_teacher=True)
                    if row[23]:
                        staff6, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.PTA_FEMALE,
                                                                      number=row[23].strip(), is_teacher=True)
                    if row[24]:
                        staff7, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.OTHER_MALE,
                                                                      number=row[24].strip(), is_teacher=True)
                    if row[25]:
                        staff8, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.OTHER_FEMALE,
                                                                      number=row[25].strip(), is_teacher=True)
                    if row[26]:
                        staff9, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.NON_TEACHING_MALE,
                                                                      number=row[26].strip(), is_teacher=False)
                    if row[27]:
                        staff10, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.NON_TEACHING_FEMALE,
                                                                       number=row[27].strip(), is_teacher=False)

                    # facts
                    if row[7]:
                        fact2, created = Fact.objects.get_or_create(name="Pupil Teacher Ratio", period=period, school=school,
                                                                    value=row[7].strip())
                    if row[8]:
                        fact1, created = Fact.objects.get_or_create(name="Pupil Classroom Ratio", period=period, school=school,
                                                                    facility=facility2, value=row[8].strip())
                    if row[9]:
                        fact4, created = Fact.objects.get_or_create(name="Pupil Toilet Ratio", period=period, school=school,
                                                                    facility=facility1, value=row[9].strip())
                    if row[10]:
                        fact5, created = Fact.objects.get_or_create(name="Total Number of Classrooms", period=period, school=school,
                                                                    facility=facility2, value=row[10].strip())
                    if row[14]:
                        fact5, created = Fact.objects.get_or_create(name="Teachers Toilets", period=period, school=school,
                                                                    facility=facility1, value=row[14].strip())

            n += 1
