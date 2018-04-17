$( document ).ready(function() {
    $('#graph').hide()
	$('#users-footer').hide()    
    click_buttons()
});

function click_buttons(){
	$('#users_interaction').on('click', function(){
		$('#plot_img').show()
		$('#graph').hide()
		$('#graph1').hide()
		$('#users-footer').hide()    
        $('#plot_img').attr('src','../media/plot/users_interaction.png');
        $('.panel-heading').text('Interacción entre los participantes');
    });

    $('#users_speak').on('click', function(){
    	$('#plot_img').show()
    	$('#graph').hide()
    	$('#users-footer').hide()
        $('#plot_img').attr('src','../media/plot/users_speak.png');
        $('.panel-heading').text('Intervenciones de los participante');
    });

    $('#users_total_time').on('click', function(){
    	$('#plot_img').hide()
    	$('#graph').show()
		$('#users-footer').hide()    
    	morris.setData(data.usersTime)
    	$('.panel-heading').text('Tiempo total de habla por participante');
    	console.log(data)
    });

    $('#users_interv_time').on('click', function(){
    	$('#plot_img').hide()
    	$('#graph').show()
    	$('#users-footer').show()
    	$('.panel-heading').text('Duración intervenciones');
    	morris.setData(data.usersIntDur[0])
    });
    $('#user1').on('click', function(){
    	morris.setData(data.usersIntDur[0])
    });
    $('#user2').on('click', function(){
    	morris.setData(data.usersIntDur[1])
    });
    $('#user3').on('click', function(){
    	morris.setData(data.usersIntDur[2])
    });
    $('#user4').on('click', function(){
    	morris.setData(data.usersIntDur[3])
    });
}