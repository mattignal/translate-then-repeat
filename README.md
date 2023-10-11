# Translate Then Repeat

Translate Then Repeat is a language learning tool that allows users to 
input words or expressions of their choice and receive an audio file to 
help with their speaking practice. The user will be prompted to translate and 
then repeat after the speaker several sentences containing variations of the 
input phrases. The prompts may be organized using a spaced repetition system 
(SRS) to optimize learning.

Given the generative nature of the sentences, this is a tool made for 
intermediate-to-advanced language learners.

## Prerequisites
* Make sure you have Python 3 installed.
* To use MP3s with pydub, you'll need to ensure you have ffmpeg or libav. These aren't Python packages, so you won't list them in requirements.txt, but you do need to install them on your system. Depending on your OS, the installation process may vary:
  * For MacOS (with Homebrew): `brew install ffmpeg`
  * For Ubuntu: `sudo apt-get update`, then `sudo apt-get install ffmpeg`
  * For Windows: You'd typically download binaries from the ffmpeg site.
  
## Setting Up
* First, clone or download this repository.

### Setup your Environment File
Create a .env file in the root directory and add your OpenAI and AWS credentials:

```
OPENAI_ORGANIZATION=<Your OpenAI Organization>
OPENAI_API_KEY=<Your OpenAI API Key>
AWS_ACCESS_KEY=<Your AWS Access Key>
AWS_SECRET_KEY=<Your AWS Secret Key>
```

For OpenAI credentials, you'll need to sign up with OpenAI and obtain the API key.

For AWS credentials:
* Log in to your AWS Management Console.
* Go to the IAM dashboard.
* Click on Users and then Add user.
* Set permissions for this user. To use Amazon Polly, the user needs 
  AmazonPollyFullAccess.

At the end of the creation process, AWS will provide an access key and a secret key. Keep these keys safe.

### Install the necessary Python libraries:

`pip install -r requirements.txt`

## How to Use
* Choose your Languages - Open voices.py to view the supported languages and 
  their voice variants. Choose the appropriate target language that you 
  wish to practice as well as your native language.
* You may need to adjust the `region_name` parameter as per your AWS 
  configuration in `create_audio.py` on line 18.
* Prepare your Word List - Create a Python list of words or expressions in 
  the desired target language. For example: `word_or_exp_list = ['está 
  hasta arriba', 'estar en las nubes', 'me cayó gordo']`.
  * [ChatGPT](https://chat.openai.com/) is a great way to generate 
    expressions in your target language. For example, a prompt like 
    `Generate 50 2-4 word commonly used n-grams in Spanish and place them in a 
    python list called 'word_or_exp_list'` should do the trick.
* Determine if you want `SRS=True` - This will shuffle the sentences 
  according to an SRS pattern. We recommend setting this to `False` for 
  verbs, and more helpful with longer lists.
* If you are using verbs and want to challenge yourself with different 
  tenses, set `verbs=True`.

Make sure to place the proper variables prior to the run_sentences call in 
the `if __name__ == __main__":`block and fill in the parameters with your 
desired values before executing.

### Run the Tool:

Execute the main script:

`python main.py`

#### Practice with the Generated Audio
You'll find the generated audio file in the audio directory. Listen to the 
audio, follow the prompts to translate, and then repeat after the speaker.

## Notes
* The system prefers Neural voices if available and chooses the gender based 
on the content of the sentence.
* For verbs, the generated sentences prioritize challenging tenses,
* If there's an error while generating sentences, the system will retry up 
  to 5 times before stopping.

## Potential Future Upgrades
* Add video option - this would allow users to follow along flash-card style
* Introduce the word before it pops up option
* Add sentences to document option