setInterval(function(){
    $.get('/api/notif/profile/',function(data) {
        document.getElementById("notifoamprofile").innerHTML = data.value;
    });
}, 5000);