const chatBody = document.getElementById("chat-body");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

// Cognitive Biases Data
const cognitiveBiases = {
    "confirmation bias": "You tend to favor information that confirms your existing beliefs.",
    "availability heuristic": "You rely on immediate examples that come to mind when evaluating a topic.",
    "anchoring bias": "You rely too heavily on the first piece of information offered.",
    "halo effect": "Your overall impression of a person influences your feelings about their specific traits.",
    "self-serving bias": "You attribute success to yourself and failures to external factors."
};

// Add a message to the chat
function addMessage(sender, text) {
    const message = document.createElement("div");
    message.classList.add("chat-message", sender);
    message.textContent = text;
    chatBody.appendChild(message);
    chatBody.scrollTop = chatBody.scrollHeight; // Scroll to the bottom
}

// Handle user input and bot response
function handleUserInput() {
    const userText = userInput.value.trim().toLowerCase();
    if (userText === "") return;

    // Add user message
    addMessage("user", userInput.value);
    userInput.value = "";

    // Add bot response
    let botResponse = cognitiveBiases[userText] || "I'm not familiar with that. Ask about another bias!";
    addMessage("bot", botResponse);
}

// Event Listeners
sendBtn.addEventListener("click", handleUserInput);
userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") handleUserInput();
});