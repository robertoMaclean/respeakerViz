$( document ).ready(function() {
    click_buttons()
});

function click_buttons(){
	$('#users_interaction').on('click', function(){
        $.ajax({
            type: "GET",
            url: '/plot/interactions',
            success: function(data) {
            	$('.panel-body').html(data)
            	$('.panel-heading').html('Interacción entre participantes')
            	$('.panel-footer').html('')
            	console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    $('#users_speak').on('click', function(){
        $.ajax({
            type: "GET",
            url: '/plot/interv',
            success: function(data) {
            	$('.panel-body').html(data)
            	$('.panel-heading').html('Intervenciones en el tiempo')
            	$('.panel-footer').html('')
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    $('#users_total_time').on('click', function(){
    	$.ajax({
            type: "GET",
            url: '/plot/barGraph',
            success: function(data) {
            	console.log(data.html)
            	$('.panel-body').html(data.html)
            	$('.panel-heading').html('Tiempo total de habla por participante')
            	$('.panel-footer').html('')
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
    	footer = '<button type="submit" id="user1" class="btn btn-danger">Usuario 1</button>'
    	footer += '<button type="submit" id="user2" class="btn btn-primary">Usuario 2</button>'
    	footer += '<button type="submit" id="user3" class="btn btn-success">Usuario 3</button>'
    	footer += '<button type="submit" id="user4" class="btn btn-warning">Usuario 4</button>'

    	$.ajax({
            type: "GET",
            url: '/plot/barGraph',
            success: function(data) {
            	//$('.panel-body').load(data)
            	$('.panel-body').html(data.html)
            	$('.panel-heading').html('Duración intervenciones')
            	$('.panel-footer').html(footer)
            	var json = JSON.parse(data.data)
            	click_buttons_interv_time()
    			console.log(json)
    			barGraph(json.usersIntDur[0])
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    $('#users_time_percent').on('click', function(){
        $.ajax({
            type: "GET",
            url: '/plot/donutGraph',
            success: function(data) {
            	//$('.panel-body').load(data)
            	$('.panel-body').html(data.html)
            	$('.panel-heading').html('Porcentaje tiempo de habla por participante')
            	$('.panel-footer').html('')
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
        $.ajax({
            type: "GET",
            url: '/plot/lineGraph',
            success: function(data) {
            	$('.panel-body').html(data.html)
            	$('.panel-heading').html('Intervenciones a traves del tiempo')
            	$('.panel-footer').html('')
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

    $('#users_vol').on('click', function(){
        footer = '<button type="submit" id="user1" class="btn btn-danger">Usuario 1</button>'
        footer += '<button type="submit" id="user2" class="btn btn-primary">Usuario 2</button>'
        footer += '<button type="submit" id="user3" class="btn btn-success">Usuario 3</button>'
        footer += '<button type="submit" id="user4" class="btn btn-warning">Usuario 4</button>'
        $.ajax({
            type: "GET",
            url: '/plot/barGraph',
            success: function(data) {
                $('.panel-body').html(data.html)
                $('.panel-heading').html('Volumen de la voz de los participante')
                $('.panel-footer').html(footer)
                var json = JSON.parse(data.data)
                console.log(json)
                click_buttons_users_vol()
                barGraph(json.usersVol[0])
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    $('#users_interv_buble').on('click', function(data){      
        $.ajax({
            type: "GET",
            url: '/plot/flare.json',
            success: function(data) {
                html = '<svg width="960" height="960"></svg>'
                console.log(data)
                $('.panel-body').html(html)
                $('.panel-heading').html('Duración intervenciones')
                $('.panel-footer').html('')
                var json = JSON.parse(data)
                buble()
                console.log(json)
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
        
    });

    function click_buttons_interv_time(){
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

        function click_buttons_users_vol(){
        $('#user1').on('click', function(){
           morris.setData(data.usersVol[0])
        });
        $('#user2').on('click', function(){
            morris.setData(data.usersVol[1])
        });
        $('#user3').on('click', function(){
            morris.setData(data.usersVol[2])
        });
        $('#user4').on('click', function(){
            morris.setData(data.usersVol[3])
        });
    }
}

    