from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404

# Create your class based views here.

# Note that CourseListView is subclassing from generic.ListView instead of View
# so that it can use attributes and override methods from ListView such as get_queryset()
class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list.html'
    context_object_name = 'course_list'

    # Override get_queryset() to provide list of objects
    def get_queryset(self):
       courses = Course.objects.order_by('-total_enrollment')[:10]
       return courses

# Note that CourseDetailsView is now subclassing DetailView 
class CourseDetailsView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_detail.html'

class EnrollView(View):

    # Handles post request
    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('pk')
        course = get_object_or_404(Course, pk=course_id)
        # Increase total enrollment by 1
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

#class CourseListView(View):

#     # Handles get request
#     def get(self, request):
#         context = {}
#         course_list = Course.objects.order_by('-total_enrollment')[:10]
#         context['course_list'] = course_list
#         return render(request, 'onlinecourse/course_list.html', context)

# class CourseDetailsView(View):

#     # Handles get request
#     def get(self, request, *args, **kwargs):
#         context = {}
#         # We get URL parameter pk from keyword argument list as course_id
#         course_id = kwargs.get('pk')
#         try:
#             course = Course.objects.get(pk=course_id)
#             context['course'] = course
#             return render(request, 'onlinecourse/course_detail.html', context)
#         except Course.DoesNotExist:
#             raise Http404("No course matches the given id.")
            
# Function based views

# Function-based course list view
# def popular_course_list(request):
#    context = {}
#    if request.method == 'GET':
#        course_list = Course.objects.order_by('-total_enrollment')[:10]
#        context['course_list'] = course_list
#        return render(request, 'onlinecourse/course_list_no_css.html', context)

# Function-based course_details view
# def course_details(request, course_id):
#    context = {}
#    if request.method == 'GET':
#        try:
#            course = Course.objects.get(pk=course_id)
#            context['course'] = course
#            return render(request, 'onlinecourse/course_detail.html', context)
#        except Course.DoesNotExist:
#            raise Http404("No course matches the given id.")

# Function-based enroll view
# def enroll(request, course_id):
#    if request.method == 'POST':
#       course = get_object_or_404(Course, pk=course_id)
#       # Create an enrollment
#       course.total_enrollment += 1
#       course.save()
#       return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))
