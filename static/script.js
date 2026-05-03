async function sendMessage() {

    let message = document.getElementById("message").value;

    if(message.trim() === "") {
        return;
    }

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `
        <div class="user">
            <b>You:</b> ${message}
        </div>
    `;

    let response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: message
        })
    });

    let data = await response.json();

    chatBox.innerHTML += `
        <div class="bot">
            <b>Bot:</b> ${data.response}
        </div>
    `;

    document.getElementById("message").value = "";

    chatBox.scrollTop = chatBox.scrollHeight;
}
