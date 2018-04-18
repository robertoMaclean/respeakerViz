$( document ).ready(function() {
    hideGraphs()
	$('#users-footer').hide()    
    click_buttons()
});

function click_buttons(){
	$('#users_interaction').on('click', function(){
		$('#plot_img').show()
        hideGraphs()
        $('#plot_img').attr('src','../media/plot/users_interaction.png');
        $('.panel-heading').text('Interacción entre los participantes');
    });

    $('#users_speak').on('click', function(){
    	$('#plot_img').show()
        hideGraphs()
    	$('#users-footer').hide()
        $('#plot_img').attr('src','../media/plot/users_speak.png');
        $('.panel-heading').text('Intervenciones de los participante');
    });

    $('#users_total_time').on('click', function(){
    	$('#plot_img').hide()
    	$('#graph').show()
        $('#donut').hide()
        $('#line').hide()
		$('#users-footer').hide()    
    	morris.setData(data.usersTime)
    	$('.panel-heading').text('Tiempo total de habla por participante');
    	console.log(data)
    });

    $('#users_interv_time').on('click', function(){
    	$('#plot_img').hide()
        $('#donut').hide()
    	$('#graph').show()
        $('#line').hide()
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

    $('#users_time_percent').on('click', function(){
        $('#plot_img').hide()
        $('#donut').show()
        $('#graph').hide()
        $('#line').hide()
        $('#users-footer').hide()
        $('.panel-heading').text('Porcentaje de habla por usuario');
        morrisDonut.setData(data.usersSpeakTimePercent)
    });

    $('#users_int_in_time').on('click', function(){
        $('#plot_img').hide()
        $('#donut').hide()
        $('#graph').hide()
        $('#line').show()
        $('#users-footer').hide()
        $('.panel-heading').text('Porcentaje de habla por usuario');
        morrisLine.setData(data.userIntInTime)
    });
}

function hideGraphs(){
    $('#graph').hide()
    $('#donut').hide()
    $('#line').hide()
}
    