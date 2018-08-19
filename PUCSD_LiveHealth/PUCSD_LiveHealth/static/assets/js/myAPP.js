/*
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method){
    return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings){
        if(!csrfSafeMethod(settings.type)){
            xhr.setRequestHeader("X-CSRFToken",document.getElementById('csrf').value);
        }
    }
});
*/
var data={};
var globalDepartmentData;
var courseData;
$.ajax({
type:'GET',
    url:"http://localhost:8000/department_list_table/ ",
    success:function(msg){
        console.log(msg)
        globalDepartmentData=msg;
        genTable(msg);
    }
    });


/*Ajax call for Course*/
$.ajax({
    type:'GET',
        url:"http://localhost:8000/course_list/ ",
        success:function(msg){
            console.log(msg);
            courseData=msg;
            genCourseTable(msg);
            studRegSelMenu();
            
        }
    });
   
/*Dynamic Table Genaration*/    
function genCourseTable(msg){
    data=msg;

    var table = $('<table class="table table-striped" id="course_display_table">');
        //Get the count of columns.
    var columnCount = msg.length;
    var tableHeading=Object.keys(data[0]) 
    //Add the header row.
    var row = $(table[0].insertRow(-1));
    
    var headerCell = $("<th />");
    headerCell.html("Course ID");
    row.append(headerCell);

    var headerCell = $("<th />");
    headerCell.html("Course Name");
    row.append(headerCell);

    var headerCell = $("<th />");
    headerCell.html("Department Name");
    row.append(headerCell);

    /*for (var i = 0; i < tableHeading.length; i++) {
        var headerCell = $("<th />");
        headerCell.html(tableHeading[i]);
        row.append(headerCell);
    }*/

    //Add the data rows.
    for (var i = 0; i < msg.length; i++) {
        row = $(table[0].insertRow(-1));

        var cell = $("<td />");
        cell.html(msg[i].course_id);
        row.append(cell);

        var cell = $("<td />");
        cell.html(msg[i].course_name);
        row.append(cell);

        var cell = $("<td />");
        cell.html(msg[i].department_id.name);
        row.append(cell);

        /*for (var j = 0; j <tableHeading.length; j++) {
            var cell = $("<td />");
            cell.html(msg[i][tableHeading[j]]);
            row.append(cell);
        }*/
        
    }

    var course_display_table = $("#course_display_table");
    course_display_table.html("");
    course_display_table.append(table);
}
            
function addCourse(){
var courseName = document.getElementById('course').value;
var deptID = document.getElementById('deptList').value;
var courseYears = document.getElementById('courseYears').value;

$.ajax({
    type:'POST',
        url:"http://localhost:8000/add_entry_in_course/ ",
        data:{
            'courseName' : courseName,
            'deptID' : deptID,
            'courseYears' : courseYears
        },
        success:function(deptList){
            console.log(deptList)
            window.location.reload();
            
        }
});
}


function genTable(msg){
    data=msg;

    var table = $('<table class="table table-striped" id="department_display_table">');
     //Get the count of columns.
    var columnCount = msg.length;
    var tableHeading=Object.keys(data[0]) 
    //Add the header row.
    var row = $(table[0].insertRow(-1));
    for (var i = 0; i < tableHeading.length; i++) {
        var headerCell = $("<th />");
        headerCell.html(tableHeading[i]);
        row.append(headerCell);
    }

    //Add the data rows.
    for (var i = 0; i < msg.length; i++) {
        row = $(table[0].insertRow(-1));
        for (var j = 0; j <tableHeading.length; j++) {
            var cell = $("<td />");
            cell.html(msg[i][tableHeading[j]]);
            row.append(cell);
        }
    }

    var department_display_table = $("#department_display_table");
    department_display_table.html("");
    department_display_table.append(table);
}

function addDepartment(){
    var deptName=document.getElementById('deptName').value;
    $.ajax({
        type:'POST',
            url:"http://localhost:8000/add_entry_in_department/ ",
            data:{
                deptName : deptName
            },
            success:function(deptList){
                console.log(deptList)
                
            }
            });        
}

