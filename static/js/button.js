$(document).ready(function() {
	$('.btn').click(function() {
		$('.btn').removeClass('clicked')
    	$(this).toggleClass('clicked');

	});
});