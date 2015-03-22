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
from places.models import Division, Location, SubLocation, SchoolZone

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
    else:
        return School.NOT_KNOWN

def get_school_type(data):
    if data== "DAY ONLY":
        return School.DAY
    elif data== "BOARDING ONLY":
        return School.BOARDING
    elif data== "DAY & BOARDING":
        return School.DAY_AND_BOARDING
    return School.NOT_KNOWN

def get_student_needs(data):
    if data == "ORDINARY":
        return School.ORDINARY
    elif data == "INTEGRATED":
        return School.SPECIAL
    elif data == "SPECIAL SCHOOL":
        return School.INTEGRATED
    return School.ORDINARY

def import_secondary_schools():
    period = datetime.datetime(day=31,month=12,year=2007)
    filename = "%s/documentation/data/2007/secondary.csv" % settings.BASE_DIR
    n = 1
    with open(filename, "rb") as ifile:
        reader = csv.reader(ifile)
        for row in reader:
            if n > 1:
                school = School()
                school.code = row[0].strip()
                school.name = row[1].strip()
                school.address = row[2].strip()
                school.level = School.SECONDARY
                school.ownership = get_ownership(row[3].strip())
                school.sponsor = get_sponsor(row[4].strip())
                school.student_gender = get_student_gender(row[5].strip())
                school.school_type = get_school_type(row[6].strip())
                school.student_needs = get_student_needs(row[6].strip())

                #location
                province,created = Province.objects.get_or_create(name=row[23].strip())
                school.province = province
                county,created = County.objects.get_or_create(name=row[24].strip())
                school.county = county
                if row[30]:
                    constituency, created = Constituency.objects.get_or_create(name=row[30].strip(), county=county)
                    school.constituency =  constituency
                if row[25]:
                    district, created = District.objects.get_or_create(name=row[25].strip(), province=province)
                    school.district = district
                if row[26]:
                    division, created = Division.objects.get_or_create(name=row[26].strip(), district=district)
                    school.division = division
                if row[27]:
                    location, created = Location.objects.get_or_create(name=row[27].strip(), division=division)
                    school.location = location
                if row[28]:
                    sub_location, created = SubLocation.objects.get_or_create(name=row[28].strip(), location=location)
                    school.sub_location = sub_location
                if row[29]:
                    school_zone, created = SchoolZone.objects.get_or_create(name=row[29].strip(), county=county)
                    school.school_zone = school_zone

                if row[31]:
                    coord = row[31].split(",")
                    x = float(coord[0][1:])
                    y = float(coord[1][1:-2])
                    school.coordinates = Point(y,x)

                school.save()

                #staff
                if row[12]:
                    staff1, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.TSC_MALE,
                        number=row[12].strip(), is_teacher=True)
                if row[13]:
                    staff2, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.TSC_FEMALE,
                        number=row[13].strip(), is_teacher=True)
                if row[14]:
                    staff3, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.LOCAL_MALE,
                        number=row[14].strip(), is_teacher=True)
                if row[15]:
                    staff4, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.LOCAL_FEMALE,
                        number=row[15].strip(), is_teacher=True)
                if row[16]:
                    staff5, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.PTA_MALE,
                        number=row[16].strip(), is_teacher=True)
                if row[17]:
                    staff6, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.PTA_FEMALE,
                        number=row[17].strip(), is_teacher=True)
                if row[18]:
                    staff7, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.OTHER_MALE,
                        number=row[18].strip(), is_teacher=True)
                if row[19]:
                    staff8, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.OTHER_FEMALE,
                        number=row[19].strip(), is_teacher=True)
                if row[20]:
                    staff9, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.NON_TEACHING_MALE,
                        number=row[20].strip(), is_teacher=False)
                if row[21]:
                    staff10, created = Staff.objects.get_or_create(period=period, school=school, staff_type=Staff.NON_TEACHING_MALE,
                        number=row[21].strip(), is_teacher=False)

                #facts
                if row[8]:
                    fact1, created = Fact.objects.get_or_create(name="Total Enrolment", period=period, school=school,
                        value=row[8].strip())
                if row[9]:
                    fact2, created = Fact.objects.get_or_create(name="Pupil Teacher Ratio", period=period, school=school,
                        value=row[9].strip())
                if row[10]:
                    fact3, created = Fact.objects.get_or_create(name="Total Teaching staff", period=period, school=school,
                        value=row[10].strip())
                if row[11]:
                    fact4, created = Fact.objects.get_or_create(name="Acreage per enrolment", period=period, school=school,
                        value=row[11].strip())
                if row[22]:
                    fact5, created = Fact.objects.get_or_create(name="Acreage", period=period, school=school,
                        value=row[22].strip())



            n += 1
