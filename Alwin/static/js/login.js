// Predefined credentials for testing purposes
const correctUsername = "user123";
const correctPassword = "123";

// Get the form and input elements
const loginForm = document.getElementById("login-form");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");

// Get the login and chat containers
const loginContainer = document.getElementById("login-container");
const chatContainer = document.getElementById("chat-container");

// Handle form submission
loginForm.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the username and password input values
    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    // Check if the username and password match the predefined values
    if (username === correctUsername && password === correctPassword) {
        alert("Login successful!");
        showChat();  // Call showChat to switch to the chat interface
    } else {
        alert("Incorrect username or password. Please try again.");
    }
});

// Function to show the chat interface after login
function showChat() {
    // Hide the login container and show the chat container
    loginContainer.style.display = "none";
    chatContainer.style.display = "flex";
}
function logout() {
    // Clear the user data stored in localStorage (if using localStorage for login state)
    
    // Redirect the user to the login page (or home page)
    window.location.href = "index.html"; // Replace with your login page URL
}

// Add event listener to the logout button
document.getElementById("logout").addEventListener("click", logout);