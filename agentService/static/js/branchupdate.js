$(document).ready(function(){
    $("#searchBranch").autocomplete({
      source: "/agent/branchLiveSearch",
      select: function( event , ui ) {
                $("#searchBranch").val(ui.item.value);
                $("#branch-search-form").submit();
        }
    });
 });