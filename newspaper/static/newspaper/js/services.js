$(function(){
	setTimeout(updateDateTime, 1000);
});

function updateDateTime(){
	url = "/newspaper/services/datetime/";
	$.get(url, function(data){
		$("#date").html(data);
		setTimeout(updateDateTime, 1000);
	});
}