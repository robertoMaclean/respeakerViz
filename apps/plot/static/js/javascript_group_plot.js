$( document ).ready(function() {
    click_buttons()
    $('#users_interv_buble').click()
    //console.log(data)
    //transform_users_time()
    //$('#users_interaction').click()
});

function active_nav_li(){
    var pathname = window.location.pathname;
    $('.nav > li > a[href="'+pathname+'"]').parent().addClass('active');
}

function click_buttons() {
	$('#users_interv_buble').on('click', function(){
		console.log(data);
        console.log(user)
		$.ajax({
            type: "GET",
            url: '/plot/group_plots/'+user+'/flare.json',
            success: function(data) {
                html = '<svg width="960" height="960"></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Agrupación de intervenciones por grupo y usuario')
                $('.panel-footer').html('')
                buble('group_plots/')
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });    
	});

	$('#group_interv_dur').on('click', function(){
		console.log(data);
		$.ajax({
            type: "GET",
            url: '/plot/group_plots/'+user+'/intdur.json',
            success: function(data) {
                footer =  '<div class="btn-group">'   
                footer += '<button type="button" id="users" class="btn btn-default">Usuarios</button>'
                footer += '<button type="button" id="group" class="btn btn-default">Grupo</button>'
                footer += '</div>'
                $('.panel-heading').html('Duración intervenciones')
                $('.panel-footer').html(footer)
                interv_dur_click()
                $('#users').click()
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });    
	});
	
    $('#group_interv').on('click', function(){
        console.log(data);
        $.ajax({
            type: "GET",
            url: '/plot/group_plots/'+user+'/interv.json',
            success: function(data) {
                footer =  '<div class="btn-group">'   
                footer += '<button type="button" id="users" class="btn btn-default">Usuarios</button>'
                footer += '<button type="button" id="group" class="btn btn-default">Grupo</button>'
                footer += '</div>'
                $('.panel-heading').html('Duración intervenciones')
                $('.panel-footer').html(footer)
                interv_click()
                $('#users').click()
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });    
    });

    $('#group_speak').on('click', function(){
        console.log(data);
        $.ajax({
            type: "GET",
            url: '/plot/group_plots/'+user+'/interv.json',
            success: function(data) {
                footer =  '<div class="btn-group">'   
                footer += '<button type="button" id="users" class="btn btn-default">Usuarios</button>'
                footer += '<button type="button" id="group" class="btn btn-default">Grupo</button>'
                footer += '</div>'
                $('.panel-heading').html('Duración habla')
                $('.panel-footer').html(footer)
                speak_click()
                $('#users').click()
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });    
    });

	$('#group_volume').on('click', function(){
		console.log(data);
		$.ajax({
            type: "GET",
            url: '/plot/group_plots/'+user+'/volume.json',
            success: function(data) {
                footer =  '<div class="btn-group">'   
                footer += '<button type="button" id="users" class="btn btn-default">Usuarios</button>'
                footer += '<button type="button" id="group" class="btn btn-default">Grupo</button>'
                footer += '</div>'
                $('.panel-heading').html('Intensidad de voz')
                $('.panel-footer').html(footer)
                volume_click()
                $('#users').click()
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });    
	});

    $('#summary').on('click', function(){
        console.log(data);
        $.ajax({
            type: "GET",
            url: '/plot/group_plots/'+user+'/summary.json',
            success: function(data) {
                html = '<svg width="960" height="8000"></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Resumen')
                $('.panel-footer').html('')
                path = 'group_plots/'+user+'/summary.json'
                treeCollapsible(path)       
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });    
    });
}

function interv_dur_click() {
    $('#users').on('click', function(){
        html = '<svg width="960" height="600"></svg>'
        $('.panel-body').html(html)
        path = 'group_plots/'+user+'/intdur.json'
        treemap(path)
        //nodesGroup(path)
    });

    $('#group').on('click', function(){
        html = '<div id="graph" class="graph"></div>'
        $('.panel-body').html(html)
        barGraph(data.groupsIntervTime, ['#c9302c'], ['Segundos'])
        morris.options.xLabelAngle = 45
        morris.setData(data.groupsIntervTime)
    });
}

function interv_click() {
    $('#users').on('click', function(){
        html = '<svg width="960" height="600"></svg>'
        $('.panel-body').html(html)
        path = 'group_plots/'+user+'/interv.json'
        treemap(path)
    });

    $('#group').on('click', function(){
        html = '<div id="graph" class="graph"></div>'
        $('.panel-body').html(html)
        barGraph(data.groupsInterv, ['#c9302c'], ['Intervenciones'])
        morris.options.xLabelAngle = 45
        morris.setData(data.groupsInterv)
    });
}

function volume_click() {
    $('#users').on('click', function(){
        html = '<svg width="960" height="600"></svg>'
        $('.panel-body').html(html)
        path = 'group_plots/'+user+'/volume.json'
        treemap(path)
    });

    $('#group').on('click', function(){
        html = '<div id="graph" class="graph"></div>'
        $('.panel-body').html(html)
        barGraph(data.groupsVolume, ['#c9302c'], ['Segundos'])
        morris.options.xLabelAngle = 45
        morris.setData(data.groupsVolume)
    });
}

function speak_click() {
    $('#users').on('click', function(){
        html = '<svg width="960" height="600"></svg>'
        $('.panel-body').html(html)
        path = 'group_plots/'+user+'/speak.json'
        treemap(path)
    });

    $('#group').on('click', function(){
        html = '<div id="graph" class="graph"></div>'
        $('.panel-body').html(html)
        barGraph(data.groupsSpeakTime, ['#c9302c'], ['Duración'])
        morris.options.xLabelAngle = 45
        morris.setData(data.groupsSpeakTime)
    });
}
