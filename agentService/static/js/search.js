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




 $('#myInput').autocomplete({
    source: function (request, response) {
          $.getJSON("/agent/getKey?term=" + request.term, function (data) {
          console.log(data);
            response($.map(data, function (value, key) {
                console.log(value);
                return {
                    label: value.label,
                    value: value.value
                };
            }));
        });
    },
    minLength: 1,
    delay: 100
});