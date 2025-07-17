# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from related_objects.models import *
from datetime import date


# Your code starts from here:
# Course has instructors reference field so can be used directly via forward access
courses = Course.objects.filter(instructors__first_name='Yan')
print("1. Get courses taught by Instructor `Yan`, forward")
print(courses)

print("\n")
# For each instructor, Django creates a implicit course_set. This is caleld backward access
instructor_yan = Instructor.objects.get(first_name='Yan')
print("1. Get courses taught by Instructor `Yan`, backward")
print(instructor_yan.course_set.all())

print("\n")
instructors = Instructor.objects.filter(course__name__contains='Cloud')
print("2. Get the instructors of Cloud app dev course")
print(instructors)

print("\n")
courses = Course.objects.filter(instructors__first_name='Yan')
occupation_list = set()
for course in courses:
    for learner in course.learners.all():
        occupation_list.add(learner.occupation)
print("3. Check the occupations of the courses taught by instructor Yan'")
print(occupation_list)