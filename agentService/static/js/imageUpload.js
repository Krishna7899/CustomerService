/*function myImageUpload() {
  var x = document.getElementById("upload");
  var y = document.getElementById("updateImage-btn")


    if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}*/

$(document).ready(function(){
    $("#updateImage-btn").click(function(){
        $("#updateImage-btn").hide();
        $("#upload").show();
    });
    $("#image-upload-button").click(function(){
        $("#upload").hide();
        $("#updateImage-btn").show();
    });
});




