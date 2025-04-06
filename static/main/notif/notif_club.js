setInterval(function(){
    $.get('/api/notif/club/',function(data) {
        document.getElementById("notifclub").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)