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