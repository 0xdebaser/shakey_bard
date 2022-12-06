import os
from dotenv import load_dotenv
import openai

load_dotenv()
key = os.getenv("OPENAI_API_KEY")


def shake_it(text):
	prompt = f"Rewrite the following in the style of William Shakespeare: {text}"
	print(prompt)
	openai.api_key = key
	response = openai.Completion.create(
		model="text-davinci-003",
		prompt=prompt,
		max_tokens=250,
		temperature=0.7
	)
	print(response)
	return response
