document.getElementById('login-btn').addEventListener('click', function() {
    // Redirect to login.html when the login button is clicked
    window.location.href = "login.html"; 
});

document.getElementById('sign-up-btn').addEventListener('click', function() {
    window.location.href="signuppage.html"
    // Implement actual sign-up functionality here
});

// When login or sign-up is successful, show the chat container
function showChat() {
    document.querySelector('.auth-container').style.display = 'none';
    document.querySelector('.chat-container').style.display = 'flex';
}
// Predefined credentials for testing purposes
// Function to logout