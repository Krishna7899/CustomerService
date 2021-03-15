$(document).ready(function(){
    var qty;
    var rate;
    var x = 1;
    var y=+$("#igst0").val();
    var z= +$("#cgst0").val();
       $("#totalTax").val(y+z);
       /*alert($("#totalTax").val());*/

    var $tblrows = $("#table tr:last");
      $tblrows.find('#rate0').on('change', function () {
       var qty = +$tblrows.find("#qty0").val();
       var price = +$tblrows.find("#rate0").val();
        $("#totalValue0").val(qty*price);
        /*alert($("#totalValue0").val());*/
   });


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
   });
    $("table tr:last").show().clone().insertAfter("table tr:last").find("input").val().each(function () {
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