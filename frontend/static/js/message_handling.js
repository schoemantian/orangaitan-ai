function adjustHeight(textarea) {
    textarea.style.height = '1px';
    textarea.style.height = (textarea.scrollHeight) + 'px';
  }
  
  function isCodeSnippet(text) {
    return text.startsWith("```") && text.endsWith("```");
  }
  
  function isBulletPoints(text) {
    const lines = text.split("\n");
    return lines.every((line) => line.trim().startsWith("- ") || line.trim().startsWith("* "));
  }
  
  function createCodeElement(text) {
    const code = document.createElement("code");
    code.textContent = text.slice(3, -3);
    const pre = document.createElement("pre");
    pre.appendChild(code);
    const header = document.createElement("div");
    header.classList.add("code-header");

    const languageLabel = document.createElement("span");
    languageLabel.classList.add("language-label");
    languageLabel.textContent = "Code";
    header.appendChild(languageLabel);

    const copyCodeText = document.createElement("span");
    copyCodeText.classList.add("copy-code");
    copyCodeText.textContent = "Copy code";
    copyCodeText.addEventListener("click", () => {
        navigator.clipboard.writeText(code.textContent).then(() => {
            console.log("Code copied to clipboard");
        }, (err) => {
            console.error("Error copying code to clipboard", err);
        });
    });
    header.appendChild(copyCodeText);

    const container = document.createElement("div");
    container.classList.add("code-container");
    container.appendChild(header);
    container.appendChild(pre);
    hljs.highlightElement(code);

    return container;
}

  
  function createBulletPoints(text) {
    const ul = document.createElement("ul");
    const lines = text.split("\n");
  
    lines.forEach((line) => {
      const li = document.createElement("li");
      li.textContent = line.trim().slice(2).trim();
      ul.appendChild(li);
    });
  
    return ul;
  }
  
  function escapeHtml(unsafe) {
    return unsafe
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }
  
  function parseText(text) {
    const lines = text.split('\n');
    const result = document.createDocumentFragment();
  
    let codeBlock = false;
    let preElement;
  
    lines.forEach((line, index) => {
      if (line.startsWith('```') && !codeBlock) {
        codeBlock = true;
        preElement = document.createElement('pre');
        const codeElement = document.createElement('code');
        preElement.appendChild(codeElement);
      } else if (line.startsWith('```') && codeBlock) {
        codeBlock = false;
        preElement.firstElementChild.textContent = preElement.firstElementChild.textContent.slice(0, -1);
        result.appendChild(preElement);
        hljs.highlightElement(preElement.firstElementChild);

        if (index < lines.length - 1) {
            result.appendChild(document.createElement('br'));
        }
    } else if (codeBlock) {
        preElement.firstElementChild.textContent += `${line}\n`;
    } else {
        const div = document.createElement('div');
        div.innerHTML = escapeHtml(line).replace(/`([^`]+)`/g, '<code>$1</code>');
        result.appendChild(div);
        if (index < lines.length - 1) {
          result.appendChild(document.createElement('br'));
        }
      }
    });
  
    return result;
  }
  
  
  async function sendMessage(event) {
    event.preventDefault();
  
    const messageInput = document.getElementById("message-input");
    const message = messageInput.value;
    const tokens = message.split(/\s+/);
  
    if (tokens.length > 1024) {
      console.error("Message exceeds the maximum token limit");
      return;
    }
  
    messageInput.value = "";
  
    const responseContainer = document.createElement("div");
    responseContainer.classList.add("message");
    responseContainer.classList.add("user-message");
    const parsedUserText = parseText(message);
    responseContainer.appendChild(parsedUserText);
    document.getElementById("messages").appendChild(responseContainer); 
  
    const responseType = document.getElementById("response-type").value;
  
    const response = await fetch("/process_message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message, response_type: responseType, new_chat: isNewChat, chat_id: currentChatId }),
    });
  
    const result = await response.json();
  
    if (isNewChat) {
      currentChatId = result.chat_id;
    }
  
    const botResponseContainer = document.createElement("div");
    botResponseContainer.classList.add("message");
    botResponseContainer.classList.add("bot-message");
  
    if (result.error) {
      botResponseContainer.textContent = result.error;
    } else {
      if (responseType === "image") {
        const imgElement = document.createElement("img");
        imgElement.src = result.response;
        imgElement.classList.add("generated-image");
        botResponseContainer.appendChild(imgElement);
      } else {
        const parsedText = parseText(result.response);
        botResponseContainer.appendChild(parsedText);
      }
    }
    document.getElementById("messages").appendChild(botResponseContainer);
  
    const messages = document.getElementById("messages");
    messages.scrollTop = messages.scrollHeight;
  
    isNewChat = false;
  
    await loadChatList();
  }
  
  document.addEventListener('DOMContentLoaded', (event) => {
    hljs.highlightAll();
});
