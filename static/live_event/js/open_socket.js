var socket = new WebSocket('ws://' + window.location.host + '/live/'+ $django_event_id);

socket.onmessage = function (e) {
    alert(e.data);
};

socket.onopen = function () {
    console.log('WebSockets connection created.');
    socket.send("New user connected to this event");
};

if (socket.readyState == WebSocket.OPEN) {
    socket.onopen();
}