import time
import gpt_calls


def generate_sentences(language, word_or_exp, n=10, verbs=False):
    if verbs:
        system_message = f"""You are a {language} speaker who creates 
short, but natural sentences containing the requested verb. Instead of using 
the infinitive form, focus on challenging tenses in the past, future, 
imperative, and especially the subjunctive. Each sentence should be no more 
than 8 words. After each sentence, you will then translate it to English, 
placing the translation in parentheses. Ensure that: 

1) The sentences are natural and conversational.
2) The translations are accurate.
3) Lines will take the form '1. Sentence (Translation)'"""

    else:
        system_message = f"""You are a {language} speaker who creates short, 
but natural sentences containing the requested word or expression. If it is a 
multi-word expression, you may play around with its different forms. Each 
sentence should be no more than 8 words. After each sentence, you will then 
translate it to English, placing the translation in parentheses. Ensure that:

1) The sentences are natural and conversational.
2) The translations are accurate.
3) Lines will take the form '1. Sentence (Translation)'"""

    user_message = f"""Write {n} different {language} sentences making use of 
    the phrase '{word_or_exp}'."""

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