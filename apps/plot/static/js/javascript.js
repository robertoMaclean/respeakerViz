$( document ).ready(function() {
    // initialize with defaults
	$("#input-id").fileinput();
 
	// with plugin options
	$("#input-id").fileinput({'showUpload':false, 'previewFileType':'any'});
	alert("hola")
});
