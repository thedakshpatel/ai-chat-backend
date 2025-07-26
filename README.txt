
AI Chat Backend with Flask, MongoDB, Together AI, and ChromaDB
---------------------------------------------------------------

This is a simple backend project that lets you:
- Sign up and log in as a user
- Chat with an AI agent (powered by Together AI)
- Store and retrieve chat history using MongoDB
- Use ChromaDB to give the AI knowledge-based context before replying

---------------------------------------------------------------
Requirements:
-------------
- Python 3.10 or above recommended
- MongoDB installed and running (localhost:27017)
- Together AI API key (get it from https://platform.together.xyz/)
- Internet connection

---------------------------------------------------------------
Setup Instructions (For Windows)

1. Open PowerShell or CMD inside the project folder.

2. Install all required packages:
   python -m pip install -r requirements.txt

3. Make sure MongoDB is running on your system.

4. Set your Together AI API key:
   set TOGETHER_API_KEY="48e0751ab6fad0972443ee41fc26fe5060e1aadd2733112b313d50a31e29b19e"

5. Add initial knowledge to ChromaDB:
   python init_knowledge.py

6. Run the Flask app:
   python app.py

---------------------------------------------------------------
API Endpoints

1. POST /signup
   Example JSON body:
   {
     "username": "yourname",
     "password": "yourpass"
   }

2. POST /login
   {
     "username": "yourname",
     "password": "yourpass"
   }

3. POST /chat
   {
     "username": "yourname",
     "message": "What does organic farming avoid?"
   }

   → The app will:
     - Search ChromaDB for related knowledge
     - Send the knowledge + your question to Together AI
     - Return the AI's response

4. GET /chat/history?username=yourname
   → Shows the full chat history for that user.

---------------------------------------------------------------
ChromaDB Notes

- ChromaDB is used to store and search knowledge before sending to the AI.
- Knowledge is added using `init_knowledge.py`.
- You can extend this to support file uploads or FAQ storage later.

---------------------------------------------------------------
Error Handling

- All critical actions (LLM calls, DB actions, vector search) use try/except.
- Errors return clear JSON like:
  {
    "error": "LLM call failed",
    "details": "..."
  }

---------------------------------------------------------------
Test Example:

1. Run this to populate ChromaDB:
   python init_knowledge.py

2. Send a message like:
   "What does organic farming avoid?"

3. You'll get an AI answer with context like:
   "Organic farming avoids synthetic chemicals..."

---------------------------------------------------------------
Need Help?

- Make sure MongoDB is running
- Always set TOGETHER_API_KEY before starting
- Internet is required for Together AI

Author: Daksh Maheshkumar Patel
Email: thedmpatel04@gmail.com
