$(document).ready(function(){

         $("#firstName_error_message").hide();
         $("#lastName_error_message").hide();
         $("#email_error_message").hide();
         $("#username_error_message").hide();
         $("#password_error_message").hide();
         $("#confirmPassword_error_message").hide();
         var error_firstName = false;
         var error_lastName = false;
         var error_email = false;
         var error_username = false;
         var error_password = false;
         var error_confirmPassword = false;
         $("#firstName").focusout(function(){
            check_firstName();
         });
         $("#lastName").focusout(function() {
            check_lastName();
         });
         $("#email").focusout(function() {
            check_email();
         });
         $("#username").focusout(function() {
            check_username();
         });
         $("#password").focusout(function() {
            check_password();
         });
         $("#confirmPassword").focusout(function() {
            check_confirmPassword();
         });
         function check_firstName() {
            var pattern = /^[a-zA-Z]*$/;
            var firstName = $("#firstName").val();
            if (pattern.test(firstName) && firstName !== '') {
               $("#firstName_error_message").hide();
               $("#firstName").css("border-bottom","2px solid #34F458");
            }
            if (firstName.length == 0){
               $("#firstName_error_message").html("First name should not be Empty");
               $("#firstName_error_message").show();
               $("#firstName").css("border-bottom","2px solid #F90A0A");
               error_firstName = true;
            }
            else if (firstName.length<5 || firstName.length>8){
               $("#firstName_error_message").html("First name should have min 5 characters and below 8 characters");
               $("#firstName_error_message").show();
               $("#firstName").css("border-bottom","2px solid #F90A0A");
               error_firstName = true;
            }

         }
         function check_lastName() {
            var pattern = /^[a-zA-Z]*$/;
            var lastName = $("#lastName").val();
            if (pattern.test(lastName) && lastName !== '') {
               $("#lastName_error_message").hide();
               $("#lastName").css("border-bottom","2px solid #34F458");
            }
            if (lastName.length==0){
               $("#lastName_error_message").html("Last name should not be empty");
               $("#lastName_error_message").show();
                $("#lastName").css("border-bottom","2px solid #F90A0A");
               error_lastName = true;
            }
            else if (lastName.length<5 || lastName.length>8){
               $("#lastName_error_message").html("Last name should have min 5 characters and below 8 characters");
               $("#lastName_error_message").show();
               $("#lastName").css("border-bottom","2px solid #F90A0A");
               error_lastName = true;
            }

         }

         function check_email() {
            var pattern = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
            var email = $("#email").val();
            if (pattern.test(email) && email !== '') {
               $("#email_error_message").hide();
               $("#email").css("border-bottom","2px solid #34F458");
            }
            else if(email.length ==0) {
               $("#email_error_message").html("Email Should not be empty");
               $("#email_error_message").show();
               $("#email").css("border-bottom","2px solid #F90A0A");
               error_email = true;
            }
            else {
               $("#email_error_message").html("Invalid Email");
               $("#email_error_message").show();
               $("#email").css("border-bottom","2px solid #F90A0A");
               error_email = true;
            }
         }
         function check_username() {
            var pattern = /^[a-zA-Z]*$/;
            var username= $("#username").val();
            if (pattern.test(username) && username !== '') {
               $("#username_error_message").hide();
               $("#username").css("border-bottom","2px solid #34F458");
            }
            else if(username.length ==0) {
               $("#username_error_message").html("Username Should not be empty");
               $("#username_error_message").show();
               $("#username").css("border-bottom","2px solid #F90A0A");
               error_username = true;
            }
            else if(username.length<4) {
               $("#username_error_message").html("Username Should have minimum 4 characters");
               $("#usename_error_message").show();
               $("#username").css("border-bottom","2px solid #F90A0A");
               error_username = true;
            }
            else if( username.length>6) {
               $("#username_error_message").html("Username Should be below 6 characters");
               $("#usename_error_message").show();
               $("#username").css("border-bottom","2px solid #F90A0A");
               error_username = true;
            }


         }
         function check_password() {

            var password= $("#password").val();

            if (password.length !==0) {
               $("#password_error_message").hide();
               $("#password").css("border-bottom","2px solid #34F458");
            }
            else if(password.length ==0) {
               $("#password_error_message").html("Password Should not be empty");
               $("#password_error_message").show();
               $("#password").css("border-bottom","2px solid #F90A0A");
               error_password = true;
            }
           else if(password.length<3) {
               $("#password_error_message").html("Username Should have minimum 3 characters");
               $("#password_error_message").show();
               $("#password").css("border-bottom","2px solid #F90A0A");
               error_password = true;
            }

         }
         function check_confirmPassword() {

            var confirmPassword= $("#confirmPassword").val();
             var password= $("#password").val();
            if (confirmPassword==password) {
               $("#confirmPassword_error_message").hide();
               $("#confirmPassword").css("border-bottom","2px solid #34F458");
            }
            else {
               $("#confirmPassword_error_message").html("Password and Confirm password did not match");
               $("#confirmPassword_error_message").show();
               $("#confirmPassword").css("border-bottom","2px solid #F90A0A");
               error_password = true;
            }
         }
         $("#registration-page").submit(function() {
             var error_firstName = false;
             var error_lastName = false;
             var error_email = false;
             var error_username = false;
             var error_password = false;
             var error_confirmPassword = false;

             check_firstName();
             check_lastName();
             check_email();
             check_username();
             check_password();
             check_confirmPassword();

            if (error_firstName === false && error_lastName === false && error_email === false && error_username === false && error_password==false && confirmPassword==false) {
               alert("Registration Successfull");
               return true;
            } else {
               alert("Please Fill the form Correctly");
               return false;
            }
         });
    });