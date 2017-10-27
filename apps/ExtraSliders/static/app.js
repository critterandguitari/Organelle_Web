
var appBaseURL = '/sliders/'
var controlurl = appBaseURL + '/control'

var sliders = new Nexus.Multislider('#sliders')
var button = new Nexus.Button('#button')

sliders.on('change',function(v) {
    console.log(v);
//    $.ajaxSetup({async: false});
    $.get(controlurl, v)
    .done(function () {
        console.log('sent data');
    })
    .fail(function () {
        console.log('problem');
    });
  //  $.ajaxSetup({async: true});
})
