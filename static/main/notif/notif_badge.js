setInterval(function(){
    $.get('/api/notif/badge/',function(data) {
        document.getElementById("notifbadge").innerHTML = data.value;
    });
}, 3000);
console.log(data.value)