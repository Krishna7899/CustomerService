$(document).ready(function(){
    $("#searchPartner").autocomplete({
      source: "/agent/partnerLiveSearch/",
      select: function( event , ui ) {
                $("#searchPartner").val(ui.item.value);
                $("#partner-search-form").submit();
        }
    });
 });