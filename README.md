# Local LLM Chat Assistant

A simple interactive Streamlit web application for interacting with a locally hosted Large Language Model using Ollama.

## Project Overview

This project demonstrates how a Streamlit frontend can communicate with a locally hosted LLM through the Ollama API.

Users can enter questions and receive AI-generated responses from the Llama 3.2 model running locally on the computer.

## Features

- Interactive Streamlit chat interface
- Local LLM inference using Ollama
- Llama 3.2 model support
- Conversation history
- Conversation memory
- Reset conversation button
- Ollama API integration
- Error handling
- No cloud API required

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- Requests
- REST API

## Architecture

User → Streamlit → Ollama API → Llama 3.2 → Response

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Local-LLM-Streamlit