/*$(document).ready(function(){
    var qty;
    var rate;
    var x = 1;
    var y= +$("#igst0").val();
    var z= +$("#cgst0").val();
       $("#totalTax").val(y+z);*/
       /*alert($("#totalTax").val());*/

  /*  var $tblrows = $("#table tr:last");
      $tblrows.find('#rate0').on('change',function (){
       var qty = +$tblrows.find("#qty0").val();
       var price = +$tblrows.find("#rate0").val();
        $("#totalValue0").val(qty*price);

   });*/


   /* $("#qty").keyup(function(){
    var qty=+$("#qty").val();
    $("#qty").keyup(function(){
    var rate=+$("#rate").val();
        $("#totalValue").val(qty*rate)
        alert($("#totalValue").val());

    });
  });*/

 /*   $("#invoice-button").click(function () {
        $('#count').val(x+1)
    $("table tr:last").show().clone().insertAfter("table tr:last").find("input").each(function () {
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
 });*/


 $(document).ready(function(){
    var i=1;
    var j=18;
    $("#add_row").click(function(){b=i-1;
        $('#count').val(i+1)
      	/*$('#tab_logic').append('<tr id="addr'+(i+1)+'"></tr>');*/
      	$("#tab_logic tr:last").show().clone(true).add('#addr'+i).insertAfter("#tab_logic tr:last").find("input").each(function () {
      	$('#tab_logic tr:last').find('td:first-child').html(i+1);
      	$('.tax-percentage').val(j);
        $(this).val('').attr({
             'id': function (_, id) {
                 return id + i
             },
                 'name': function (_, name) {
                 return name.slice(0, -1) + i

             },
                 'value':function (_, value) {
                 return value + i
             }
         });
        });
      	i++;
  	});
  /*	$(document).on('click', 'button.btn', function () {
    var y =  $('#count').val()

       alert($('#count').val(
    ));
    $(this).closest('tr').remove();
    calc();
        return false;
    });*/
   $(document).on('click', 'button.delete', function (){
      var c=  $("#count").val();
		$(this).closest('tr').remove();
		calc();
	});

	$('#tab_logic tbody').on('keyup change',function(){
		calc();
	});
	$('#tax').on('keyup change',function(){
		calc_total();
	});
    $('#transport_amount').on('change',function(){
              calc_Grand_total();
    });

});

function calc()
{
	$('#tab_logic tbody tr').each(function(i, element) {
		var html = $(this).html();
		if(html!='')
		{
			var qty = $(this).find('.qty').val();
			var price = $(this).find('.price').val();
		    $(this).find('.total').val(qty*price);
			$(this).find('.taxPrice').val(qty*price*18/100);
			calc_total();
		}
    });
}
/*var prodCost = $('.total').val();
var taxPrice = $('.tax-percentage').val();
               $('.taxPrice').val((prodCost*taxPrice)/100)*/


function calc_total()
{
	total=0;
	$('.total').each(function() {
        total += parseInt($(this).val());
    });
	$('#sub_total').val(total.toFixed(2));
	tax_sum=total/100*$('#tax').val();
	transport=$("#transport_amount").val();
	$('#tax_amount').val(tax_sum.toFixed(2));
	$('#total_amount').val((tax_sum+total).toFixed(2));
}

function calc_Grand_total(){
      var tr_charges=+$('#transport_amount').val();
      var gTotal=+$('#total_amount').val();
       $('#total_amount').val((tr_charges+gTotal).toFixed(2));

}