$( document ).ready(function() {
    click_buttons()
});

function click_buttons(){
	$('#users_interaction').on('click', function(){
		alert("hola")
		console.log("Hola")
		$('#plot_img').show()
        $('#plot_img').attr('src','../media/plot/users_interaction.png');
        $('.panel-heading').text('Interacción entre los participantes');
    });

    $('#users_speak').on('click', function(){
    	$('#plot_img').show()
        $('#plot_img').attr('src','../media/plot/users_speak.png');
        $('.panel-heading').text('Tiempo de habla por participante');
    });

    $('#interv_time').on('click', function(){
    	alert("hide")
    	$('#plot_img').hide()
    });

}