$( document ).ready(function() {
    $("#search").on("change keyup keydown",function(){
      SearchFiles();
    });
    CheckAll()
    $("#delete-files").on("click", function() {
      delete_alert();
    });
    $("#delete").on("click", function() {
      var filename = $(this).closest("tr")   // Finds the closest row <tr> 
                       .find("#name")     // Gets a descendent with class="nr"
                       .text();
      delete_one(filename)
    })
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

function DeleteFiles() {
  for(var i=0;i<$("#myTable #checkbox").length;i++){
    if($("#myTable #checkbox")[i].checked){
      $.ajax({
          type: "GET",
          url: '/plot/delete_files/'+String(name),
          success: function(data) {
              window.location.reload()
              console.log('success')
          },
          error: function(data) {
              console.log('error')
          },
      });
    }
  }
};

function DeleteFile(filename) {
  $.ajax({
          type: "GET",
          url: '/plot/delete_files/'+filename,
          success: function(data) {
              window.location.reload()
              console.log('success')
          },
          error: function(data) {
              console.log('error')
          },
      });
}