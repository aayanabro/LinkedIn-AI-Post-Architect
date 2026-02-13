# LinkedIn AI Post Architect

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-f55036?style=for-the-badge&logo=groq&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

**LinkedIn AI Post Architect** is a state-of-the-art content generation system that leverages **Few-Shot Learning** and **Llama 3.3-70B** to build viral personal brands. Unlike generic AI writers, this tool analyzes your unique writing style through historical data to ensure every post feels authentic and professional.

---

## Key Features

* **Few-Shot Learning Engine**: Retrieves relevant historical post examples to guide the LLM's writing style based on specific tags and lengths.
* **Intelligent Post Tagging**: Automatically extracts metadata including line counts, language (English/Hinglish), and topical tags from raw text.
* **Custom Glassmorphism UI**: A high-end Streamlit interface featuring transparent glass cards, modern typography, and LinkedIn-themed styling.
* **Tone & Length Control**: Fine-tune output with four distinct tones (Professional, Casual, Inspirational, Thought Leader) and three length categories.
* **Automated Data Ingestion**: A robust preprocessing pipeline that unifies disparate tags and enriches raw JSON data using AI.

---

## Technical Architecture

| Module | Responsibility |
| :--- | :--- |
| **`main.py`** | Streamlit application entry point and custom CSS-in-JS styling. |
| **`post_generator.py`** | Orchestrates prompt engineering and few-shot example injection. |
| **`few_shot.py`** | Manages data filtering logic to match posts by language, length, and topic. |
| **`llm_helper.py`** | Initializes the ChatGroq client using the Llama 3.3-70B model. |
| **`preprocess.py`** | Uses LangChain and JsonOutputParser to enrich raw post data with metadata. |

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/linkedin-post-architect.git](https://github.com/your-username/linkedin-post-architect.git)
cd linkedin-post-architect
