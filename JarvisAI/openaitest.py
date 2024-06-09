# Todo: This code is definitely not working (BUG)
import os
from openai import OpenAI
from config import apikey

client = OpenAI(
    api_key=os.environ.get("Your api key"),  # apikey
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write an email to my boss about my resignation letter"}
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
