PolyLingo: Multilingual AI Chatbot
Powered by: Flask + Transformers (FLAN-T5) + Google Translate + TTS + Web UI

📌 Objective
PolyLingo is an intelligent chatbot that:

Accepts user queries in any language

Understands the intent (question, task, or problem)

Responds with natural, helpful answers

Translates the answer into the user-selected output language

Supports voice playback (Text-to-Speech) in that language

Example: If a user asks "आज की तारीख क्या है?" and selects "English" as output, the bot replies “Today is 27 July 2025.”
If "Hindi" is selected, it replies: “आज 27 जुलाई 2025 है।”

⚙️ Architecture Overview
plaintext
Copy
Edit
[User Input (Any Language)]
          ↓
  [Language Detection (langdetect)]
          ↓
  [Translate to English (Googletrans)]
          ↓
  [FLAN-T5 Reasoning/Answer (Transformers)]
          ↓
  [Translate Answer to Selected Language]
          ↓
  [Frontend Display + Voice TTS (SpeechSynthesis)]
🧠 Backend: app.py
Libraries Used
bash
Copy
Edit
pip install flask transformers langdetect googletrans==4.0.0-rc1
Features
Component	Description
langdetect	Detects input language
googletrans	Translates both input → English and English → output
transformers	FLAN-T5 model used for understanding & generating answers
chat_memory	Stores last 3 messages per session
/chat endpoint	Accepts JSON (message, session_id, language)
/ endpoint	Renders frontend (HTML)

Key Functions
detect_language(text)
Detects the language of the input string.

polylingo_chat(user_input, reply_lang, session_id)
Detects source language

Translates to English

Builds an intelligent prompt

Uses FLAN-T5 model to generate answers

Translates output to selected language

💻 Frontend: templates/index.html
Key Features
Feature	Description
#userInput	Input field for the question
#sessionId	Optional session tracking
#replyLang	Language dropdown
#speakBtn	Voice output (SpeechSynthesis API)
AJAX POST /chat	Sends query to backend and receives answer
Friendly UI	CSS-styled, responsive, clear

Languages Supported
You can expand <select> dropdown in HTML with any valid Google Translate language codes, e.g.:

en - English

hi - Hindi

fr - French

ta - Tamil

de - German

es - Spanish

zh-cn - Chinese Simplified

🧪 Sample Flow
plaintext
Copy
Edit
Input: "Wie spät ist es?" (German)
Selected Output: "French"

→ Detected as German
→ Translated to English: "What time is it?"
→ FLAN-T5 answers: "It's currently 5:30 PM."
→ Translated to French: "Il est actuellement 17h30."
→ User sees + hears the French response
📤 API Endpoint: /chat
POST Request
json
Copy
Edit
{
  "message": "Bonjour, comment ça va ?",
  "session_id": "user123",
  "language": "en"
}
Response
json
Copy
Edit
{
  "response": "Hello, how are you?"
}
🔊 TTS: Voice Output
Uses the built-in SpeechSynthesisUtterance API in JavaScript to:

Automatically detect the output language (from dropdown)

Speak the answer in that language (if supported by browser)

