# AI Lead Qualification & Smart Response System

An AI-powered lead processing system that automatically classifies incoming customer leads and generates professional responses using Large Language Models (LLMs).

Built using:

* FastAPI
* Groq API
* Llama 3
* Streamlit
* SQLite
* Docker

---

# Problem Statement

Businesses receive different kinds of incoming customer messages every day, such as:

* pricing inquiries
* support requests
* demo requests
* partnership opportunities
* spam messages

Manually handling and categorizing these leads takes time and reduces response efficiency.

The goal of this project is to build a simple and scalable AI-powered system that can:

1. Understand incoming lead messages
2. Classify them into categories
3. Generate contextual professional responses
4. Store processed results
5. Handle failures gracefully

This project focuses more on practical AI engineering and system design rather than training custom machine learning models.

---

# Project Goals

The main goals of this assignment were:

* Build a modular AI pipeline
* Integrate an LLM into a backend service
* Design scalable and maintainable architecture
* Add fallback handling
* Create a working frontend demo
* Containerize the application using Docker

---

# System Architecture

```text
Streamlit UI
      ↓
FastAPI Backend
      ↓
Input Validation
      ↓
Lead Classification (LLM)
      ↓
Response Generation (LLM)
      ↓
SQLite Database
```

---

# Workflow

## Step 1 — User Submits Lead

Example:

```text
"I want pricing details for your AI automation service."
```

---

## Step 2 — Lead Classification

The backend sends the message to the LLM using a constrained prompt.

Possible categories:

* sales
* support
* partnership
* spam
* general

Example output:

```text
sales
```

---

## Step 3 — Response Generation

Another prompt generates a professional AI response based on:

* lead category
* user message

Example response:

```text
"Thank you for your interest in our AI solutions..."
```

---

## Step 4 — Store Result

The system stores:

* original message
* classified category
* generated response
* processing status

inside the SQLite database.

---

# Why I Chose This Architecture

I intentionally kept the architecture simple and modular instead of overengineering the solution.

The assignment specifically mentioned focusing on practical and scalable thinking, so I prioritized:

* maintainability
* readability
* modularity
* simplicity

instead of adding unnecessary complexity.

---

# Tech Stack

| Technology | Purpose               |
| ---------- | --------------------- |
| FastAPI    | Backend API framework |
| Groq API   | LLM inference         |
| Llama 3    | Language model        |
| Streamlit  | Frontend demo UI      |
| SQLite     | Database              |
| SQLAlchemy | ORM                   |
| Docker     | Containerization      |

---

# Why Groq?

I selected Groq because:

* it provided very fast inference
* easy experimentation
* reliable free-tier access
* simple API integration

---

# Why Prompt-Based Classification?

Instead of training a custom classifier model, I used prompt-based classification because:

* faster development
* more flexible
* simpler architecture
* enough for assignment scope

This also reduced the need for training data and model fine-tuning.

---

# Project Structure

```text
ai-lead-system/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── prompts/
│   ├── schemas/
│   └── services/
│
├── streamlit_app/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env
```

---

# API Endpoint

## POST `/process-lead`

### Input

```json
{
  "message": "I need pricing details for enterprise AI solutions."
}
```

---

### Output

```json
{
  "category": "sales",
  "response": "Thank you for your interest in our AI solutions...",
  "status": "success"
}
```

---

# Prompt Engineering

## Classification Prompt

The classification prompt restricts outputs to predefined categories only.

This helps:

* reduce hallucinations
* improve consistency
* simplify downstream processing

---

## Response Generation Prompt

The response prompt focuses on:

* concise replies
* professional tone
* contextual responses
* avoiding fake promises

---

# Error Handling & Fallbacks

I added fallback handling for situations such as:

* API failures
* invalid model outputs
* empty inputs
* timeout issues

Example fallback response:

```text
"Thank you for contacting us. Our team will reach out shortly."
```

This ensures the system fails gracefully instead of crashing completely.

---

# Streamlit Frontend

I added a Streamlit frontend to make the system easier to test and demo visually.

The frontend allows users to:

* submit lead messages
* view lead category
* view generated AI responses
* check processing status

---

# Docker Support

The project is containerized using Docker.

This helps:

* maintain consistent environments
* simplify deployment
* improve reproducibility

---

# Local Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd ai-lead-system
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Add Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

---

# Running FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Running Streamlit Frontend

```bash
streamlit run streamlit_app/app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# Docker Run

## Build Docker Image

```bash
docker build -t ai-lead-system .
```

---

## Run Container

```bash
docker run -p 8000:8000 ai-lead-system
```

---

# Deployment

Backend deployed on Render. 

https://ai-lead-system-xh0u.onrender.com


Frontend :

https://aileadsystem-fwzfsffokotsh4tvh4vj9m.streamlit.app/

The Streamlit frontend communicates with the deployed backend API.



---

# Future Improvements

If given more time, I would improve:

* PostgreSQL integration
* Redis queues
* retry mechanisms
* confidence scoring
* authentication
* monitoring dashboards
* human review workflow
* analytics dashboard

---

# Key Learnings

Through this project, I learned:

* practical LLM integration
* prompt engineering
* API design
* modular architecture
* frontend-backend integration
* Docker-based deployment
* fallback handling strategies
* production-oriented AI system thinking

---

# Final Thoughts

This project was focused on building a practical AI engineering solution instead of creating an overly complex system.

The goal was to design something:

* understandable
* modular
* maintainable
* scalable
* and easy to extend later.

Thank you for checking out the project.
