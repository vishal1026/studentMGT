# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.http import HttpResponse
from decorators import *

@api_view(['GET'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def renderlogin(request):
    return Response(template_name='login.html')


@csrf_exempt
def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = School_user.objects.get(user_name=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['user_id'] = m.user_id
            request.session['user_name'] = m.user_name
            request.session['user_type'] = m.user_type
            # return HttpResponseRedirect('/you-are-logged-in/')
            if m.user_type==1:
                details = Student.objects.get(user_id=m.user_id)
                request.session['stud_fname'] = details.fname
                request.session['stud_lname'] = details.lname
                request.session['stud_contact'] = str(details.contact)
                request.session['stud_id'] = details.student_id
                request.session['parent_id'] = None
                request.session['parent_fname'] = None
                request.session['parent_lname'] = None
                request.session['parent_contact'] = None
                request.session['teacher_id'] = None
                request.session['teacher_fname'] = None
                request.session['teacher_lname'] = None
                request.session['teacher_contact'] = None
            
            elif m.user_type==2:
                details = Parent.objects.get(user_id=m.user_id)
                request.session['stud_fname'] = None
                request.session['stud_lname'] = None
                request.session['stud_contact'] = None
                request.session['stud_id'] = None
                request.session['parent_id'] = details.parent_id
                request.session['parent_fname'] = details.fname
                request.session['parent_lname'] = details.lname
                request.session['parent_contact'] = details.contact
                request.session['teacher_id'] = None
                request.session['teacher_fname'] = None
                request.session['teacher_lname'] = None
                request.session['teacher_contact'] = None
            
            elif m.user_type==2:
                details = Parent.objects.get(user_id=m.user_id)
                request.session['stud_fname'] = None
                request.session['stud_lname'] = None
                request.session['stud_contact'] = None
                request.session['stud_id'] = None
                request.session['parent_id'] = details.parent_id
                request.session['parent_fname'] = details.fname
                request.session['parent_lname'] = details.lname
                request.session['parent_contact'] = details.contact
                request.session['teacher_id'] = None
                request.session['teacher_fname'] = None
                request.session['teacher_lname'] = None
                request.session['teacher_contact'] = None
            
            elif m.user_type==3:
                details = Teacher.objects.get(user_id=m.user_id)
                request.session['stud_fname'] = None
                request.session['stud_lname'] = None
                request.session['stud_contact'] = None
                request.session['stud_id'] = None
                request.session['parent_id'] = None
                request.session['parent_fname'] = None
                request.session['parent_lname'] = None
                request.session['parent_contact'] = None
                request.session['teacher_id'] = details.teacher_id
                request.session['teacher_fname'] = details.fname
                request.session['teacher_lname'] = details.lname
                request.session['teacher_contact'] = details.contact
            
            elif m.user_type==4:
                details = Teacher.objects.get(user_id=m.user_id)
                request.session['stud_fname'] = None
                request.session['stud_lname'] = None
                request.session['stud_contact'] = None
                request.session['stud_id'] = None
                request.session['parent_id'] = None
                request.session['parent_fname'] = None
                request.session['parent_lname'] = None
                request.session['parent_contact'] = None
                request.session['teacher_id'] = details.teacher_id
                request.session['teacher_fname'] = details.fname
                request.session['teacher_lname'] = details.lname
                request.session['teacher_contact'] = details.contact
           
            return HttpResponse("Success")
    except School_user.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")

@checkParent
def sessionValues(request):
    print (1+1)
    return HttpResponse("Success in session values")
def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

@csrf_exempt

def createStudent(request):
    try:
        studentId = request.POST["studentId"]
        fname = request.POST["fname"] 
        lname = request.POST["lname"]
        contact = request.POST["contact"]

        studInstance = School_user.objects.get(user_id=int(studentId))
        stud = Student()
        stud.student_id = 1
        stud.user_id = studInstance
        stud.fname = fname
        stud.lname = lname
        stud.contact = contact
        stud.save()
        return HttpResponse("Pass")

    except:
        return HttpResponse("Failed")   