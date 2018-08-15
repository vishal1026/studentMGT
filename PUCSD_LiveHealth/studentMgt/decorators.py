from django.core.exceptions import PermissionDenied
from models import *

def checkStudent(function):
    def wrap(request, *args, **kwargs):
        if request.session['user_type'] == 1:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def checkParent(function):
    def wrap(request, *args, **kwargs):
        if request.session['user_type'] == 2:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def checkTeacher(function):
    def wrap(request, *args, **kwargs):
        if request.session['user_type'] == 3:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def checkAdmin(function):
    def wrap(request, *args, **kwargs):
        if request.session['user_type'] == 4:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def checkSuperUser(function):
    def wrap(request, *args, **kwargs):
        if request.session['user_type'] == 5:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap