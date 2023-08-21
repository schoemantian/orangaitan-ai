let currentChatId = null;
let isNewChat = true;

async function loadChatHistory(chatId) {
    const response = await fetch(`/chat/${chatId}`);
    const result = await response.json();
  
    const messagesContainer = document.getElementById("messages");
    messagesContainer.innerHTML = "";
  
    for (const message of result.chat_history) {
      const userMessageContainer = document.createElement("div");
      userMessageContainer.classList.add("message");
      userMessageContainer.classList.add("user-message");
      const parsedUserText = parseText(message.user_message);
      userMessageContainer.appendChild(parsedUserText);
      messagesContainer.appendChild(userMessageContainer);
  
      const botMessageContainer = document.createElement("div");
      botMessageContainer.classList.add("message");
      botMessageContainer.classList.add("bot-message");
      const parsedBotText = parseText(message.bot_message);
      botMessageContainer.appendChild(parsedBotText);
      messagesContainer.appendChild(botMessageContainer);
    }
  
    currentChatId = chatId;
    isNewChat = false;
  }
  
  async function loadChatList() {
    const response = await fetch("/chat_history");
    const result = await response.json();
  
    const chatListContainer = document.getElementById("chat-history-container");
    chatListContainer.innerHTML = "";
  
    for (const chat of result.chats) {
      const chatElement = document.createElement("div");
      chatElement.classList.add("chat");
  
      const chatTitle = document.createElement("span");
      chatTitle.classList.add("chat-title");
      chatTitle.textContent = chat.last_message;
      chatElement.appendChild(chatTitle);
  
      chatElement.addEventListener("click", function() {
        loadChatHistory(chat.id);
      });
  
      const deleteButton = document.createElement("i");
      deleteButton.className = "fas fa-trash trash-icon";
      deleteButton.addEventListener("click", async function(event) {
        event.stopPropagation();
        const response = await fetch(`/delete_chat/${chat.id}`, { method: "DELETE" });
        if (response.ok) {
          loadChatList();
        } else {
          console.error("Error deleting chat");
        }
      });
  
      chatElement.appendChild(deleteButton);
      chatListContainer.appendChild(chatElement);
    }
  }

  function clearAllChats() {
    // Clear all chats logic here
  }
  
  function exportData() {
    // Export data logic here
  }

  
  window.onload = function() {
    loadChatHistory();
    loadChatList();
  };
  