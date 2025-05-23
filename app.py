import os
import re
import requests
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    generated_code = ""
    generated_title = ""

    if request.method == 'POST':
        prompt = request.form['prompt']  # Get the prompt from the user

        try:
            # Send the prompt to the local LLM using Ollama's API
            response = requests.post(
                'http://localhost:11434/v1/completions',
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "system": "You are an assistant that generates clean Python code and a meaningful title based on user prompts. First, write a short descriptive title, then a code block in triple backticks."
                }
            )
            response.raise_for_status()

            data = response.json()
            print("API Response:", data) 
            
            generated_output = data["choices"][0]["text"]

            # Extract title and code from the model output
            generated_title, generated_code = parse_output(generated_output)

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return render_template(
        'index.html',
        generated_code=generated_code,
        generated_title=generated_title,
    )

# Extract title and code from the model's output
def parse_output(output):
    try:
        # Extract code blocks enclosed in triple backticks
        code_blocks = re.findall(r"```(?:[a-zA-Z]+\n)?(.*?)```", output, re.DOTALL)
        code = code_blocks[0].strip() if code_blocks else "No code found."

        # Take the first non-code line as the title
        lines = output.strip().splitlines()
        title = next((line for line in lines if not line.strip().startswith("```") and line.strip()), "No title found.")

        return title.strip(), code
    except Exception as e:
        return "Error", "Failed to parse the output."

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
