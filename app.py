
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

GEMINI_API_KEY = 'your_gemini_api_key_here'
GEMINI_API_URL = 'https://api.gemini.com/v1/chat'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Send user message to Gemini API
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"message": user_message}
    
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    response_json = response.json()
    
    bot_reply = response_json.get("response", "I'm sorry, I didn't get that.")
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
