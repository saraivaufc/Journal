$("#button-contrast").click(function(){
	$("*").toggleClass("contrast");
	$("a, h1, h2, h3").toggleClass("link_contrast");
	if($(this).hasClass("disable-contrast")){
		$(this).removeClass("disable-contrast");
		$(this).addClass("enable-contrast");
		$(this).text("Desativar Auto contraste[2]");	
	}else if($(this).hasClass("enable-contrast")){
		$(this).removeClass("enable-contrast");
		$(this).addClass("disable-contrast");
		$(this).text("Ativar Auto contraste[2]");
	}
});

$("#button-font").click(function(){
	if($(this).hasClass("font-plus")){
		font_minus();
		$(this).removeClass("font-plus");
		$(this).addClass("font-minus");
		$(this).text("Aumentar a Letra[3]");
	}else if ($(this).hasClass("font-minus")) {
		font_plus();
		$(this).removeClass("font-minus");
		$(this).addClass("font-plus");
		$(this).text("Diminuir a Letra[3]");
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
