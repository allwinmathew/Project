from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)

# Define responses for each cognitive bias
biases_responses = {
    "cognitive bias": "Cognitive bias is a systematic pattern of deviation from norm or rationality in judgment, whereby inferences may be illogical.",
    "halo effect": "The halo effect is a cognitive bias where the perception of one positive trait influences the overall perception of a person or thing.",
    "hindsight bias": "Hindsight bias is the tendency to see events as having been predictable after they have already occurred.",
    "anchoring bias": "Anchoring bias is a cognitive bias where individuals rely too heavily on the first piece of information they receive (the 'anchor') when making decisions.",
    "self-serving bias": "Self-serving bias is the habit of attributing positive events to one's own character but attributing negative events to external factors.",
    "illusion of control": "The illusion of control is the tendency for people to overestimate their ability to control events, even when they have no influence over them.",
    "confirmation bias": "Confirmation bias is the tendency to search for, interpret, or remember information in a way that confirms one's preconceptions, leading to statistical errors."
}

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            rating INTEGER NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == "correct_username" and password == "correct_password":
            return redirect(url_for('chat'))
        else:
            return render_template('login.html', error="Incorrect username or password.")
    
    return render_template('login.html') 

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '').lower()
    
    for bias in biases_responses:
        if bias in user_message:
            return jsonify({'response': biases_responses[bias]})
    
    return jsonify({'response': "I'm here to assist you with cognitive biases. Please ask about a specific bias!"})

# Route to handle feedback submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.get_json()

        # Validate input fields
        name = data.get('name')
        email = data.get('email')
        rating = data.get('rating')
        message = data.get('message')

        if not name or not email or not rating or not message:
            return jsonify({"error": "All fields are required!"}), 400

        # Connect to the database and insert feedback
        conn = sqlite3.connect('feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, email, rating, message) VALUES (?, ?, ?, ?)", (name, email, rating, message))
        conn.commit()
        conn.close()

        return jsonify({"message": "Feedback submitted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to handle contact form submission
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()

        # Extract and validate data
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({"error": "All fields are required!"}), 400

        # Store in SQLite database
        conn = sqlite3.connect('contact.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contact (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()

        return jsonify({"message": "Message submitted successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
if __name__ == '__main__':
    app.run(debug=True)
