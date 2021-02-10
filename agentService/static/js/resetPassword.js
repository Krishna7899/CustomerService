
function resetPassword() {
  var x = document.getElementById("resetPassword");
  var y = document.getElementById("profile-details");
  var z = document.getElementById("updateProfile");
        z.style.display = "none"

    if (y.style.display === "block"){
         y.style.display = "none"
    }else{
        y.style.display = "block"
    }
    if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}