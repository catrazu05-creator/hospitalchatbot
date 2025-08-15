from openai import OpenAI

client= OpenAI(
    api_key="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"
    base_url="https://api.groq.com/openai/vl"
)
while True:
    user_input= input("you:")
    if user_input == "quit" :
        print("bot: Goodbye!")
        break
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        message=[
            {"role": "system","content": "you are a medical bot, provide information only relate"}
            {"role": "user", "content": user_input}
        ]
    )
    print("bot:, ", response.choices[0].message.content)
    