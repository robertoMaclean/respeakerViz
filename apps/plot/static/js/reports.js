$( document ).ready(function() {
    $("#search").on("change keyup keydown",function(){
      SearchFiles();
    });
    CheckAll()
    $("#delete-files").on("click", function() {
      delete_alert();
    });
    $(".delete").on("click", function() {
      var filename = $(this).closest("tr")   // Finds the closest row <tr> 
                       .find(".name")     // Gets a descendent with class="nr"
                       .text();
      delete_one(filename)
    });
    $("#group-analyze").on("click", function() {
        groupPlots();
    });
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
  for(var i=0;i<$("#myTable .checkbox").length;i++){
    if($("#myTable .checkbox")[i].checked){
      var name = $("#myTable tr .name")[i].textContent  
      console.log(name)
      $.ajax({
          type: "DELETE",
          url: '/plot/delete_files/'+name,
          headers: { "X-CSRFToken": getCookie("csrftoken") },
          success: function(data) {
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
          type: "DELETE",
          url: '/plot/delete_files/'+filename,
          success: function(data) {
              console.log('success')
          },
          error: function(data) {
              console.log('error')
          },
      });
}

function groupPlots() {
  groups = getNames()
  if(groups.length>=2){
    $.ajax({
      type: "POST",
      url: '/plot/group_plots',
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      data: {
        groups: groups
      },
      dataType: 'json',
      success: function(data) {
          console.log('success')
          window.location.replace("./group_plots");
      },
      error: function(data) {
          console.log('error')
      },
    });
  }else{
    swalWithBootstrapButtons(
          'Advertencia',
          'Debe seleccionar al menos dos grupos',
          'warning'
        )
  }
  
}

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

 function getNames(){
  var names = []
  for(var i=0;i<$("#myTable .checkbox").length;i++){
    if($("#myTable .checkbox")[i].checked){
      names.push($("#myTable tr .name")[i].textContent)
    }
  }
  return names;
}