/*$(document).ready(function(){
  $(".search-item").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".topnav").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});*/

/*$(document).ready(function(){

  // Initialize select2
  $("#selUser").select2();

  // Read selected option
  $('#but_read').click(function(){
    var username = $('#selUser option:selected').text();
    var userid = $('#selUser').val();

    $('#result').html("id : " + userid + ", name : " + username);

  });
});*/

$(document).ready(function(){
  $("#myInput").on("keyup", function(){
    var value = $(this).val().toLowerCase();
    $("#myList li").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});