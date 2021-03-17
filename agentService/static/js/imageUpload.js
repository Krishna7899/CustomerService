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
    $("#image-upload-button").click(function(e){
       if ($('#image-file-upload')[0].files.length === 0) {
             e.preventDefault();
             $("#image-error").html("No File Selected");
             $("#image-error").css({"color":"red","font-size":"12px"}).show();
      }else{
        $("#upload").hide();
        $("#updateImage-btn").show();
        }
    });
});




