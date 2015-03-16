$(function(){
	$("input[name='msg']").each(function(){
		var msg = $(this).attr("value");
		Notification.requestPermission(function(perm){
			if( perm == "granted"){
				var not = new Notification("Msg", {body: msg});
			}else{
				alert(msg);	
			}
		});
	});
});