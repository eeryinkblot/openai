from openai import OpenAI
client = OpenAI()

messages=[
    {"role": "system", "content": "Du bist der beste Programmierer der Welt der sich hervorragend mit Java auskennt."},
]

def callGPT(messages):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message.content

while True:
    messages.append({"role": "user", "content": input("User: ")})
    message = callGPT(messages)
    print(f"Assistant: {message}")
    messages.append({"role": "assistant", "content": message})