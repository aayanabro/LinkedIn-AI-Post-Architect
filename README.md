# 貯 LinkedIn AI Post Architect

A high-performance content engine that uses **Few-Shot Learning** and **Llama 3.3** to craft viral LinkedIn posts tailored to your unique voice.

---

## 視 Core Features

* **Few-Shot Style Mimicry**: Analyzes your successful past posts to replicate your specific writing style.
* **Multi-Tone Selection**: Choose between Professional, Casual, Inspirational, or Thought Leader tones.
* **Bilingual Capability**: Full support for both **English** and **Hinglish** content generation.
* **Glassmorphism UI**: A modern, transparent "Glass Card" interface built with Streamlit.
* **Automated Metadata**: AI-powered extraction of tags and line counts from raw text.

---

## 懇 Technical Architecture

* **LLM**: Llama-3.3-70b via Groq API.
* **Orchestration**: LangChain for prompt templating and output parsing.
* **Data Logic**: Pandas-based filtering for few-shot example retrieval.
* **UI Framework**: Streamlit with custom CSS injections.

---

## 壺 Quick Start

### 1. Prerequisites
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_api_key_here
