import requests

from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from database import db
from models.conversation import Conversation

OLLAMA_BASE_URL = "http://localhost:11434/api/generate"

chat_blueprint = Blueprint("chat", __name__, template_folder="../views")


@chat_blueprint.route("/")
@login_required
def index():
    conversations = Conversation.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", conversations=conversations)


# Accepts a prompt from the user
@chat_blueprint.route("/api/chat", methods=["POST"])
@login_required
def chat():
    data = request.json

    if not data or "prompt" not in data:
        return jsonify({"error": "Prompt is required"})

    prompt = data["prompt"]

    # Payload to call ollama
    payload = {
        "model": "qwen:0.5b",
        "prompt": prompt,
        "stream": False,
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(OLLAMA_BASE_URL, headers=headers, json=payload)
        response.raise_for_status()
    except Exception as e:
        return jsonify({"error": f"Failed to connect witl OLLAMA: str{e}"}), 500

    result = response.json()
    response_text = result.get("response", "")

    if not response_text:
        return jsonify({
            "error": "Failed to connect witl OLLAMA: Could not extract response text from ollama"
        }), 500

    conversation = Conversation(
        user_id=current_user.id, prompt=prompt, response=response_text
    )

    db.session.add(conversation)
    db.session.commit()

    return jsonify({"response": response_text})
