
var appBaseURL = '/robot-control'
var controlurl = appBaseURL + '/control'

$(function () {
    $("#control-fwd").click(function(){
        console.log('fwd')
        $.ajaxSetup({async: false});
        $.get(controlurl+'?operation=move', { 'dir' : 'fwd' })
        .done(function () {
            console.log('went fwd');
        })
        .fail(function () {
            console.log('problem');
        });
        $.ajaxSetup({async: true});
    });
    $("#control-right").click(function(){
        console.log('right')
    });
    $("#control-left").click(function(){
        console.log('left')
    });
    $("#control-rev").click(function(){
        console.log('rev')
    });
});
