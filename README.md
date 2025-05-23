# AI Code Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language](https://img.shields.io/badge/Language-Python-blue)]()
[![Build Status](https://img.shields.io/github/actions/workflow/status/sevvalasi/ai-codegen/python-app.yml)]()

---

## About the Project

AI Code Generator is an AI-powered application that automatically generates Python code using natural language-based instructions (prompts) received from the user and suggests topics. By integrating with modern LLM (Large Language Model) technologies, it aims to speed up and facilitate the code generation process of software developers.

---

## Features

- **Code Generation with Natural Language:** Generates Python code based on the user's comments.
- **Header Suggestion:** Generates meaningful headers suitable for the generated code.
- **Local LLM Support (Ollama):** It can work with locally running LLM models (e.g. `llama3`, `mistral`) that do not require an internet connection.
- **Web Interface:** Simple and user-friendly interface for interaction.
- **Easy Integration:** Easy to use in other projects with API and backend architecture.
- **Docker & Minikube Support:** Easy deployment in cloud environments and container-based platforms.

---

## Technologies

- Python 3.9+
- Flask (Web Framework)
- JavaScript, HTML, CSS (FrontEnd)
- Docker
- Kubernetes / Minikube (Deployment)
- Ollama (LLM Integration)

---

## Installation and Running

### Requirements

- Python 3.9 or higher
- Docker (Optional, for container use)
- [Ollama](https://ollama.com/) is an installed and working model (e.g. `llama3`, `mistral`, etc.) 

### Local Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sevvalasi/ai-codegen.git
   cd ai-codegen
   
2. Create and activate a virtual environment:

- On macOS/Linux:
  
   ```bash
   python3 -m venv venv
   source venv/bin/activate

- On Windows: 

    ```bash
    python -m venv venv
   .\venv\Scripts\activate

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Create the .env file and add the Ollama settings:

   ```bash
   # For use with ollama (for example)
   OLLAMA_MODEL=your_model_name
   OLLAMA_HOST=http://localhost:11434

5. Run the application:

   ```bash
   flask run

6. Go to http://localhost:5001 in a browser.


### Installation with Docker

1. Create a Docker Image:

   ```bash
   docker build -t ai-codegen .

2. Run Container (with the environment variables required for instantiation):

   ```bash
   docker run -p 5001:5001 \
   --env OLLAMA_MODEL=your_model_name \
   --env OLLAMA_HOST=http://host.docker.internal:11434 \
   ai-codegen

## Usage

* Write the desired Python code in natural language via the web interface.
* Click the “Generate” button to generate the code and title.
* You can copy the generated code and use it in your projects.

## Project Structure 

```plaintext
ai-codegen/
├── app.py                  # Flask application main file
├── templates/
│   └── index.html          # Home page template
├── requirements.txt       
├── Dockerfile              # Configuration for a Docker image
├── README.md               # Project description
