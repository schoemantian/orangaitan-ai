const maxLines = 3;
const lineHeight = 15;

document.querySelector(".newChatButton").addEventListener("click", function() {
  document.getElementById("messages").innerHTML = "";
  isNewChat = true;
});

document.getElementById("message-input").addEventListener("input", function (event) {
  const maxTokens = 2048;
  const tokens = event.target.value.split(/\s+/); 

  if (tokens.length > maxTokens) {
    tokens.pop();
    event.target.value = tokens.join(" ");
  }

  adjustHeight(event.target);

  if (event.target.scrollHeight <= lineHeight * maxLines) {
    event.target.style.overflowY = 'hidden';
  } else {
    event.target.style.overflowY = 'scroll';
    event.target.style.height = lineHeight * maxLines + 'px';
  }
});


document.getElementById("message-input").addEventListener("keypress", function (event) {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    const messageForm = document.getElementById("message-form");
    sendMessage(new Event("submit", { target: messageForm, cancelable: true }));
  }
});

