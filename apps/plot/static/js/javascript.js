$( document ).ready(function() {
    click_buttons()
    active_nav_li()
    transform_users_time()
});

function active_nav_li(){
    var pathname = window.location.pathname;
    $('.nav > li > a[href="'+pathname+'"]').parent().addClass('active');
}

function transform_users_time(){
    max = Math.max(data.usersTime[0]['y'], data.usersTime[1]['y'], data.usersTime[2]['y'], data.usersTime[3]['y'])
    users_time = [data.usersTime[0]['y']/max, data.usersTime[1]['y']/max, data.usersTime[2]['y']/max, data.usersTime[3]['y']/max]
}
function click_buttons(){
	$('#users_interaction').on('click', function(){
        $.ajax({
            type: "GET",
            url: '/plot/interactions',
            success: function(data) {
                footer = '<div>'
                footer += '<a type="link" id="download_csv" href="/media/plot/relaciones.csv" class="btn btn-primary">Descargar datos</a>'
            	footer += '</div>'
                $('.panel-body').html(data)
            	$('.panel-heading').html('Interacción entre participantes')
            	$('.panel-footer').html(footer)
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
        html = '<div id="graph" class="graph"></div>'
        html += '<div id="donut" class="graph"></div>'
        $('.panel-body').html(html)
        $('.panel-heading').html('Tiempo total de habla por participante')
        $('.panel-footer').html('')
        /*var json = JSON.parse(data.data)*/
        /*console.log(json)*/
        console.log(data)
        barGraphMultiColor(data.usersTime, ['Segundos'])
        donutGraph(data.usersSpeakTimePercent)
        console.log('success')
    });

    $('#users_interv_time').on('click', function(){ 
        footer ='<div class="btn-group">'	
    	footer += '<button type="button" id="general" class="btn">General</button>'
        footer += '<button type="button" id="user1" class="btn btn-danger">Usuario 1</button>'
    	footer += '<button type="button" id="user2" class="btn btn-primary">Usuario 2</button>'
    	footer += '<button type="button" id="user3" class="btn btn-success">Usuario 3</button>'
    	footer += '<button type="button" id="user4" class="btn btn-warning">Usuario 4</button>'
        footer += '<button type="button" id="total" class="btn btn-default">Total</button>'
        footer += '</div>'
        html = '<div id="graph" class="graph"></div>' 
        $('.panel-body').html(html)
        $('.panel-heading').html('Duración intervenciones')
        $('.panel-footer').html(footer)
        click_buttons_interv_time()
        barGraph(data.usersIntDur[0], '#c9302c', ['Segundos'])
        $("#general").click()
        console.log('success')
    	/*$.ajax({
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
    			barGraph(json.usersIntDur[0], '#c9302c', ['Segundos'])
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });*/
    });

    $('#users_int_in_time').on('click', function(){
        html = '<div id="line" class="graph"></div>'
        $('.panel-body').html(html)
        $('.panel-heading').html('Intervenciones a traves del tiempo')
        $('.panel-footer').html('')
        lineGraph(data.userIntInTime)
        console.log('success')
        /*$.ajax({
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
        });*/
    });

    $('#users_vol').on('click', function(){
        footer ='<div class="btn-group">'
        footer += '<button type="button" id="vol_in_time" class="btn">General</button>'
        footer += '<button type="button" id="user1" class="btn btn-danger">Usuario 1</button>'
        footer += '<button type="button" id="user2" class="btn btn-primary">Usuario 2</button>'
        footer += '<button type="button" id="user3" class="btn btn-success">Usuario 3</button>'
        footer += '<button type="button" id="user4" class="btn btn-warning">Usuario 4</button>'
        footer += '<button type="button" id="total" class="btn btn-defaul">Total</button>'
        footer += '</div>' 
        html = '<div id="graph" class="graph"></div>'
        $('.panel-body').html(html)
        $('.panel-heading').html('Volumen de la voz de los participante')
        $('.panel-footer').html(footer)
        /*var json = JSON.parse(data.data)
        console.log(json)*/
        click_buttons_users_vol()
        barGraph(data.usersVol[0], '#c9302c', ['Volumen'])
        $("#vol_in_time").click()
        console.log('success')
        /*$.ajax({
            type: "GET",
            url: '/plot/barGraph',
            success: function(data) {
                $('.panel-body').html(data.html)
                $('.panel-heading').html('Volumen de la voz de los participante')
                $('.panel-footer').html(footer)
                var json = JSON.parse(data.data)
                console.log(json)
                click_buttons_users_vol()
                barGraph(json.usersVol[0], '#c9302c', ['Volumen'])
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });*/
    });

    $('#users_interv_buble').on('click', function(data){      
        $.ajax({
            type: "GET",
            url: '/plot/'+user+'/flare.json',
            success: function(data) {
                html = '<svg width="960" height="960"></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Agrupación de intervenciones por usuario')
                $('.panel-footer').html('')
                buble()
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
            url: '/plot/'+user+'/relations',
            success: function(data) {
                html = '<svg></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Relación entre intervenciones')
                $('.panel-footer').html('')
                /*var json = JSON.parse(data)*/
                relations()
                /*console.log(json)*/
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
        
    });

    $('#test').on('click', function(data){      
        $.ajax({
            type: "GET",
            url: '/plot/force.csv',
            success: function(data) {
                html = '<svg></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Agrupación de intervenciones por usuario')
                $('.panel-footer').html('')
                nodes()
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });
        
    });

    
    function get_sum(array) {
        sum = 0
        for(var i=0;i<array.length;i++){
            sum = parseFloat(array[i].y)+sum
        }
        return sum.toFixed(2)
    } 

    function click_buttons_interv_time(){
        func_users = function (row, series, type) {
                    /*console.log("--> "+row.label, series, type);*/
                    if(row.label == "Usuario 1") return "#c9302c";
                    else if(row.label == "Usuario 2") return "#337ab7";
                    else if(row.label == "Usuario 3") return "#5cb85c";
                    else if(row.label == "Usuario 4") return "#f0ad4e";
                }
        func_times = function (row, series, type) {
                    /*console.log("--> "+row.label, series, type);*/
                    if((contador[0]<data.usersIntDur[0].length)&&row.label == String(data.usersIntDur[0][contador[0]]['x'])){
                        contador[0] += 1
                        return "#c9302c";
                    } 
                    else if((contador[1]<data.usersIntDur[1].length)&&row.label == String(data.usersIntDur[1][contador[1]]['x'])){
                        contador[1] += 1
                        return "#337ab7";
                    } 
                    else if((contador[2]<data.usersIntDur[2].length)&&row.label == String(data.usersIntDur[2][contador[2]]['x'])){
                        contador[2] += 1
                        return "#5cb85c";
                    } 
                    else if((contador[3]<data.usersIntDur[3].length)&&row.label == String(data.usersIntDur[3][contador[3]]['x'])){
                        contador[3] += 1
                        return "#f0ad4e";
                    } 
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
            morris.options.barColors = func_users
            dat ={
                "datos": [
                    {"x":"Usuario 1","y":get_sum(data.usersIntDur[0])},
                    {"x":"Usuario 2","y":get_sum(data.usersIntDur[1])},
                    {"x":"Usuario 3","y":get_sum(data.usersIntDur[2])},
                    {"x":"Usuario 4","y":get_sum(data.usersIntDur[3])}
                ]
            } 
            morris.setData(dat.datos)
        });
        $('#general').on('click', function(){
           morris.options.barColors = func_times
           var array_concat = data.usersIntDur[0].concat(data.usersIntDur[1], data.usersIntDur[2], data.usersIntDur[3])
           array_concat.sort(function(a, b){return a['x'] - b['x']});
           contador = [0,0,0,0]
           morris.setData(array_concat)
        });
    }

    function click_buttons_users_vol(){
        func_users = function (row, series, type) {
                    /*console.log("--> "+row.label, series, type);*/
                    if(row.label == "Usuario 1") return "#c9302c";
                    else if(row.label == "Usuario 2") return "#337ab7";
                    else if(row.label == "Usuario 3") return "#5cb85c";
                    else if(row.label == "Usuario 4") return "#f0ad4e";
                }
        var contador = [0,0,0,0]
        func_times = function (row, series, type) {
                    /*console.log("--> "+row.label, series, type);*/
                    if((contador[0]<data.usersVol[0].length)&&row.label == String(data.usersVol[0][contador[0]]['x'])){
                        contador[0] += 1
                        return "#c9302c";
                    } 
                    else if((contador[1]<data.usersVol[1].length)&&row.label == String(data.usersVol[1][contador[1]]['x'])){
                        contador[1] += 1
                        return "#337ab7";
                    } 
                    else if((contador[2]<data.usersVol[2].length)&&row.label == String(data.usersVol[2][contador[2]]['x'])){
                        contador[2] += 1
                        return "#5cb85c";
                    } 
                    else if((contador[3]<data.usersVol[3].length)&&row.label == String(data.usersVol[3][contador[3]]['x'])){
                        contador[3] += 1
                        return "#f0ad4e";
                    } 
                }
        $('#vol_in_time').on('click', function(){
           morris.options.barColors = func_times
           var array_concat = data.usersVol[0].concat(data.usersVol[1], data.usersVol[2], data.usersVol[3])
           array_concat.sort(function(a, b){return a['x'] - b['x']});
           contador = [0,0,0,0]
           morris.setData(array_concat)
        });
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
        $('#total').on('click', function(){
            morris.options.barColors = func_users
            morris.setData(data.usersVolAVG)
        });
    }

    function click_buttons_users_vol2(){
        var contador = [0,0,0,0]
        func = function (row, series, type) {
                    /*console.log("--> "+row.label, series, type);*/
                    if((contador[0]<data.usersVol[0].length)&&row.label == String(data.usersVol[0][contador[0]]['x'])){
                        contador[0] += 1
                        return "#c9302c";
                    } 
                    else if((contador[1]<data.usersVol[1].length)&&row.label == String(data.usersVol[1][contador[1]]['x'])){
                        contador[1] += 1
                        return "#337ab7";
                    } 
                    else if((contador[2]<data.usersVol[2].length)&&row.label == String(data.usersVol[2][contador[2]]['x'])){
                        contador[2] += 1
                        return "#5cb85c";
                    } 
                    else if((contador[3]<data.usersVol[3].length)&&row.label == String(data.usersVol[3][contador[3]]['x'])){
                        contador[3] += 1
                        return "#f0ad4e";
                    } 
                }
        $('#user1').on('click', function(){
           morris.options.barColors = func
           var array_concat = data.usersVol[0].concat(data.usersVol[1], data.usersVol[2], data.usersVol[3])
           array_concat.sort(function(a, b){return a['x'] - b['x']});
           contador = [0,0,0,0]
           morris.setData(array_concat)
        });
        $('#user2').on('click', function(){
            morris.options.barColors = ["#337ab7"]
            morris.setData(data.usersVol[0])
        });
        $('#user3').on('click', function(){
            morris.options.barColors = ["#5cb85c"]
            morris.setData(data.usersVol[2])
        });
        $('#user4').on('click', function(){
            morris.options.barColors = ["#f0ad4e"]
            morris.setData(data.usersVol[3])
        });
        $('#total').on('click', function(){
            morris.options.barColors = func
            /*console.log(data.usersVol[0][0]['x'])
            dat ={
                "datos": [
                    {"x":data.usersVol[0]['x'],"y":data.usersVol[0]['y']},
                    {"x":data.usersVol[1]['x'],"y":data.usersVol[1]['y']},
                    {"x":data.usersVol[2]['x'],"y":data.usersVol[2]['y']},
                    {"x":data.usersVol[3]['x'],"y":data.usersVol[3]['y']},
                ]
            } */
            morris.setData(data.usersVolAVG)
        });
    }

    function getSum(total, num) {
        return total + num;
    }

    
}

    