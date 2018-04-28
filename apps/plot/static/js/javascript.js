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
                html = data.html + '<div id="donut" class="graph"></div>'
            	$('.panel-body').html(html)
            	$('.panel-heading').html('Tiempo total de habla por participante')
            	$('.panel-footer').html('')
    			var json = JSON.parse(data.data)
    			console.log(json)
    			barGraphMultiColor(json.usersTime)
                donutGraph(json.usersSpeakTimePercent)
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    $('#users_interv_time').on('click', function(){ 
        footer ='<div class="btn-group">'	
    	footer += '<button type="button" id="user1" class="btn btn-danger active">Usuario 1</button>'
    	footer += '<button type="button" id="user2" class="btn btn-primary active">Usuario 2</button>'
    	footer += '<button type="button" id="user3" class="btn btn-success active">Usuario 3</button>'
    	footer += '<button type="button" id="user4" class="btn btn-warning active">Usuario 4</button>'
        footer += '<button type="button" id="total" class="btn btn-default active">Total</button>'
        footer += '</div>'
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
    			barGraph(json.usersIntDur[0], "#c9302c")
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
    });

    /*$('#users_time_percent').on('click', function(){
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
        
    });*/

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
        footer ='<div class="btn-group">'
        footer += '<button type="submit" id="user1" class="btn btn-danger">Usuario 1</button>'
        footer += '<button type="submit" id="user2" class="btn btn-primary">Usuario 2</button>'
        footer += '<button type="submit" id="user3" class="btn btn-success">Usuario 3</button>'
        footer += '<button type="submit" id="user4" class="btn btn-warning">Usuario 4</button>'
        footer += '<button type="submit" id="total" class="btn btn-defaul">Total</button>'
        footer += '</div>' 
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
                barGraph(json.usersVol[0], "#c9302c")
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

    $('#sec_intertv').on('click', function(data){      
        $.ajax({
            type: "GET",
            url: '/plot/relations',
            success: function(data) {
                html = '<svg></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Duración intervenciones')
                $('.panel-footer').html('')
                var json = JSON.parse(data)
                relations()
                console.log(json)
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
        
    });

    function click_buttons_interv_time(){
        func = function (row, series, type) {
                    /*console.log("--> "+row.label, series, type);*/
                    if(row.label == "Usuario 1") return "#c9302c";
                    else if(row.label == "Usuario 2") return "#337ab7";
                    else if(row.label == "Usuario 3") return "#5cb85c";
                    else if(row.label == "Usuario 4") return "#f0ad4e";
                }
    	$('#user1').on('click', function(){
           morris.options.barColors = ["#c9302c"]
    	   morris.setData(data.usersIntDur[0])
	    });
	    $('#user2').on('click', function(){
            morris.options.barColors = ["#337ab7"]
	    	morris.setData(data.usersIntDur[1])
            
	    });
	    $('#user3').on('click', function(){
            morris.options.barColors = ["#5cb85c"]
	    	morris.setData(data.usersIntDur[2])
	    });
	    $('#user4').on('click', function(){
            morris.options.barColors = ["#f0ad4e"]
            morris.setData(data.usersIntDur[3])
	    });
        $('#total').on('click', function(){
            morris.options.barColors = func
            dat ={
                "datos": [
                    {"x":"Usuario 1","y":data.usersIntDur[0].length},
                    {"x":"Usuario 2","y":data.usersIntDur[1].length},
                    {"x":"Usuario 3","y":data.usersIntDur[2].length},
                    {"x":"Usuario 4","y":data.usersIntDur[3].length}
                ]
            } 
            morris.setData(dat.datos)
        });
    }

        function click_buttons_users_vol(){
        $('#user1').on('click', function(){
           morris.options.barColors = ["#c9302c"]
           morris.setData(data.usersVol[0])
        });
        $('#user2').on('click', function(){
            morris.options.barColors = ["#337ab7"]
            morris.setData(data.usersVol[1])
        });
        $('#user3').on('click', function(){
            morris.options.barColors = ["#5cb85c"]
            morris.setData(data.usersVol[2])
        });
        $('#user4').on('click', function(){
            morris.options.barColors = ["#f0ad4e"]
            morris.setData(data.usersVol[3])
        });
    }
}

    