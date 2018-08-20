$.ajax({
type:'GET',
    url:"http://localhost:8000/student_attendance_list/ ",
    success:function(msg){
      data=msg;
        var add_form='<form method="POST">';
        var table = $('<table class="table table-striped" id="attendance_display_table">');

        var columnCount = msg.length;
        var tableHeading=Object.keys(data[0]);

        //Add the header row.
        var row = $(table[0].insertRow(-1));
        var headerCell = $("<th />");
        headerCell.html("Id");
        row.append(headerCell);

        var headerCell = $("<th />");
        headerCell.html("Student Name");
        row.append(headerCell);

        var headerCell = $("<th />");
        headerCell.html("Last Name");
        row.append(headerCell);

        var headerCell = $("<th />");
        headerCell.html("Absent/Present");
        row.append(headerCell);
        var add_stud_id=[];
        //Add the data rows.
        for (var i = 0; i < msg.length; i++)
         {
            row = $(table[0].insertRow(-1));
            var cell = $("<td />");
            var stud_id=msg[i].student_id;
            add_stud_id.push(stud_id);
            cell.html(msg[i].student_id);
            row.append(cell);

            var cell = $("<td />");
            cell.html(msg[i].fname);
            row.append(cell);

            var cell = $("<td />");
            cell.html(msg[i].lname);
            row.append(cell);

            var cell = $("<td />");
            cell.html('<input type="checkbox" name="presenty"  value="'+stud_id+'">');
            row.append(cell);
        }
        var attendance_display_table = $("#attendance_display_table");
        attendance_display_table.append(add_form);
        attendance_display_table.append(table);
        var button="<input class='btn btn-primary' type='submit' onclick='submit_attendance("+stud_id+");' value='submit'></table></form>";
        attendance_display_table.append(button);
    }
    });




function submit_attendance(param)
 {
   var today = new Date();
   var dd = today.getDate();
   var mm = today.getMonth()+1;
   var yyyy = today.getFullYear();
   if(dd<10)
   {
    dd='0'+dd;
   }

   if(mm<10)
   {
    mm='0'+mm;
   }
   today = mm+'-'+dd+'-'+yyyy;

    var counter = 0,i = 0,url = [],input_obj = document.getElementsByTagName('input');
    for (i = 0; i < input_obj.length; i++)
    {
        if (input_obj[i].type === 'checkbox' && input_obj[i].checked === true)
        {
            counter++;
            url.push(input_obj[i].value);
        }
    }

    if (counter > 0)
    {
      url.toString();
      var class_id=1;
    $('#attendance_display_table').hide();
    $('#add_attendance').show();
    $.ajax({
        type:'POST',
            url:"http://localhost:8000/add_entry_in_attendance/ ",
            data:{
                'date' : today,
                'attendance_data' : url,
                'class_id' :class_id
            },
            success:function(deptList){
              alert("entry goes in database");
              //  console.log(deptList)
              //  window.location.reload();

            }
    });
    }
    else
    {
        alert('There is no checked checkbox');
    }
}
