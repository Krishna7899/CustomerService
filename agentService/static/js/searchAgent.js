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
     if (firstName.length == 0 && lastName.length ==0 && username.length==0){
        e.preventDefault()
        $("#error_message").html("At least One Field value is mandatory!!");
        $("#error_message").show();

        }
     else{
         $("#error_message").hide();
     }
  });

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
        $('#placeholder').attr('placeholder',
            'Enter user id ');
    }

function changePlaceholder2() {
        $('#placeholder').attr('placeholder',
            'Enter user name ');
    }
