function test(){
    $.ajax({
        type:'GET',
               url:"http://localhost:8000/foo/ ",
            success:function(msg){
              console.log(msg);
           }
          });
    
}