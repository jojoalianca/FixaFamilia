setInterval(function(){
    $.get('/api/notif/conf/',function(data) {
        document.getElementById("notifconf").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)