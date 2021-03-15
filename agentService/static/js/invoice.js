$(document).ready(function(){
    var qty;
    var rate;
    var x = 1;
    var y= parseInt($("#igst").val());
    var z= parseInt($("#cgst").val());
    var w= y + z;
       $("#totalTax").val(w);
       alert($("#totalTax").val());

   /* $("#qty").keyup(function(){
    var qty=+$("#qty").val();
    $("#qty").keyup(function(){
    var rate=+$("#rate").val();
        $("#totalValue").val(qty*rate)
        alert($("#totalValue").val());

    });
  });*/

    $("#invoice-button").click(function () {
        $('#count').val(x+1)
    $("table tr:last").find("input").each(function () {
     $("table tr:last").show().clone().insertAfter("table tr:last");
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