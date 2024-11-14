
async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const userMessage = inputField.value;

    // Display user message in chat box
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
    inputField.value = "";

    // Send user message to the backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
}
