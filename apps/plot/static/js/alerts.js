const swalWithBootstrapButtons = swal.mixin({
  confirmButtonClass: 'btn btn-success',
  cancelButtonClass: 'btn btn-danger',
  buttonsStyling: false,
})


function delete_one(filename){
  swalWithBootstrapButtons({
      title: '¿Estas seguro?',
      text: "Su reporte será eliminado",
      type: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Si, eliminar',
      cancelButtonText: 'No, cancelar',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        DeleteFile(filename)
        swalWithBootstrapButtons(
          'Eliminado!',
          'Su reporte se ha eliminado exitosamente',
          'success'
        )
      } else if (
        // Read more about handling dismissals
        result.dismiss === swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons(
          'Cancelado',
          'Su reporte no se ha eliminado',
          'error'
        )
      }
    })
}

function delete_alert(){ 
  if(some_check_select()){
    swalWithBootstrapButtons({
      title: '¿Estas seguro?',
      text: "Sus reportes serán eliminados",
      type: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Si, eliminar',
      cancelButtonText: 'No, cancelar',
      reverseButtons: true
    }).then((result) => {
      if (result.value) {
        DeleteFiles()
        swalWithBootstrapButtons(
          'Eliminado!',
          'Sus reportes se han eliminado exitosamente',
          'success'
        )
      } else if (
        // Read more about handling dismissals
        result.dismiss === swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons(
          'Cancelado',
          'Sus reportes no se han eliminado',
          'error'
        )
      }
    })

  }else {
    swal("Mensaje", "Debe seleccionar al menos un reporte", "warning")
  }
  
}

function some_check_select(){
  for(var i=0;i<$("#myTable #checkbox").length;i++){
    if($("#myTable #checkbox")[i].checked){
      return true
    }
  }
  return false
}