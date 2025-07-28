<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>🌍 PolyLingo Chatbot</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f0f4f8;
      padding: 2rem;
    }
    .chat-box {
      max-width: 600px;
      margin: auto;
      background: #fff;
      padding: 1.5rem;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    input, select, button {
      margin-top: 10px;
      padding: 0.6rem;
      width: 100%;
      font-size: 1rem;
    }
    #responseBox {
      margin-top: 20px;
      padding: 1rem;
      background: #e6f7ff;
      border-left: 4px solid #1890ff;
      display: none;
    }
    #speakBtn {
      margin-top: 10px;
      background-color: #1890ff;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="chat-box">
    <h2>🌍 PolyLingo Chatbot</h2>
    <input type="text" id="userInput" placeholder="Type your message..." />
    <input type="text" id="sessionId" placeholder="Session ID (default)" value="default" />
    <select id="replyLang">
      <option value="en">English</option>
      <option value="fr">French</option>
      <option value="hi">Hindi</option>
      <option value="ta">Tamil</option>
      <option value="es">Spanish</option>
      <option value="de">German</option>
      <option value="zh-cn">Chinese</option>
      <!-- Add more language codes as needed -->
    </select>
    <button onclick="sendMessage()">Send</button>

    <div id="responseBox">
      <strong>PolyLingo:</strong>
      <p id="responseText"></p>
      <button id="speakBtn">🔊 Speak</button>
    </div>
  </div>

  <script>
    async function sendMessage() {
      const message = document.getElementById("userInput").value;
      const sessionId = document.getElementById("sessionId").value || "default";
      const replyLang = document.getElementById("replyLang").value;

      const res = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message, session_id: sessionId, language: replyLang })
      });

      const data = await res.json();
      const text = data.response || "No response received.";

      document.getElementById("responseText").innerText = text;
      document.getElementById("responseBox").style.display = "block";

      // Store replyLang globally
      window.currentLang = replyLang;
    }

    // 🔊 Speak the response
    document.getElementById("speakBtn").addEventListener("click", () => {
      const text = document.getElementById("responseText").innerText;
      const lang = window.currentLang || "en";

      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = lang;
      speechSynthesis.speak(utterance);
    });
  </script>
</body>
</html>
