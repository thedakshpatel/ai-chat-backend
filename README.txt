AI Chat Backend with Flask, MongoDB, Together AI, and ChromaDB
___________________________________________________________________

This project is a lightweight backend application that enables:

User authentication (Sign up / Login)

Conversational interaction with an AI agent powered by Together AI

Chat history management using MongoDB

Context-aware responses using ChromaDB for knowledge retrieval

It is built using Python (Flask framework) and is easily extendable for production use.
_______________________________________________________________________

Requirements

Python 3.10 or higher

MongoDB installed and running (default: localhost:27017)

Together AI API key (get it from https://platform.together.xyz/)

Internet connection
_________________________________________________________________________

Setup Instructions (Windows)

Open PowerShell or CMD in the project folder.

Install required Python packages:

python -m pip install -r requirements.txt

Ensure MongoDB service is running locally.

Set your Together AI API key:

set TOGETHER_API_KEY="48e0751ab6fad0972443ee41fc26fe5060e1aadd2733112b313d50a31e29b19e"

Add initial knowledge to ChromaDB:

python init_knowledge.py

-> You should update init_knowledge.py with knowledge relevant to your application before running it.

Run the Flask app:

python app.py
_______________________________________________________________________________________________

API Endpoints

POST /signup

Registers a new user.

Example:

{
  "username": "yourname",
  "password": "yourpass"
}

POST /login

Logs in an existing user.

Example:

{
  "username": "yourname",
  "password": "yourpass"
}

POST /chat

Sends a message to the AI agent.

Example:

{
  "username": "yourname",
  "message": "What does organic farming avoid?"
}

Internally:

Retrieves related knowledge from ChromaDB

Sends context and message to Together AI

Returns the AI-generated reply

GET /chat/history?username=yourname

Returns all chat history for the specified user.
______________________________________________________________________

ChromaDB Notes

ChromaDB is used to store searchable contextual knowledge.

You must update init_knowledge.py with your domain-specific facts or data.

This setup enables retrieval-augmented generation (RAG) style chat.
_________________________________________________________________________________

In future, you can:

Extend it to support file uploads (e.g., PDFs)

Load large corpora or FAQ docs for smarter context
____________________________________________________________________________________
Error Handling

All major operations (LLM, DB, vector store) are wrapped in try/except blocks.

On failure, errors are returned in the following format:

{
  "error": "Descriptive error message",
  "details": "Technical explanation"
}
___________________________________________________________________________________
Test Example

Run the initialization script once:

python init_knowledge.py

(Update it as per your domain knowledge before running)

Sign up and log in:

{
  "username": "daksh",
  "password": "yourpass"
}

Ask a question through the chat endpoint:

{
  "username": "daksh",
  "message": "What does organic farming avoid?"
}

Get a relevant AI reply using ChromaDB-enhanced context.
_______________________________________________________________________________

Future Enhancements

Add PDF or document ingestion (e.g., langchain for parsing + chunking)

Create a frontend (React/HTML) for user-friendly interface

Add admin dashboard to manage users or knowledge base

Support more LLMs (OpenAI, Gemini, etc.) using API switches
________________________________________________________________________________

Troubleshooting

Ensure MongoDB is running on localhost:27017

Check that your Together API key is correctly set in the environment

Verify internet connection for LLM access
____________________________________________________________________________________

Author

Daksh Maheshkumar Patel
Email: thedmpatel04@gmail.com
GitHub: https://github.com/thedakshpatel
