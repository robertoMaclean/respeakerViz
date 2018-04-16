$( document ).ready(function() {
    $('#graph').hide()
    click_buttons()
});

function click_buttons(){
	$('#users_interaction').on('click', function(){
		$('#plot_img').show()
		$('#graph').hide()
        $('#plot_img').attr('src','../media/plot/users_interaction.png');
        $('.panel-heading').text('Interacción entre los participantes');
    });

    $('#users_speak').on('click', function(){
    	$('#plot_img').show()
    	$('#graph').hide()
        $('#plot_img').attr('src','../media/plot/users_speak.png');
        $('.panel-heading').text('Tiempo de habla por participante');
    });

    $('#interv_time').on('click', function(){
    	$('#plot_img').hide()
    	$('#graph').show()
    	morris.setData(data.users)
    	console.log(data.users)
    });
}