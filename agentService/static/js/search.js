/*$("#myOption").on('change', function () {
  var value = $("#myOption").val();
  if (value != "") {
    $('#myInput').val(value)
  }
}).trigger('change');*/

/*$("#myOption").click(function(event)
    var value = $("#myOption").val();
    $("#myInput").val(value);
});
*/

/*$(document).ready(function(){
  $('#myOption').click(function(){
  var value = $("#myOption").val();
  $('#myInput').attr('value',value);
   });
});*/
$(document).ready(function () {
    $('#myList').change(function(){
    var value = $(this).val();
    $('#myInput').val(value);
    })
});
/*$(document).ready(function () {
    $('#search-submit').click(function(){
            $('#myList').show();
    })
});*/
