$(document).ready( function(){
	$("#logo").delay(200).fadeTo(1800, 1);

	$("#title").delay(1200).fadeTo(1000, 1);

	$(".github-button").delay(2600).fadeTo(1800, 1);

	$(".paragraph").delay(2600).fadeTo(1800, 1);

	$(".b_seemore").delay(3000).fadeTo(1800, 1);

})

function show_more() {
	$(".media").fadeTo(700, 1);

	$('html, body').animate({
        scrollTop: $(".media").offset().top
    }, 2000);
}
