$( document ).ready(function() {
	$('#users-footer').hide()    
    click_buttons()
});

function click_buttons(){
	$('#users_interaction').on('click', function(){
        $('#users-footer').hide() 
        $.ajax({
            type: "GET",
            url: '/plot/interactions',
            success: function(data) {
            	$('.panel-body').html(data)
            	$('.panel-heading').html('Interacción entre participantes')
            	console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    $('#users_speak').on('click', function(){
        $('#users-footer').hide() 
        $.ajax({
            type: "GET",
            url: '/plot/interv',
            success: function(data) {
            	//$('.panel-body').load(data)
            	$('.panel-body').html(data)
            	$('.panel-heading').html('Intervenciones en el tiempo')
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    $('#users_total_time').on('click', function(){
		$('#users-footer').hide() 
    	$.ajax({
            type: "GET",
            url: '/plot/barGraph',
            success: function(data) {
            	console.log(data.html)
            	$('.panel-body').html(data.html)
            	$('.panel-heading').html('Tiempo total de habla por participante')
    			//morris.setData(data.usersTime)
    			var json = JSON.parse(data.data)
    			console.log(json)
    			barGraph(json.usersTime)
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    $('#users_interv_time').on('click', function(){
    	$.ajax({
            type: "GET",
            url: '/plot/barGraph',
            success: function(data) {
            	//$('.panel-body').load(data)
            	$('.panel-body').html(data.html)
            	$('.panel-heading').html('Duración intervenciones')
            	$('#users-footer').show()
            	var json = JSON.parse(data.data)
    			console.log(json)
    			barGraph(json.usersIntDur[0])
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
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
        $('#users-footer').hide() 
        $.ajax({
            type: "GET",
            url: '/plot/donutGraph',
            success: function(data) {
            	//$('.panel-body').load(data)
            	$('.panel-body').html(data.html)
            	$('.panel-heading').html('Porcentaje tiempo de habla por participante')
            	var json = JSON.parse(data.data)
    			console.log(json)
    			donutGraph(json.usersSpeakTimePercent)
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
        
    });

    $('#users_int_in_time').on('click', function(){
    	$('#users-footer').hide() 
        $.ajax({
            type: "GET",
            url: '/plot/lineGraph',
            success: function(data) {
            	//$('.panel-body').load(data)
            	$('.panel-body').html(data.html)
            	$('.panel-heading').html('Intervenciones a traves del tiempo')
                var json = JSON.parse(data.data)
    			console.log(json)
    			lineGraph(json.userIntInTime)
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });
}

    