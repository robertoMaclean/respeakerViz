$( document ).ready(function() {
    click_buttons()
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
		$.ajax({
            type: "GET",
            url: '/plot/group_plots/'+user+'/flare.json',
            success: function(data) {
                html = '<svg width="960" height="960"></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Agrupación de intervenciones por usuario')
                $('.panel-footer').html('')
                buble('group_plots/')
                //treemap()
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
                html = '<svg width="960" height="600"></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Duración intervenciones')
                $('.panel-footer').html('')
                //buble('group_plots/')
                path = 'group_plots/'+user+'/intdur.json'
                treemap(path)
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
                html = '<svg width="960" height="600"></svg>'
                $('.panel-body').html(html)
                $('.panel-heading').html('Agrupación de intervenciones por usuario')
                $('.panel-footer').html('')
                //buble('group_plots/')
                path = 'group_plots/'+user+'/volume.json'
                treemap(path)
                console.log('success')
            },
            error: function(data) {
                console.log('error')
            },
        });    
	});
}
