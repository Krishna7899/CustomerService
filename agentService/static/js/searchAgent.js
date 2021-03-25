/* $(document).ready(function() {
         $('#tabs li a:not(:first)').addClass('inactive')
         $('.container').hide();
         $('.container:first').show();
         $('#tabs li a').click(function(){
            var t = $(this).attr('id');
         if($(this).hasClass('inactive')){ //this is the start of our condition
            $('#tabs li a').addClass('inactive');
            $(this).removeClass('inactive');
            $('.container').hide();
            $('#'+ t + 'C').fadeIn('slow');
         }
        });
});*/

$(document).ready(function(){
  $('#button-2').click(function(e){
     var firstName = $("#firstName").val();
     var lastName = $("#lastName").val();
     var username = $("#username").val();
     var advSearchMsg = "{{advSearchMsg}}";
     if (firstName.length == 0 && lastName.length ==0 && username.length==0){
           e.preventDefault()
        $("#error_message").html("At least One Field value is mandatory!!");
        $("#error_message").show();

        }
     else{
          $('#tab2').show();
          $('#tab1').hide();
         $("#error_message").hide();
     }
     if( advSearchMsg == "No Data" ){
          $("#view_error_message").html("No Data found Please try with Other Details");
          $("#view_error_message").show();

        }else{
           $("#view_error_message").hide();
        }
  });


/*$(document.ready).function(){
   var advSearchMsg = "{{advSearchMsg}}";
   if (advSearchMsg == "NoData"){
        e.preventDefault()
        $("#error_message").html("No Data Found Please try with other details");
        $("#error_message").show();
   }
}*/


$('ul.tabs').each(function(){
    var $active, $content, $links = $(this).find('a');
    $active = $links.first().addClass('active');
    $content = $($active.attr('href'));
    $links.not(':first').each(function () {
    $($(this).attr('href')).hide();
    });

    $(this).on('click', 'a', function(e){
        $active.removeClass('active');
        $content.hide();
        $active = $(this);
        $content = $($(this).attr('href'));
        $active.addClass('active');
        $content.show();
        e.preventDefault();
    });
});
});

/*$("#button-2").onclick(function(){
     var firstName = $("#firstName").val();
     var lastName = $("#lastName").val();
     var username = $("#username").val();
     if (firstName.length == 0 && lastName.length ==0 && username.length==0){
        $("#error_message").html("At least One Field value is mandatory!!");
        $("#error_message").show();

        }
     else{
         $("#error_message").hide();
     }
     });*/

function changePlaceholder1() {
        $('#placeholder').attr('placeholder','Enter user id ');
        $('.search-field-input').attr('type','number')
       }

function changePlaceholder2() {
        $('#placeholder').attr('placeholder','Enter user name ');
        $('.search-field-input').keypress(function(e){
            var key = e.keyCode;
            var fn = $(".search-field-input").val();
            var regex = /^[a-zA-Z0-9\_]+$/
             if (regex.test(fn)==false){
                  e.preventDefault();
                alert('Only characters followed by numbers  are allowed');
             }

      });





        }

$(document).ready(function() {
   $('.search-field-input').keypress(function(e){
        if (!$('input[name=radio]:checked').val())
        {
        e.preventDefault();
        alert("Radio Button Not Checked");
        }

   });

});