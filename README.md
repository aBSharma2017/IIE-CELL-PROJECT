# IIE-CELL-PROJECT

 a simple Flask server application that leverages the OpenAI GPT-3.5 Turbo model to analyze text input and determine the most suitable action from a predefined list. The server accepts POST requests with JSON data and returns an analyzed response from the AI model.

## Features

- Flask Web Server: A lightweight web server built with Flask to handle incoming HTTP requests.
- OpenAI GPT-3.5 Turbo: Integration with the OpenAI API to utilize the powerful language model for text analysis.
- JSON Handling: Processes JSON payloads sent to the `/print` endpoint.
- Predefined Actions: The AI model selects the most suitable action from the list: `[raiseLeftHand, raiseRightHand, raiseRightLeg, raiseLeftLeg, dance]`.

## Prerequisites

- Python 3.6 or higher
- Flask
- OpenAI Python library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install flask openai
```

4. Set up OpenAI API Key:
   - Ensure you have an OpenAI API key. If you don't have one, you can get it from [OpenAI's website](https://openai.com/api/).
   - Replace the placeholder API key in the `server.py` file with your actual OpenAI API key.

## Usage

1. Run the Flask server:

```bash
python server.py
```

2. Send a POST request:
   - You can use tools like `curl` or Postman to send a POST request to the server.

Example using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/print -H "Content-Type: application/json" -d '{"name": "Your input text here"}'
```

## Code Explanation

- Initialization:
  - The `OpenAI` client is initialized with the API key.
  
- chat_gpt Function:
  - Takes a `prompt` as input, sends it to the OpenAI API, and returns the AI-generated response.
  
- Flask Application:
  - A single endpoint `/print` is defined to handle POST requests.
  - The input JSON is read, processed, and passed to the `chat_gpt` function.
  - The response from the AI model is printed to the console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README further based on your specific needs or preferences!
