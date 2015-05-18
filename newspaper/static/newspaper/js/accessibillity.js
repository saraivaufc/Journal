$(function(){
	if(readCookie("contrast")){
		$("*").addClass("contrast");	
		$("a, h1, h2, h3").addClass("link_contrast");
		$(".btn").addClass("btn_contrast");
		var button_contrast = $("#button-contrast");
		button_contrast.removeClass("disable-contrast");
		button_contrast.addClass("enable-contrast");
		button_contrast.text("Desativar Auto contraste[2]");
	}
	if(readCookie("font")){
		font_plus();
		var button_font = $("#button-font");
		button_font.removeClass("font-minus");
		button_font.addClass("font-plus");
		button_font.text("Diminuir a Letra[3]");
	}
});

$("#button-contrast").click(function(){
	var csrf = $("input[name='csrfmiddlewaretoken']").val();
	$("*").toggleClass("contrast");
	$("a, h1, h2, h3").toggleClass("link_contrast");
	$(".btn").toggleClass("btn_contrast");
	if($(this).hasClass("disable-contrast")){
		$(this).removeClass("disable-contrast");
		$(this).addClass("enable-contrast");
		$(this).text("Desativar Auto contraste[2]");
		generateCookie("contrast", true , 7);
	}else if($(this).hasClass("enable-contrast")){
		$(this).removeClass("enable-contrast");
		$(this).addClass("disable-contrast");
		$(this).text("Ativar Auto contraste[2]");
		eraseCookie("contrast");
	}
});

$("#button-font").click(function(){
	if($(this).hasClass("font-plus")){
		font_minus();
		$(this).removeClass("font-plus");
		$(this).addClass("font-minus");
		$(this).text("Aumentar a Letra[3]");
		eraseCookie("font");
	}else if ($(this).hasClass("font-minus")) {
		font_plus();
		$(this).removeClass("font-minus");
		$(this).addClass("font-plus");
		$(this).text("Diminuir a Letra[3]");
		generateCookie("font", true , 7);
	};
});

function font_plus(){
	$("p").css({"font-size": "140%" });
	$("a").css({"font-size": "130%" });
}

function font_minus(){
	$("p").css({"font-size": "100%" });
	$("a").css({"font-size": "100%" });
}