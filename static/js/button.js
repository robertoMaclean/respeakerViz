$(document).ready(function() {
	$('.lateral').click(function() {
		$('.lateral').removeClass('clicked')
    	$(this).toggleClass('clicked');

	});
});