function addOption(elt,val){
    var select = document.getElementById("deptList");
    select.options[select.options.length] = new Option(elt,val,false, false);
}

function deptSelMenu(){
    $('#deptList').empty();
    cnt = globalDepartmentData.length;
    addOption("Select Department",0);
    for(var i = 0; i < cnt; i++ ){
        addOption(globalDepartmentData[i].name, globalDepartmentData[i].department_id);
    }
}



function studCourseAddOp(elt,val){
    var select = document.getElementById("studCourseList");
    select.options[select.options.length] = new Option(elt,val,false, false);
}

function studRegSelMenu(){
    $('#studCoursetList').empty();
    cnt = courseData.length;
    studCourseAddOp("Select Course",0);
    for(var i = 0; i < cnt; i++ ){
        studCourseAddOp(courseData[i].course_name, courseData[i].course_id);
    }
}

/* Admin Add Subject*/

function subCourseAddOp(elt,val){
    var select = document.getElementById("courseList");
    select.options[select.options.length] = new Option(elt,val,false, false);
}

function addCourseSelMenu(){
    $('#courseList').empty();
    cnt = courseData.length;
    subCourseAddOp("Select Course",0);
    for(var i = 0; i < cnt; i++ ){
        subCourseAddOp(courseData[i].course_name, courseData[i].course_id);
    }
}

function yearOfCourseAddOp(elt,val){
    var select = document.getElementById("courseYears");
    select.options[select.options.length] = new Option(elt,val,false, false);
}

function addCourseClassSelMenu(classList){
    $('#courseYears').empty();
    cnt = classList.length;
    yearOfCourseAddOp("Select Class",0);
    for(var i = 0; i < cnt; i++ ){
        yearOfCourseAddOp(classList[i].yearOfCourse, classList[i].class_id);
    }
}


function courseSelMenu(){
    $("#courseYears").hide();
    addCourseSelMenu();   
}

function showCourseYear(){
    $("#courseYears").show();
    var courseID = document.getElementById('courseList').value;

    $.ajax({
        type:'POST',
            url:"http://localhost:8000/getCoursewiseClass/ ",
            data:{
                'courseID' : courseID
            },
            success:function(classList){
                console.log(classList);
                addCourseClassSelMenu(classList);
            }
    });
}

function addSubject(){
    var currentYear = document.getElementById('courseYears').value;
    var subjectName = document.getElementById('subjectName').value;
    $.ajax({
        type:'POST',
            url:"http://localhost:8000/addSubject/ ",
            data:{
                'currentYear' : currentYear,
                'subjectName' : subjectName
            },
            success:function(subjectEntry){
                alert("Subject Added Successfully");
                window.location.reload()
            }
    });    
}

/* Exam Creation*/

function subjectAddOp(elt,val){
    var select = document.getElementById("examSubject");
    select.options[select.options.length] = new Option(elt,val,false, false);
}

function subjectSelMenu(examSubjectList){
    $('#examSubject').empty();
    cnt = examSubjectList.length;
    subjectAddOp("Select Subject",0);
    for(var i = 0; i < cnt; i++ ){
        subjectAddOp(examSubjectList[i].subject_name, examSubjectList[i].subject_id);
    }
}

function getSubject(){
$.ajax({
    type:'GET',
        url:"http://localhost:8000/examSubjectList/ ",
        success:function(examSubjectList){
            console.log(examSubjectList);
            subjectSelMenu(examSubjectList);
            
        }
    });
}

function addExam(){
var examName = document.getElementById('examName').value;
var examDate = document.getElementById('examDate').value;
var subject = document.getElementById('examSubject').value;
$.ajax({
    type:'POST',
        url:"http://localhost:8000/addExam/ ",
        data:{
            'examName' : examName,
            'examDate' : examDate,
            'subject' : subject
        },
        success:function(subjectEntry){
            alert("Exam Added Successfully");
            window.location.reload()
        }
});    
}