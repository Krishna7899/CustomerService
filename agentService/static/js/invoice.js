$(document).ready(function(){
    var qty;
    var rate;
    var x = 1;
    var y= +$("#igst").val();
    var z= +$("#cgst").val();
       $("#totalTax").val(y+z);

   /* $("#qty").keyup(function(){
    var qty=+$("#qty").val();
    $("#qty").keyup(function(){
    var rate=+$("#rate").val();
        $("#totalValue").val(qty*rate)
        alert($("#totalValue").val());

    });
  });*/
  var $tblrows = $("#table tr:last");
          $tblrows.find('#rate').on('change', function () {
        var qty = +$tblrows.find("#qty").val();
        var price = +$tblrows.find("#rate").val();
            $("#totalValue").val(qty*price);
           /* alert($("#totalValue").val());*/
        });
    $("#invoice-button").click(function () {
        $('#count').val(x+1)
     $("table tr:last").show().clone().insertAfter("table tr:last").add().find("input").each(function () {
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