import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Load environment variables from .env file

openai.organization = os.getenv('OPENAI_ORGANIZATION')
openai.api_key = os.getenv('OPENAI_API_KEY')


def call_gpt(system_message, user_message):
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": system_message},
            {'role': 'user',
             'content': user_message}
        ]
    )