$(document).ready(function() {
     $("#pButton").on('click',function () {
     $(".pAddress-update-text").prop("readonly",false);
     $(".pAddress-update-text").css({"display":"block","border":"1px solid black"});
     $(".pAddress-update-button").css({"visibility":"visible"});
     $("#pButton").hide();
     });
});

$(document).ready(function() {
     $("#tButton").on('click',function () {
     $(".tAddress-update-text").prop("readonly",false);
     $(".tAddress-update-text").css({"display":"block","border":"1px solid black"});
     $(".tAddress-update-button").css({"visibility":"visible","margin-bottom":"30px"});
     $("#tButton").hide();
     });
});