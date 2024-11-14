# AI Chatbot Using Gemini API Key

This project is a simple chatbot deployed with HTML, CSS, JavaScript, Python (Flask), and the Gemini AI API. It allows users to interact with a chatbot interface via a webpage. User messages are processed by the Gemini API, which generates responses displayed on the web page.

## Project Structure

```
AI_Chatbot_Gemini/
├── app.py                  # Main Python file with Flask app and routes
├── templates/
│   └── index.html          # HTML file for the chatbot interface
├── static/
│   ├── style.css           # CSS for styling the chatbot interface
│   └── script.js           # JavaScript for handling user interactions and API calls
└── README.md               # Project documentation
```

## Requirements

- Python 3.x
- Flask
- requests

To install the required Python packages, you can run:
```bash
pip install flask requests
```

## Setup

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd AI_Chatbot_Gemini
    ```

2. **Configure the Gemini API**:
   - Sign up for an API key at the [Gemini API](https://gemini.com/) website.
   - Replace `your_gemini_api_key_here` in `app.py` with your actual Gemini API key.

3. **Run the Flask Application**:
    ```bash
    python app.py
    ```

4. **Access the Chatbot**:
   - Open a browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. Type your message in the input box on the webpage.
2. Click "Send" to get a response from the Gemini AI chatbot.
3. The conversation history will appear on the page.

## Files

- `app.py`: Main Flask application that routes requests, calls the Gemini API, and returns chatbot responses.
- `templates/index.html`: HTML file that contains the chatbot UI.
- `static/style.css`: Styles for the chatbot UI.
- `static/script.js`: JavaScript for sending and receiving messages asynchronously.

## License

This project is open-source and free to use.
