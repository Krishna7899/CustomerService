$(document).ready(function() {
     $("#pButton").on('click',function () {
     $(".pAddress-update-text").prop("readonly",false);
     $(".pAddress-update-text").css({"display":"block","border":"1px solid #ddd"});
     $(".pAddress-update-button").css({"visibility":"visible",
                                           "background": "#87ceeb","border":"none","border-radius":"2px","color":"white"});
     /*$(".pAddressType-text").prop("readonly",false)*/
     $(".pAddressType-text").css({"visibility":"visible","border":"1px solid #ddd"})
     $("#pButton").hide();
     });
});

$(document).ready(function() {
     $("#tButton").on('click',function () {
     $(".tAddress-update-text").prop("readonly",false);
     $(".tAddress-update-text").css({"display":"block","border":"1px solid #ddd"});
     $(".tAddress-update-button").css({"visibility":"visible","margin-bottom":"30px",
                                "background": "#87ceeb","border":"none","border-radius":"2px","color":"white"});
     $(".tAddressType-text").css({"visibility":"visible","border":"1px solid #ddd"});
     $("#tButton").hide();
     });
});