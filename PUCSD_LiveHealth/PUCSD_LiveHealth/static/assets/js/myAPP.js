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
$.ajax({
type:'GET',
    url:"http://localhost:8000/department_list_table/ ",
    success:function(msg){
        console.log(msg)
        genTable(msg);
    }
    });

var data={};
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