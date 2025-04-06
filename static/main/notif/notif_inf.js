setInterval(function(){
    $.get('/api/notif/inf/',function(data) {
        document.getElementById("notifinf").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)