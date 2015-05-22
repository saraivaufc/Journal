$('#openBtn').click(function(){
	$('#myModal').modal({show:true})
});

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

var searchValues = [];
$(function(){
	$.get("/newspaper/services/sections/all/", function(data){
		var sections = (JSON.parse(data).sections);
		
		for(var i=0 ; i< sections.length; i++){
			searchValues.push(sections[i]);
		}
	});
	$.get("/newspaper/services/subsections/all/", function(data){
		var subsections = (JSON.parse(data)).subsections;
		for(var i=0 ; i< subsections.length; i++){
			searchValues.push(subsections[i]);
		}
	});
});

$("#search").autocomplete({
	source: searchValues
});

$(function(){
	$("#search").keyup(function(){
		var text = $("#search").val();
		if(text.length > 0){
			$("#searchclear").removeClass("hidden");
		}else{
			$("#searchclear").addClass("hidden");
		}
	});

	$("#searchclear").click(function(){
		$("#search").val('');
		$("#searchclear").addClass("hidden");
	});
});

