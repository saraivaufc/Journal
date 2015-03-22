$('#openBtn').click(function(){
	$('#myModal').modal({show:true})
});

function validaSignIn(){
	try{
		var password = $("#formLogin #password");
		var hash = Sha256.hash(password.text());	
		password.val(hash);
	}catch(e){
		console.log(e);
		return false;
	}
	return true;
}

function validaSignUp(){
	var password = $("#formRegister #password");
	var password2 = $("#formRegister #password2");
	if(password.val() != password2.val()){
		alert("Senha não Conferem!!!!");
		return false;
	}
	try{
		var hash = Sha256.hash(password.text());	
		password.val(hash);
	}catch(e){
		console.log(e);
		return false;
	}
	return true;
}


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

$("[type=file]").on("change", function(){
	// Name of file and placeholder
	var file = this.files[0].name;
	var dflt = $(this).attr("placeholder");
	if($(this).val()!=""){
		$(this).next().text(file);
	} else {
		$(this).next().text(dflt);
	}
});