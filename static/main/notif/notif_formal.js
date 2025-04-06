setInterval(function(){
    $.get('/api/notif/formal/',function(data) {
        document.getElementById("notifformal").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)