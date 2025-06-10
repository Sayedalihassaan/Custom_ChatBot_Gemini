```markdown
# 🤖 Custom Gemini Assistant

A conversational AI assistant built with **LangChain**, **Streamlit**, and **Google's Gemini 1.5 model**. This project allows users to interact with a friendly and configurable AI chatbot through a simple web interface.

---

## 🚀 Features

- 🔐 **Secure API Integration** using `.env`
- 💬 **Interactive Chat Interface** powered by `streamlit_chat`
- 🔄 **Session Memory** using LangChain message schema
- ⚙️ **Customizable Assistant Role** from the sidebar
- 🧹 **Clearable Chat History**
- 📊 **Optional Token Usage Display**
- 🛠️ **Auto Project Structure Setup**

---

## 🗂️ Project Structure

```

Custom\_Gemini/
├── .env                   # Stores API Key securely
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── Custom\_Gemini.py       # Main Streamlit chatbot app
└── create\_structure.py    # Utility to create necessary project files

````

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Custom_Gemini.git
cd Custom_Gemini
````

### 2. Set Up Python Environment

Make sure Python 3.8 or higher is installed.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and add your **Google API Key**:

```
GOOGLE_API_KEY=your_google_api_key_here
```

> 🔐 *Keep your `.env` file private and never push it to public repositories.*

### 5. Run the App

```bash
streamlit run Custom_Gemini.py
```

---

## 🧪 Usage

1. Enter your message in the chat input box.
2. Customize the assistant's behavior using the "System Role" field in the sidebar.
3. Clear chat history anytime.
4. Enable token usage tracking (for debugging or optimization).

---

## 📁 File Descriptions

| File                  | Description                                        |
| --------------------- | -------------------------------------------------- |
| `Custom_Gemini.py`    | Main Streamlit application to interact with Gemini |
| `.env`                | Stores API keys and other secrets                  |
| `requirements.txt`    | Contains all necessary Python dependencies         |
| `README.md`           | Documentation for setting up and using the project |
| `create_structure.py` | Automatically creates base files and folders       |

---

## 📋 Requirements

* Python 3.8+
* Streamlit
* LangChain
* streamlit\_chat
* langchain\_google\_genai
* python-dotenv

See [`requirements.txt`](./requirements.txt) for full list.

---

## ✅ Example `.env` File

```dotenv
GOOGLE_API_KEY=your_api_key_here
```

---

## 🔧 Auto File Setup (Optional)

Use `create_structure.py` to generate required base files:

```bash
python create_structure.py
```

This ensures the presence of:

* `README.md`
* `.env`
* `requirements.txt`
* `Custom_Gemini.py`

---

## 📌 Notes

* This project uses **Gemini 1.5 Flash** for fast, contextual responses.
* Make sure your API key has the correct permissions.
* Use the token usage feature to monitor API usage and avoid overuse.

---

## 🙏 Acknowledgements

* [Google Generative AI](https://ai.google/discover/gemini/)
* [LangChain](https://www.langchain.com/)
* [Streamlit](https://streamlit.io/)
* [streamlit-chat](https://github.com/AI-Yash/st-chat)

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more info.

---

## ✨ Future Improvements

* Chat history persistence to file or DB
* Voice input/output integration
* Multi-user support with login
* Theme switcher for UI

---

```

---

Would you also like me to generate the contents of `requirements.txt` based on your code?
```
