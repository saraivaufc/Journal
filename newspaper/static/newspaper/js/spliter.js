$(function(){
	$('#mainSplitter').jqxSplitter({
        width: '100%', 
        height: 1000, 
        panels: [{ size: 300 }] 
    });
    $('#jqxTree').jqxTree({  height: '100%', width: '100%' });
});