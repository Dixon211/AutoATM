import openai
from dotenv import load_dotenv
import os 

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = "org-I0lUrNr7ZGbRrz5zE5WGS9vf"

messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]
while True:
	message = input("User : ")
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="babbage", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})
