$('#openBtn').click(function(){
	$('#myModal').modal({show:true})
});

// function validaSignIn(){
// 	try{
// 		var password = $("#inputpassword");
// 		var hash = CryptoJS.SHA256( password.text() );	
// 		password.val(hash);
// 	}catch(e){
// 		console.log(e);
// 		return false;
// 	}
// 	return true;
// }

function removeNews(id){
	if(window.confirm("Want to remove the news?")){
		
	}
}

$(function(){
	var alert_success = $("#alert-success");
	var alert_danger = $("#alert-danger");
	var alert_warning = $("#alert-warning");
	var alert_info = $("#alert-info");

	if(alert_success.length) {
		$().toastmessage('showSuccessToast', alert_success.val());	
	};
	if(alert_danger.length) {
		$().toastmessage('showErrorToast', alert_danger.val());
	};
	if (alert_warning.length) {
		$().toastmessage('showWarningToast', alert_warning.val());	
	};

	if(alert_info.length) {
		$().toastmessage('showNoticeToast', alert_info.val());
	}	
	
});