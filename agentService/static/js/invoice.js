$(document).ready(function(){
    var x = 1;
    var y= +$("#igst").val();
    var z= +$("#cgst").val();
       $("#totalTax").val(y+z);
    $("#invoice-button").click(function () {
        $('#count').val(x+1)

     $("table tr:last").show().clone(true).insertAfter("table tr:last").add().find("input").each(function () {
         $(this).val('').attr({
             'id': function (_, id) {
                 return id + x
             },
                 'name': function (_, name) {
                 return name.slice(0, -1) + x

             },
                 'value':function (_, value) {
                 return value + x
             }
         });
     });
     x++;
    });
 });