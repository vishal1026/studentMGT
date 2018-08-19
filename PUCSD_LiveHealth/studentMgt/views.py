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
from random import randint


@checkAdmin
@csrf_exempt
@api_view(['POST'])
@authentication_classes(())
@renderer_classes((JSONRenderer,))
@permission_classes(())
def addExam(request):
    examObj = Exam()
    examObj.exam_name = request.data['examName']
    examObj.date = request.data['examDate']
    subObj=Subject.objects.get(subject_id=request.data['subject'])
    examObj.subject_id = subObj
    examObj.save()
    examSer = examSerializer(examObj, many=False)
    return Response(examSer.data)


@checkAdmin
@csrf_exempt
@api_view(['GET'])
@authentication_classes(())
@renderer_classes((JSONRenderer,))
@permission_classes(())
def examSubjectList(request):
    subObj = Subject.objects.all()
    sSer = subjectSerializer(subObj, many=True)
    return Response(sSer.data)

@checkAdmin
@csrf_exempt
@api_view(['GET'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def create_exam(request):
    return Response(template_name='admin_create_exam.html')


@checkAdmin
@csrf_exempt
@api_view(['POST'])
@authentication_classes(())
@renderer_classes((JSONRenderer,))
@permission_classes(())
def getCoursewiseClass(request):
    courseClassObj = Course_Class.objects.filter(course_id = request.data['courseID'])
    courseClassSer = course_ClassSerializer(courseClassObj, many=True)
    print "Years-----------------------", courseClassSer.data
    return Response(courseClassSer.data)

@checkAdmin
@csrf_exempt
@api_view(['POST'])
@authentication_classes(())
@renderer_classes((JSONRenderer,))
@permission_classes(())
def addSubject(request):
    courseClassObj = Course_Class.objects.get(class_id = request.data['currentYear'])
    subjectObj = Subject()
    subjectObj.class_id= courseClassObj
    subjectObj.subject_name = request.data['subjectName']

    cntTeachers= Teacher.objects.all().count()
    teacherObjs = Teacher.objects.all()
    j = randint(0,cntTeachers-1)
    subjectObj.teacher_id = teacherObjs[j]
    subjectObj.save()     
    return Response('{ "status" : "done"}')

@checkAdmin
@csrf_exempt
@api_view(['GET'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def add_subject(request):
    return Response(template_name='admin_add_subject.html')


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
    courseYears = int(request.data['courseYears'])
    courseObj.noOfYears = courseYears
    courseObj.department_id = deptId 
    courseObj.save()
    courseSer = courseSerializer(courseObj, many=False)
    cntTeachers= Teacher.objects.all().count()
    teacherObjs = Teacher.objects.all()

    for i in range(1,courseYears+1):
        j = randint(0,cntTeachers-1)
        ccObj = Course_Class()
        ccObj.course_id = courseObj
        ccObj.teacher_id = teacherObjs[j]
        ccObj.yearOfCourse = i
        ccObj.save()

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
        teacherUser = Teacher()
        teacherUser.user_id = userObj
        teacherUser.fname = request.data['teacherFName']
        teacherUser.lname = request.data['teacherLName']        
        teacherUser.contact = request.data['teacherContact']
        teacherUser.save()
    return Response({"Status":"Done"})

@checkAdmin
@csrf_exempt
@api_view(['GET'])
@authentication_classes(())
@renderer_classes((TemplateHTMLRenderer,))
@permission_classes(())
def student_registration(request):
    return Response(template_name='admin_register_student.html')


def studReg(request,parentObj):
    userObjS = School_user()
    userObjS.user_name = request.data['studentEmail']
    userObjS.password = unique_id = get_random_string(length=5)
    userObjS.is_active = True
    userObjS.user_type = 1
    userObjS.save()
    
    studentObj = Student()
    studentObj.user_id = userObjS
    studentObj.parent_id = parentObj
    studentObj.fname = request.data['studentFName']
    studentObj.lname = request.data['studentLName']
    studentObj.contact = request.data['studentContact']
    studentObj.save()

    ccObj = Course_Class.objects.get(course_id = request.data['studCourse'], yearOfCourse = 1 )
    ccObj.strength = ccObj.strength + 1
    ccObj.save()
    sicObj = Student_in_class()
    sicObj.student_id = studentObj
    sicObj.class_id = ccObj
    sicObj.save()
    return


@checkAdmin
@csrf_exempt
@api_view(['POST'])
@authentication_classes(())
@renderer_classes((JSONRenderer,))
@permission_classes(())
def addStudent(request):
    isParentExist = 0
    isStudentExist = 0 
    isStudentExist=School_user.objects.filter(user_name=request.data['studentEmail']).count()
    isParentExist=School_user.objects.filter(user_name=request.data['parentEmail']).count()
    if isParentExist==0:
        userObjP = School_user()
        userObjP.user_name = request.data['parentEmail']
        userObjP.password = unique_id = get_random_string(length=5)
        userObjP.is_active = True
        userObjP.user_type = 2
        userObjP.save()
        
        parentObj = Parent()
        parentObj.user_id = userObjP
        parentObj.fname = request.data['parentFName']
        parentObj.lname = request.data['parentLName']
        parentObj.contact = request.data['parentContact']
        parentObj.save()

        studReg(request,parentObj)

    elif isStudentExist==0:
        userObj = School_user.objects.get(user_name=request.data['parentEmail'])
        parentObj = Parent.objects.get(user_id=userObj)
        studReg(request,parentObj)

    return Response({"Status":"Done"})