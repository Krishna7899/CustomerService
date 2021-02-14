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
/*$(document).ready(function () {
    $('#myList').change(function(){
    var value = $(this).val();
    $('#myInput').val(value);
    })
});
$(document).ready(function () {
    $('#search-submit').click(function(){
            $('#myList').toggle();
    })
});*/
/*auto complete */
 $( function(){
    $("#myInput").autocomplete({
      source: "/agent/getKey/",
      select: function( event , ui ) {
                /*var value = ui.item.value;*/
                var url = "/agent/%s" % ui.item.value;
                $(location).prop('href',"http://127.0.0.1:8000/agent/"+ui.item.value+"/");
           /* alert( "You selected: " + ui.item.value );*/
        }
    });
 });