# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from django.shortcuts import render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.crypto import get_random_string
from models import *
from django.http import HttpResponse
from decorators import *
from django.contrib.auth import logout
from serializers import *

@checkAdmin
@csrf_exempt
@api_view(['GET'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def student_registration(request):
    return Response(template_name='admin_register_student.html')



@checkAdmin
@csrf_exempt
@api_view(['GET'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def add_course(request):
    return Response(template_name='admin_add_course.html')


@checkAdmin
@csrf_exempt
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def add_entry_in_course(request):
    courseObj = Course()
    deptId = Department.objects.get(department_id = request.data['deptID'])
    courseObj.course_name = request.data['courseName']
    courseObj.department_id = deptId 
    courseObj.save()
    courseSer = courseSerializer(courseObj, many=False)
    return Response(courseSer.data)


@checkAdmin
@csrf_exempt
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def course_list(request):
    courseObj = Course.objects.all()
    courseList = courseSerializer(courseObj, many=True)
    print courseList.data
    
    return Response(courseList.data)    



@api_view(['GET'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def renderlogin(request):
    return Response(template_name='login.html')


@checkAdmin
@api_view(['GET'])
@authentication_classes(())
@renderer_classes((JSONRenderer,))
@permission_classes(())
def foo(request):
    data= {'rfg':'acs'}
    return Response(data)

@checkAdmin
@api_view(['GET','POST'])
@renderer_classes((TemplateHTMLRenderer,))
def render_add_department(request):
    return Response(template_name='admin_add_department.html')



@checkAdmin
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def department_list_table(request):
    department_obj = Department.objects.all()
    department_list = departmentSerializer(department_obj, many=True)
    print department_list.data
    return Response(department_list.data)



@checkAdmin
@csrf_exempt
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def add_entry_in_department(request):
    department_obj = Department()
    department_obj.name = request.data['deptName']
    department_obj.save()
    dept = departmentSerializer(department_obj, many=False)
    return Response(dept.data)



@api_view(['POST'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = School_user.objects.get(user_name=request.POST['username'])
        if m.password == request.POST['password']:
            #request.session.set_expiry(300) 
            request.session['user_id'] = m.user_id
            request.session['user_name'] = m.user_name
            request.session['user_type'] = m.user_type
            # return HttpResponseRedirect('/you-are-logged-in/')
            if m.user_type==1: #Student Type
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
                return Response(template_name='student_index.html')
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
                return Response(template_name='parent_index.html')
                     
            elif m.user_type==3: #teacher type
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
                return Response(template_name='teacher_index.html')
            elif m.user_type==4: #class teacher type
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
                return Response(template_name='class_teacher_index.html')

            elif m.user_type==5: #admin type
                
                request.session['stud_fname'] = None
                request.session['stud_lname'] = None
                request.session['stud_contact'] = None
                request.session['stud_id'] = None
                request.session['parent_id'] = None
                request.session['parent_fname'] = None
                request.session['parent_lname'] = None
                request.session['parent_contact'] = None
                request.session['teacher_id'] = None
                request.session['teacher_fname'] = None
                request.session['teacher_lname'] = None
                request.session['teacher_contact'] = None
                return Response(template_name='admin_index.html')

            
    except School_user.DoesNotExist:
        return Response(template_name='login.html')

@checkParent
def sessionValues(request):
    print (1+1)
    return HttpResponse("Success in session values")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@checkAdmin
@csrf_exempt
@api_view(['GET'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def teacher_registration(request):
    return Response(template_name='admin_teacher_registration.html')

@checkAdmin
@csrf_exempt
@api_view(['POST'])
@authentication_classes(())
@renderer_classes((JSONRenderer,))
@permission_classes(())
def addTeacher(request):
    isExist=0
    isExist=School_user.objects.filter(user_name=request.data['teacherEmail']).count()
    if isExist==0:
        userObj = School_user()
        userObj.user_name = request.data['teacherEmail']
        userObj.password = unique_id = get_random_string(length=5)
        userObj.is_active = True
        userObj.user_type = 3
        userObj.save()
        #userObj1=School_user.objects.get(user_name = request.data['teacherEmail'])
        teacherUser = Teacher()
        teacherUser.user_id = userObj
        teacherUser.fname = request.data['teacherFName']
        teacherUser.lname = request.data['teacherLName']        
        teacherUser.contact = request.data['teacherContact']
        teacherUser.save()
    # teacherObj= Teacher()
    # teacherFName = request.POST["teacherFName"] 
    # lname = request.POST["lname"]
    # contact = request.POST["contact"]

    # studInstance = School_user.objects.get(user_id=int(studentId))
    # stud = Student()
    # #stud.student_id = 1
    # stud.user_id = studInstance
    # stud.fname = fname
    # stud.lname = lname
    # stud.contact = contact
    # stud.save()
    #lid=School_user.objects.latest('user_id')
    #lid=0
    #lid=School_user.objects.filter(user_name=request.data['teacherEmail']).count()
    #lsi= school_userSerializer(lid, many=False)
    #print "---------------------",lid
    #print "-----------------------", lsi.data['user_name']
    return Response({"Status":"Done"})
