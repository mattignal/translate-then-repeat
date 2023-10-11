import os
from boto3 import Session
from pydub import AudioSegment
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import sys
from find_gender import find_gender
from voices import select_voice

# Load environment variables
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

# You may need to adjust the 'region_name' parameter as per your AWS
# configuration
session = Session(aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY,
                  region_name='us-east-1')
polly = session.client("polly")


def produce_speech(text, voice):
    try:
        # Request speech synthesis
        try:
            response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                               VoiceId=voice, Engine='neural')
        except:
            response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                               VoiceId=voice,
                                               Engine='standard')

    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output_loc = 'audio/speech.mp3'

            try:
                # Open a file for writing the output as a binary stream
                with open(output_loc, "wb") as file:
                    stream_read = stream.read()
                    if len(stream_read) > 5000:
                        file.write(stream_read)
                    else:
                        stream2 = stream_read + b'\xaa' * 5000
                        file.write(stream2)
                    output = AudioSegment.from_file(output_loc)
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    return output


def create_silent_audio(duration):
    return AudioSegment.silent(duration=duration)


def produce_translation_output(audio_portions, output):
    audio_portions += output
    audio_portions += create_silent_audio(1000)
    return audio_portions


def produce_original_output(audio_portions, output):
    audio_portions += create_silent_audio(len(output) + 2250)
    audio_portions += output
    audio_portions += create_silent_audio(len(output) + 1750)
    audio_portions += output
    audio_portions += create_silent_audio(len(output) + 1750)
    return audio_portions


def produce_audio(native_language, target_language, ordered_sentences):

    audio_portions = create_silent_audio(2000)

    if native_language == 'English':
        text = f"Translate the following text, then repeat after the speaker."
        NL_voice = select_voice(language=native_language, gender='Unsure')
        output = produce_speech(text, NL_voice)
        audio_portions += output
        audio_portions += create_silent_audio(2000)

    for _, sentence, translation, gender in ordered_sentences:

        gender = find_gender(target_language, sentence)
        NL_voice = select_voice(language=native_language, gender=gender)
        TL_voice = select_voice(language=target_language, gender=gender)

        output = produce_speech(translation, voice=NL_voice)
        audio_portions = produce_translation_output(audio_portions, output)

        output = produce_speech(sentence, voice=TL_voice)
        audio_portions = produce_original_output(audio_portions, output)

    if native_language == 'English':
        text = f"Exercise Complete."
        NL_voice = select_voice(language=native_language, gender='Unsure')
        output = produce_speech(text, NL_voice)
        audio_portions += output
    audio_portions += create_silent_audio(750)

    return audio_portions
