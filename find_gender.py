import time
import gpt_calls


def find_gender(language, sentence):
    system_message = f"""You are a {language} speaker who determines the 
most likely gender of the speaker of a given sentence. You must return 
one word. Do not use quotation marks or punctuation. Your response must 
be one of the following: 

Male
Female
Unsure"""

    user_message = f"""What is the most likely gender of the speaker of the 
following sentence?: '{sentence}'"""

    tries = 0
    while tries < 5:
        try:
            response = gpt_calls.call_gpt(system_message, user_message)
            return response['choices'][0]['message']['content']
        except Exception as e:
            tries += 1
            print(f"Error occurred: {e}. Retry {tries} of 5.")
            time.sleep(30)
        if tries == 5:
            raise RuntimeError('Failed to produce text after 5 attempts')
