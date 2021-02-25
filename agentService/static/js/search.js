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

 /*$('#myInput').autocomplete({
    source: function (request, response) {
        $.getJSON("/agent/getKey/", function (data) {
            response($.map(data.search_list_dict,function (value, key) {
                return {
                    label: value,
                    value: key
                };
            }));
        });
    },
    minLength: 2,
    delay: 100
});*/


/*$(document).ready(function() {
      $("#myInput").autocomplete({
           source:"/agent/getKey",
           select: function(event,ui){
                   GetRedirectPage(ui.item.label,ui.item.value);
            }
       });
    });

    function GetRedirectPage(label, slug) {
          window.location.href = "/agent/"+slug;
    }*/

$(document).ready(function(){
    $("#myInput").autocomplete({
      source: "/agent/getKey/",
      select: function( event , ui ) {
                $("#myInput").val(ui.item.value);
                $("#search-form").submit();
        }
    });
 });