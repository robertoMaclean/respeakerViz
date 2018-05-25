$( document ).ready(function() {
    $("#search").on("change keyup keydown",function(){
      SearchFiles()
    })
    CheckAll()
});

function SearchFiles() {
  // Declare variables 
  var input, filter, table, tr, td, i;
  input = $("#search")[0];
  console.log(input.value)
  filter = input.value.toUpperCase();
  tr = $("#myTable tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {   
    td_name = $(tr[i]).find("td")[1];
    td_date = $(tr[i]).find("td")[2];
    if (td_name||td_date) {
      if (td_name.innerHTML.toUpperCase().indexOf(filter)  > -1) {
        tr[i].style.display = "";
      }
      else if(td_date.innerHTML.toUpperCase().indexOf(filter)  > -1) {
        tr[i].style.display = "";
      }
      else
      {
        tr[i].style.display = "none";
      }
    } 
  }
}

function CheckAll() {
  $("#myTable #checkall").click(function () {
        if ($("#myTable #checkall").is(':checked')) {
            $("#myTable input[type=checkbox]").each(function () {
                $(this).prop("checked", true);
            });

        } else {
            $("#myTable input[type=checkbox]").each(function () {
                $(this).prop("checked", false);
            });
        }
    });
    
    $("[data-toggle=tooltip]").toolt
}