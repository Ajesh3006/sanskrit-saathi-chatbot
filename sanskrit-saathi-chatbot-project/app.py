from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

RESPONSES = {
    "hello": "नमस्ते! Namaste! How can I help you?",
    "namaste": "नमस्ते (Namaste) — greetings to you!",
    "thanks": "स्वागतम्! (Swāgatam) — You are welcome!",
    "thank you": "स्वागतम्! (Swāgatam) — You are welcome!",
    "how are you": "अहं कुशलः अस्मि। (Aham kuśalaḥ asmi) — I am well.",
    "good morning": "सुप्रभातम्! (Suprabhātam) — Good morning!",
    "bye": "पुनर्मिलामः! (Punarmilāmaḥ) — See you again!",
    "help": "Try: hello, namaste, how are you, good morning, thanks, or bye."
}

def get_reply(message):
    cleaned = " ".join(message.lower().strip().split())
    for phrase, reply in RESPONSES.items():
        if phrase in cleaned:
            return reply
    return ("मम क्षमां कुरु। I don't know that phrase yet. "
            "Try 'namaste', 'how are you', 'thanks', or 'help'.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    if not message:
        return jsonify({"reply": "Please enter a message."}), 400
    return jsonify({"reply": get_reply(message)})

@app.route("/health")
def health():
    return jsonify({"status": "ok", "application": "Sanskrit Chatbot"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
