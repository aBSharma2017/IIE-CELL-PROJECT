# server.py
from flask import Flask, request
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def print_name():
    prompt = request.json.get('name')
    print("Prompt:", prompt)
    user_input = prompt + "/n Analyse the above text or string and choose out of list which suits the best or most close to(One word answer) [raiseLeftHand,raiseRightHand,raiseRightLeg,raiseLeftLeg, dance]"
    response = chat_gpt(user_input)
    print("Bot:", response)
    return "prompt received by Flask server"

if __name__ == '__main__':
    app.run(debug=True)
