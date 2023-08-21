function openSettingsModal() {
    document.getElementById('settings-modal').classList.remove('settings-modal-hidden');
    let currentTheme = getCurrentThemePreference();
    let themeSelectionDropdown = document.getElementById('theme-selection');
    themeSelectionDropdown.value = currentTheme;
  }
  
  function closeSettingsModal() {
    document.getElementById('settings-modal').classList.add('settings-modal-hidden');
  }
  
  function showGeneralSettings() {
    document.getElementById('general-settings').classList.remove('settings-modal-hidden');
    document.getElementById('data-controls-settings').classList.add('settings-modal-hidden');
  }
  
  function showDataControlsSettings() {
    document.getElementById('general-settings').classList.add('settings-modal-hidden');
    document.getElementById('data-controls-settings').classList.remove('settings-modal-hidden');
  }
  
  function toggleTheme(selectedTheme) {
    let body = document.body;
    let highlightjsStyles = document.getElementById("highlightjs-styles");

    if (selectedTheme === 'Dark') {
        body.className = 'theme-dark';
        highlightjsStyles.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/github-dark.min.css';
        setThemePreference('dark');
    } else if (selectedTheme === 'Light') {
        body.className = 'theme-light';
        highlightjsStyles.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/github.min.css';
        setThemePreference('light');
    } else {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            body.className = 'theme-dark';
            highlightjsStyles.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/github-dark.min.css';
        } else {
            body.className = 'theme-light';
            highlightjsStyles.href = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/github.min.css';
        }
        setThemePreference('system');
    }
}


function getCurrentThemePreference() {
  let bodyClass = document.body.className;
  if (bodyClass === 'theme-dark') {
      return 'Dark';
  } else if (bodyClass === 'theme-light') {
      return 'Light';
  } else {
      return 'System';
  }
}

  function setThemePreference(theme) {
    fetch('/set_theme_preference', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ theme: theme })
    }).then(response => response.json()).then(data => {
        if (data.message) {
        } else {
        }
    });
}

  function toggleChatHistory() {
    // Toggle chat history logic here
  }

  
  