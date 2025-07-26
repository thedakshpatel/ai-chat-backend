from flask import Blueprint, request, jsonify
from services.db import messages_col
from services.vector_store import search_knowledge
from together import Together
import os

chat_bp = Blueprint("chat", __name__)

# Initialize Together client
client = Together(api_key="48e0751ab6fad0972443ee41fc26fe5060e1aadd2733112b313d50a31e29b19e")

@chat_bp.route("/chat", methods=["POST"])
def send_message():
    data = request.json
    user = data.get("username")
    message = data.get("message")

    # Step 1: Search relevant knowledge from ChromaDB
    try:
        context = search_knowledge(message, top_k=2)
        context_str = "\n".join(context)
    except Exception as e:
        return jsonify({"error": "Failed to search context from ChromaDB", "details": str(e)}), 500

    # Step 2: Call Together AI API
    try:
        prompt = f"Context:\n{context_str}\n\nQuestion: {message}"
        response = client.chat.completions.create(
            model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        reply = response.choices[0].message.content
    except Exception as e:
        return jsonify({"error": "LLM call failed", "details": str(e)}), 500

    # Step 3: Save to MongoDB
    try:
        messages_col.insert_one({
            "username": user,
            "message": message,
            "reply": reply
        })
    except Exception as e:
        return jsonify({"error": "Failed to save message", "details": str(e)}), 500

    return jsonify({"reply": reply})

@chat_bp.route("/chat/history", methods=["GET"])
def get_history():
    username = request.args.get("username")
    try:
        history = list(messages_col.find({"username": username}, {"_id": 0}))
        return jsonify(history)
    except Exception as e:
        return jsonify({"error": "Failed to fetch chat history", "details": str(e)}), 500
