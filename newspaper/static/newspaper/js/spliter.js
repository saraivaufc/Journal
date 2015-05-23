$(function(){
	$('#jqxTree').jqxTree({  height: '100%', width: '100%' });
	$('#mainSplitter').jqxSplitter({
        width: '100%', 
        height: 800, 
        panels: [{ size: 200 }] 
    });
});
