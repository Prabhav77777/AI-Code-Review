<div align="center">

# 🤖 AI Code Review Assistant

### Instant, intelligent code reviews powered by Llama 3.3 70B via the Groq API

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit_App-00C896?style=for-the-badge)](https://ai-code-review-lime.vercel.app/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/Powered_by-Groq_API-F55036?style=for-the-badge&logo=lightning&logoColor=white)](https://groq.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Vercel](https://img.shields.io/badge/Deployed_on-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-license)

</div>

---

## 📖 Project Overview

**AI Code Review Assistant** is a full-stack web application that brings the power of **Large Language Models** to everyday code review.

Simply **paste your source code**, hit **Review**, and within seconds get a structured breakdown of:

- 🐞 **Issues** found in your code
- 💡 **Suggestions** for improvement
- ✨ A fully **optimized version** of your code

Under the hood, the app sends your code to **Llama 3.3 70B Versatile** via the blazing-fast **Groq API**, parses the model's response, and presents it in a clean, easy-to-read interface — no setup, no sign-up, just paste and review.

> Built as a practical demonstration of integrating LLM-powered tooling into a real-world developer workflow, with a lightweight FastAPI backend and a vanilla JS frontend.

---

## 🌐 Live Demo

🔗 **[https://ai-code-review-lime.vercel.app/](https://ai-code-review-lime.vercel.app/)**

> 💡 Try pasting a small function with an obvious bug (e.g., an off-by-one loop or an unused variable) and watch the AI catch it instantly!

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 **AI-Powered Code Reviews** | Leverages Llama 3.3 70B Versatile through Groq for fast, high-quality analysis |
| 🐞 **Automatic Issue Detection** | Identifies bugs, anti-patterns, and code smells |
| 💡 **Actionable Suggestions** | Provides clear, practical recommendations to improve code quality |
| ✨ **Optimized Code Generation** | Returns a refactored, improved version of your code |
| ⚡ **Fast Response Times** | Powered by Groq's high-throughput inference engine |
| 🎨 **Clean & Responsive UI** | Minimal, distraction-free interface that works on any screen |
| 📋 **Paste-and-Review Workflow** | Zero setup — paste your code and click a single button |

---

## 🛠️ Tech Stack

### Frontend

| Technology | Purpose |
|---|---|
| 🌐 HTML5 | Page structure and layout |
| 🎨 CSS3 | Styling and responsive design |
| ⚙️ JavaScript | API communication and dynamic UI updates |

### Backend

| Technology | Purpose |
|---|---|
| 🐍 Python | Core backend language |
| ⚡ FastAPI | REST API framework serving the `/review` endpoint |
| 📦 Pydantic | Request data validation (`CodeInput` model) |

### AI / Intelligence Layer

| Technology | Purpose |
|---|---|
| 🤖 Groq API | High-speed LLM inference provider |
| 🦙 Llama 3.3 70B Versatile | The model performing the actual code review |

### Deployment & Environment

| Technology | Purpose |
|---|---|
| ▲ Vercel | Hosting for the frontend |
| 🐍 Python Backend API | Serves the FastAPI review endpoint |
| 🔐 python-dotenv | Manages environment variables (e.g., API keys) |

---

## 🏗️ Project Architecture

```
┌──────────────────────┐        HTTPS POST /review        ┌──────────────────────────┐
│                       │ ────────────────────────────────▶ │                          │
│   Frontend (Vercel)   │                                    │   FastAPI Backend        │
│   HTML / CSS / JS     │ ◀──────────────────────────────── │   (main.py)              │
│                       │     JSON: issues, suggestions,    │                          │
└──────────────────────┘     optimized_code                 └────────────┬─────────────┘
                                                                           │
                                                                           │ Prompt with
                                                                           │ user's code
                                                                           ▼
                                                              ┌──────────────────────────┐
                                                              │       Groq API           │
                                                              │  Llama 3.3 70B Versatile  │
                                                              └────────────┬─────────────┘
                                                                           │
                                                                           │ Raw AI response
                                                                           │ (ISSUES / SUGGESTIONS /
                                                                           │  OPTIMIZED_CODE)
                                                                           ▼
                                                              ┌──────────────────────────┐
                                                              │  reviewer.py parses       │
                                                              │  response into structured │
                                                              │  JSON for the frontend    │
                                                              └──────────────────────────┘
```

---

## ⚙️ How It Works (Review Pipeline)

1. **User Input** — The user pastes their source code into the textarea on the frontend and clicks **"Review Code"**.
2. **API Request** — The frontend sends a `POST` request to the `/review` endpoint of the FastAPI backend with the code as a JSON payload (`{ "code": "..." }`).
3. **Validation** — FastAPI validates the incoming request using the `CodeInput` Pydantic model.
4. **Prompt Construction** — `reviewer.py` builds a structured prompt instructing the model to return its response in a strict `ISSUES / SUGGESTIONS / OPTIMIZED_CODE` format.
5. **LLM Inference** — The prompt is sent to the **Groq API**, which runs it through **Llama 3.3 70B Versatile** and returns a raw text response.
6. **Response Parsing** — The backend parses the raw text into three distinct sections: a list of issues, a list of suggestions, and the optimized code block.
7. **JSON Response** — The structured result is returned to the frontend as JSON.
8. **UI Rendering** — The frontend dynamically renders the issues, suggestions, and optimized code into their respective panels for the user to read.

If the AI service fails or the response can't be parsed, the backend gracefully falls back to a default response so the UI never breaks.

---

## 🚀 Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Code-Review.git
cd AI-Code-Review
```

### 2️⃣ Create a Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` File

In the project's `backend` directory, create a file named `.env`.

### 5️⃣ Add Your Groq API Key

Add your Groq API key to the `.env` file (see [Environment Variables](#-environment-variables-env) below).

### 6️⃣ Run the FastAPI Server

```bash
cd backend
uvicorn main:app --reload
```

The backend will now be running at:  
👉 `http://127.0.0.1:8000`

### 7️⃣ Open the Frontend

Simply open `frontend/index.html` in your browser, **or** serve it with a local server:

```bash
cd frontend
python -m http.server 5500
```

Then visit:  
👉 `http://127.0.0.1:5500`

> ⚠️ **Note:** If running locally, update the API URL in `script.js` from the deployed backend URL to `http://127.0.0.1:8000/review`.

---

## 🔐 Environment Variables (`.env`)

Create a `.env` file inside the `backend` directory with the following content:

```env
# Groq API Key — get yours at https://console.groq.com/keys
GROQ_API_KEY=your_groq_api_key_here
```

> 🔒 Never commit your `.env` file to version control. It's already excluded via `.gitignore`.

---

## 🔄 API Workflow

### Endpoint: `POST /review`

**Request Body**

```json
{
  "code": "def add(a, b):\n    return a+b"
}
```

**Response Body**

```json
{
  "issues": [
    "Missing type hints for function parameters",
    "No docstring explaining function purpose"
  ],
  "suggestions": [
    "Add type annotations for better readability",
    "Add input validation for non-numeric types"
  ],
  "optimized_code": "def add(a: float, b: float) -> float:\n    \"\"\"Return the sum of two numbers.\"\"\"\n    return a + b"
}
```

**Internal Flow**

```
Client → POST /review → CodeInput (Pydantic validation)
       → get_review(code) → Groq Chat Completion (Llama 3.3 70B)
       → Parse "ISSUES / SUGGESTIONS / OPTIMIZED_CODE"
       → Return structured JSON → Client renders UI
```

**Error Handling**

- If the Groq API call fails → returns a fallback message (`"AI service unavailable"`).
- If the AI response can't be parsed into the expected format → returns the raw response inside `optimized_code` along with a `"Response parsing failed"` notice.

---

## 📂 Folder Structure

```
AI-Code-Review/
│
├── backend/
│   ├── __init__.py
│   ├── main.py            # FastAPI app & /review endpoint
│   ├── models.py          # Pydantic request models (CodeInput)
│   ├── reviewer.py         # Groq API integration & response parsing
│   └── .env                # Environment variables (not committed)
│
├── frontend/
│   ├── index.html          # Main UI structure
│   ├── style.css           # Styling
│   └── script.js           # API calls & DOM updates
│
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

---

## 🖼️ Screenshots

### 🏠 Home Page

<div align="center">

*[Add a screenshot of the home page UI here]*

`![Home Page](./screenshots/home-page.png)`

</div>

### 📊 Review Result

<div align="center">

*[Add a screenshot of the review results — issues, suggestions, and optimized code — here]*

`![Review Result](./screenshots/review-result.png)`

</div>

---

## 🔮 Future Improvements

- 🌍 **Multi-language Support** — Extend reviews beyond a single language to JavaScript, Java, C++, Go, and more
- 🔑 **Authentication** — User accounts to save preferences and personalize reviews
- 🕘 **Review History** — Store and revisit previously reviewed code snippets
- 📄 **PDF Export** — Download review reports as shareable PDFs
- 🔗 **GitHub Integration** — Review entire repositories or pull requests directly
- 🌈 **Syntax Highlighting** — Improve code readability with highlighted syntax in the editor and output
- 🌗 **Dark / Light Mode** — Theme toggle for better accessibility and user preference

---

## 🧩 Challenges & Learnings

Building this project came with several real-world engineering challenges:

- **Prompt Engineering for Structured Output** — Getting a free-form LLM to consistently return a parseable format (`ISSUES / SUGGESTIONS / OPTIMIZED_CODE`) required careful prompt design and iteration.
- **Robust Parsing** — Since LLM outputs aren't always perfectly consistent, the backend needed defensive parsing logic with graceful fallbacks to avoid breaking the UI.
- **API Reliability** — Handling Groq API errors gracefully (timeouts, rate limits, unavailability) without crashing the request flow.
- **Frontend-Backend Decoupling** — Designing a clean separation between a static frontend (Vercel) and a separately deployed Python API.
- **CORS Configuration** — Properly configuring CORS middleware in FastAPI to allow secure cross-origin requests from the deployed frontend.

These challenges reinforced practical skills in **API integration, prompt engineering, error handling, and full-stack deployment**.

---

## 💡 Why This Project

Code review is one of the most valuable — yet time-consuming — parts of software development. This project was built to explore:

- How **LLMs can augment developer productivity** by providing instant, on-demand feedback
- Practical, hands-on experience with **LLM API integration** (Groq + Llama 3.3)
- Designing a **simple, focused product** that solves a real problem without unnecessary complexity
- Building and deploying a complete **full-stack application** from scratch — frontend, backend, and AI layer working together

It's a small project with a big idea: **make quality code feedback accessible to everyone, instantly.**

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. **Fork** the repository
2. **Create** your feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes
   ```bash
   git commit -m "Add some amazing feature"
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open** a Pull Request

Please make sure to update tests and documentation as appropriate.

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it as you see fit. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

Have questions, feedback, or ideas? Feel free to reach out!

- 📧 **Email:** your.email@example.com
- 💼 **LinkedIn:** [linkedin.com/in/your-profile](https://linkedin.com)
- 🐙 **GitHub:** [github.com/your-username](https://github.com)

---

## 👨‍💻 Developer

<div align="center">

### **Prabhav Agrawal**

🎓 B.Tech, Computer Science & Applied Mathematics (CSAM)  
🏛️ Indraprastha Institute of Information Technology, Delhi (IIIT Delhi)

*Passionate about building AI-powered tools that make developers' lives easier.*

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/)

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

</div>
