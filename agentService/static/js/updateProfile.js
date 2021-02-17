/*$(document).ready(function() {
  //toggle the component with class accordion_body
  $(".accordion_head").click(function() {
    if ($('.accordion_body').is(':visible')) {
      $(".accordion_body").slideUp(300);
      $(".plusminus").text('+');
    }
    if ($(this).next(".accordion_body").is(':visible')) {
       $(this).next(".accordion_body").slideUp(300);
       $(this).children(".plusminus").text('+');
    }
    else {
      $(this).next(".accordion_body").slideDown(300);
      $(this).children(".plusminus").text('-');
    }
  });




});*/
$(document).ready(function() {
$('.change-password-submit').click(function(e){
    var password= $("#password-field").val();
    var confirmPassword=$("#confirm-password-field").val();
    if (confirmPassword!=password){
        e.preventDefault()
        $("#errorMessage").html("Password and Confirm password did not match");
        $("#errorMessage").show();

    }
    else{
        $("#errorMessage").hide();
    }
});
});
/*$(document).ready(function() {
$(".accordion_head").click(function(){
    if ($(this).find(".accordion_body").slideDown('slow');

});
});*/
/*$(document).ready(function(){
      $('#button-2').click(function(e){
          e.preventDefault()
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
});*/

/*$(document).ready(function() {
        $("#tabs").tabs({
                active: false,
                collapsible: true
            })
})*/

/*$(document).ready(function() {
  $("#tab2-updateProfile").click(function() {
    $("#profile-details").hide();
    $("#tab3-change").hide();
    $("#tab2-update").toggle();
  });
});
$(document).ready(function() {
 $("#tab3-changePassword").click(function() {
    $("#profile-details").hide();
    $("#tab2-update").hide();
    $("#tab3-change").toggle();
  });
});*/
/*$(document).ready(function() {
 $("#tab1-profile-details").click(function() {
    $("#profile-details").toggle();
    $("#tab2-update").hide();
    $("#tab3-change").hide();
  });
});

$(document).ready(function() {
 $("#update-profile").click(function() {
    $("#tab2-update").toggle();
    $("#profile-details").hide();
    $("#tab3-change").hide();
    $("#address").hide();
  });
});

$(document).ready(function() {
 $("#change-password").click(function() {
    $("#profile-details").hide();
    $("#tab2-update").hide();
    $("#tab3-change").toggle();
  });
});*/
