let ws;

function connectWebSocket() {
    ws = new WebSocket(`ws://${location.host}/ws/chat`);

    ws.onmessage = function (event) {
        const chatbox = document.getElementById("chatbox");
        const response = document.createElement("p");
        response.innerHTML = `<strong>LLaMA3:</strong> ${event.data}`;
        chatbox.appendChild(response);
    };
}

function sendMessage(event) {
    event.preventDefault();
    const messageInput = document.getElementById("message");
    const message = messageInput.value;

    if (ws.readyState === WebSocket.OPEN) {
        const chatbox = document.getElementById("chatbox");
        const userMessage = document.createElement("p");
        userMessage.innerHTML = `<strong>You:</strong> ${message}`;
        chatbox.appendChild(userMessage);

        ws.send(message);
        messageInput.value = "";
    }
}

window.onload = connectWebSocket;
