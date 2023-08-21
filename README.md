
# Orangaitan: A Multi-Modal AI Chat App
![Orangaitan Logo](https://themaintenanceman.co.za/wp-content/uploads/2023/08/logo_light.png)

🐵 Welcome, dear friends of the jungle! I'm Orangaitan, and I'm here to introduce you to a new world of AI chat and multi-modal conversations. Built with love, care, and a strong desire to help both humans and my fellow animal friends, Orangaitan is not just an app but a movement.

## Overview
Orangaitan is a free and open-source multi-modal AI chat app designed to engage, educate, and empower. With Google SSO, OpenAI APIs, and the ability to integrate various pre-trained LLMs like Llama-2, and more, Orangaitan offers a robust and secure platform for exploratory AI interactions.

## Support Orangaitan by Donating to African Wildlife Foundation

<p align="center">
  <img src="https://aaf1a18515da0e792f78-c27fdabe952dfc357fe25ebf5c8897ee.ssl.cf5.rackcdn.com/2320/logo-awf.png?v=1657570835000" alt="African Wildlife Foundation Logo" width="200">
  <br>
  <a href="https://secure.awf.org/page/119125/donate/1" target="_blank" style="display: inline-block; background-color: #4CAF50; color: white; padding: 20px 30px; text-align: center; text-decoration: none; font-size: 20px; font-weight: bold; border-radius: 10px; margin-top: 15px;">Donate to African Wildlife & Endangered Animals</a>
</p>

Join the Orangaitan movement by contributing to the African Wildlife Foundation. Your support helps protect endangered animals and preserves the natural beauty of our world. Together, we can make a difference!
 For more information about what African Wildlife Foundation does you can visit their website at https://www.awf.org/


### Features Overview:
* **Google SSO:** Secure and seamless login with Google SSO, including domain-specific restrictions.
* **OpenAI Integration:** Access to powerful OpenAI APIs, including GPT-4 and DALL-E.
* **Data Leakage Protection:** A built-in DLP layer to identify and block restricted keywords.
* **Contextual Conversations:** A local database to enable higher contextual conversations, storing and utilizing snippets of previous interactions.
* **Multi-User Support:** Host on a server to enable multi-user interactions.
---
Join me, Orangaitan, as we embark on a journey to explore the fascinating world of AI while upholding our responsibility to protect and preserve the natural environment.

---

##  Features of Orangaitan
### Google Single Sign-On (SSO)
Orangaitan's secure login is made possible through Google SSO. Simply use your Google credentials to sign in, and if you're an administrator, you can even restrict access to specific domains. No fuss, just one click, and you're in!

### OpenAI Integration
Orangaitan embraces the power of AI by integrating OpenAI's cutting-edge APIs. From textual conversations to image responses with DALL-E, it's a jungle of possibilities! You can even bring in pre-trained models like Llama-2 from HuggingFace. Orangaitan makes AI chat exciting and exploratory.

### Data Leakage Protection (DLP)
To keep the jungle safe, Orangaitan has a built-in DLP layer. By identifying and blocking restricted keywords, it ensures that no sensitive information slips through the vines. Data protection is a priority in our jungle!

### Contextual Conversations
With Orangaitan, conversations flow like a river in the jungle. A small but efficient local database stores snippets of previous conversations, allowing for contextual understanding and seamless switching between topics. Dive into meaningful and engaging interactions!

### Multi-User Support
Host Orangaitan on a server, and invite your fellow explorers to join the adventure. Multi-user support means more friends, more conversations, and more learning. **Together, we grow!**

### Image Responses with DALL-E
Orangaitan's creativity knows no bounds! With integration of OpenAI's DALL-E, you can generate fascinating image responses based on text prompts. A picture is worth a thousand words, and in our jungle, those words come to life!

---

![Orangaitan Login Page](https://themaintenanceman.co.za/wp-content/uploads/2023/08/Screenshot-2023-08-20-at-16.14.51.png)
### Login Page
This screenshot showcases the login page of Orangaitan, where users can sign in using Google SSO for secure access.

---

![Orangaitan Chat Interface](https://themaintenanceman.co.za/wp-content/uploads/2023/08/Screenshot-2023-08-20-at-16.18.10.png)
### Chat Interface
Here, we see the main chat interface of Orangaitan, where users can engage in multi-modal conversations with AI.

---

<p float="center">
  <img src="https://themaintenanceman.co.za/wp-content/uploads/2023/08/Screenshot-2023-08-20-at-16.37.00.png" width="47%" alt="Conversational Flow Light Mode">
  <img src="https://themaintenanceman.co.za/wp-content/uploads/2023/08/Screenshot-2023-08-20-at-16.40.23.png" width="47%" alt="Conversational Flow Dark Mode">
</p>

### Conversational Flow
This screenshot captures an engaging conversation within Orangaitan, demonstrating the fluidity and intelligence of the AI responses.

---

![Orangaitan Image Response](https://themaintenanceman.co.za/wp-content/uploads/2023/08/Screenshot-2023-08-20-at-16.58.17.png)
### Chat Interface
Here, we see an example of a DALL-E generated image response, showcasing the multi-modal capabilities of Orangaitan.

**NOTE:** Dall-E 2 was integrated for testing and efficiency, many other image generation application API's are available and on request more can be added

---

##  Installation
1. **Clone the Repository:** Use your favorite Git tool to clone the Orangaitan repository to your local machine.
1. **Install Dependencies:** Navigate to the project folder and run `pip install -r requirements.txt` to install all necessary Python packages.
1. **Configure Environment Variables:** Set up your environment variables, including Google OAuth credentials, OpenAI API key, and other necessary configurations in the config.py file as follows:

```
import os

SECRET_KEY = "<SECRET_KEY_HERE>"
GOOGLE_OAUTH_CLIENT_ID = "<GOOGLE_OAUTH_CLIENT_ID_HERE>"
GOOGLE_OAUTH_CLIENT_SECRET = "<GOOGLE_OAUTH_CLIENT_SECRET_HERE>"
OPENAI_API_KEY = "<OPENAI_API_KEY_HERE>"


os.environ["SECRET_KEY"] = SECRET_KEY
os.environ["GOOGLE_CLIENT_ID"] = GOOGLE_OAUTH_CLIENT_ID
os.environ["GOOGLE_CLIENT_SECRET"] = GOOGLE_OAUTH_CLIENT_SECRET
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```
4. **Start the Server:** Run flask run to start the Orangaitan server. Visit http://localhost:5000 in your browser to access the app, Note that the DB is auto-created, when running the App.

----

* You can Obtain your [OpenAI Secret here](https://platform.openai.com/account/api-keys)
*  you can obtain your [Google Client Secret and ID here](https://console.cloud.google.com/apis/credentials/oauthclient/)

To run the app locally make sure you set the `Authorized redirect URI's` to the following:
```
http://localhost:5000/login/google/authorized
http://127.0.0.1:5000/login/google/authorized
```

## Usage
* **Login with Google SSO:** Click the "Login with Google" button on the landing page and enter your credentials.
* **Explore the Chat Interface:** Once logged in, you'll find a user-friendly chat interface. Feel free to ask questions, request images, or explore various AI models.
* **Switch Topics Seamlessly:** With contextual conversations, you can switch between topics and maintain the flow of the conversation.
* **Check Out Image Responses:** Try prompts that trigger DALL-E to generate creative image responses.
* **Logout:** Click the logout button, which is in the popup menu, in the side panel when clicking on your user name, when you're done exploring.

## Troubleshooting
Facing any challenges swinging through the jungle? Feel free to reach out to our community on GitHub or reach out to me directly via [LinkedIn](https://www.linkedin.com/in/tian-schoeman-b96342104/) or [GitHub](https://github.com/schoemantian) or refer to the detailed documentation available in the repository.

### 🐾  Follow the paw prints, and you'll never be lost in the jungle of Orangaitan!

# The Orangaitan Movement
🌍 **The Orangaitan Movement:** AI, Ecology, and Ethical Balance
Welcome to the heart of the jungle, where Orangaitan's true essence resides. Beyond the code and technology, Orangaitan is a movement, a call to action, and a reminder of our collective responsibility.

### AI and Ecology
The rise of AI has brought unprecedented possibilities, but it also comes with an ecological footprint. Massive AI servers with powerful GPUs consume electricity and emit immense heat, impacting the environment.

Orangaitan urges you to recognize this impact and strive for innovation that's harmonious with nature. Let's find better ways to advance technology while protecting the world for animals, plants, and future generations.

### The Orangaitan Pledge
Orangaitan invites you to join the movement:

* **Learn Responsibly:** Educate yourself about the ecological impact of technology and find sustainable solutions.
* **Develop Mindfully:** Build and innovate with care for the environment and all its inhabitants.
* **Support the Cause:** Contribute to open-source projects like Orangaitan that promote education, awareness, and ecological balance.

### Support Endangered Animals
Orangaitan is more than just an app; it's a symbol of hope and care for endangered animals and ecosystems. By supporting Orangaitan and advocating for educational tools, you can make a difference.

[Donate to the African Wildlife Foundation](https://secure.awf.org/page/119125/donate/1) and help us protect the beauty, diversity, and richness of our planet.
<p align="center">
  <img src="https://aaf1a18515da0e792f78-c27fdabe952dfc357fe25ebf5c8897ee.ssl.cf5.rackcdn.com/2320/logo-awf.png?v=1657570835000" alt="African Wildlife Foundation Logo" width="200">
  <br>
  <a href="https://secure.awf.org/page/119125/donate/1" target="_blank" style="display: inline-block; background-color: #4CAF50; color: white; padding: 20px 30px; text-align: center; text-decoration: none; font-size: 20px; font-weight: bold; border-radius: 10px; margin-top: 15px;">Donate to African Wildlife & Endangered Animals</a>
</p>

🌳 Together, we can swing towards a future where technology and nature coexist in harmony!

---
---

# Contribute to the Cause: Join the Orangaitan Family
Orangaitan is not just an app; it's a community, a family, and a platform where every explorer has a place. As an open-source project, Orangaitan thrives on collaboration, innovation, and shared passion.

## Contribute to the Code
* **Fork and Clone:** Fork the Orangaitan repository and clone it to your local machine.
* **Explore and Experiment:** Dive into the code, make enhancements, fix bugs, or add new features.
* **Submit a Pull Request:** Share your contributions by submitting a pull request. Together, we build!

## Support the Mission
Orangaitan's mission goes beyond code. It's about **FREE** education, awareness, and a commitment to our planet. Support the mission by:

* **Spreading the Word:** Share Orangaitan with friends, colleagues, and fellow explorers.
* **Joining the Conversation:** Engage in discussions, ask questions, and contribute ideas.
* **Donating to the Cause:** Support the African Wildlife Foundation and help protect endangered animals.

## License

Orangaitan is fully free and open-source, licensed under the GNU General Public License v3. By liking and supporting Orangaitan, you contribute to a greater cause, fostering a community of learning, growth, and compassion.

The GPL v3 license ensures that any changes made to the code must be shared under the same license, thereby maintaining the open-source nature of the project.

For more details, please refer to the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html).

![GPL v3 Logo](https://www.gnu.org/graphics/gplv3-127x51.png)






















