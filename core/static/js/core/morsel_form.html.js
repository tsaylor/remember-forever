$(document).ready(function(){
    var previewPaneId = "previewPane";
    var inputId = "id_content";
    var converter = new Showdown.converter();

    $("#" + inputId).keyup(function(){
        $("#" + previewPaneId).html(converter.makeHtml($(this).val()));
    });
    
});