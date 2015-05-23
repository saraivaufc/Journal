$(function(){
	$('#jqxTree').jqxTree({  height: '100%', width: '100%' });
	$('#mainSplitter').jqxSplitter({
        width: '100%', 
        height: 500, 
        panels: [{ size: 500 }] 
    });
});

$("#id_subsection").jqxDropDownList({filterable:true});