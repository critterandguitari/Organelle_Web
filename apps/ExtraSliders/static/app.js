
var appBaseURL = '/sliders/'
var controlurl = appBaseURL + '/control'

var button = new Nexus.Button('#button')


//var sliders = new Nexus.Multislider('#sliders')
var sliders = new Nexus.Multislider('#sliders',{
 'size': [1000,200],
 'numberOfSliders': 100,
 'min': 0,
 'max': 1,
 'step': 0,
})

sliders.on('change',function(v) {
    console.log(v);
    //$.ajaxSetup({async: false});
    $.get(controlurl, v)
    .done(function () {
        console.log('sent data');
    })
    .fail(function () {
        console.log('problem');
    });
    //$.ajaxSetup({async: true});
})
