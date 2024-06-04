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

if __name__ == "__main__":
    while True:
        user_input = input("You: ") + "/n Analyse the above text or string and choose out of list which suits the best or most close to(One word answer) [raiseLeftHand, raiseRightHand, raiseRightLeg, raiseLeftLeg, dance]"
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_gpt(user_input)
        print("Bot:", response)