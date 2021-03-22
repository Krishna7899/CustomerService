$(document).ready(function(){

     $('#partner-name').keypress(function(e){
            var key = e.keyCode;
            var fn = $("#partner-name").val();
            var regex = /^[a-zA-Z\_]+$/
             if (regex.test(fn)==false){
                  e.preventDefault();
                alert('Only characters are allowed');
             }
            if (key >= 48 && key <= 57) {
                e.preventDefault();
                alert('Only characters are allowed');
            }
      });
       $('#partner-code').keypress(function(e){
            var key = e.keyCode;
            var fn = $("#partner-code").val();
            var regex = /^[0-9a-zA-Z\_]+$/
             if (regex.test(fn)==false){
                  e.preventDefault();
                alert('Partner code should contain only Characters and Numbers');
             }
      });
       $('#partner-GSTCode').keypress(function(e){
            var key = e.keyCode;
            var fn = $("#partner-GSTCode").val();
            var regex = /^[0-9a-zA-Z\_]+$/
             if (regex.test(fn)==false){
                  e.preventDefault();
                alert('GST code should contain only Characters and Numbers');
             }
      });
});






$(document).ready(function(){
    $("#searchPartner").autocomplete({
      source: "/agent/partnerLiveSearch/",
      select: function( event , ui ) {
                $("#searchPartner").val(ui.item.value);
                $("#partner-search-form").submit();
        }
    });
 });