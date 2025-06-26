import os
from dotenv import load_dotenv
from openai import OpenAI
from .video_to_audio import extract_audio
import logging

load_dotenv()
client = OpenAI(api_key=os.getenv("openai_key"))

def transcribe(video_path):
    audio_path = extract_audio(video_path)
    print(audio_path)
    try:
        audio_file = open(audio_path, "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        return transcription.text
    except Exception as e:
        logging.critical(f" Could not transcribe the given audio.\n{e}")


def analyse(transcription, model = "gpt-4.1-2025-04-14"):
    prompt = ('Your job is to analyse this script of this influencer.'
              'Respond with a a JSON object using this format {"genre":"", "tags":"["","",...]", "analysis" : ""} '
              '"tags" should be a list of strings, they should be ordered, and what the video is related to. They should be ordered, first being what the video is most related and so on. Your job is to list 10 tags.'
              '"analysis" is what you understand of the transcript, of what is happening in it.'
              'Your response should be in English. Be concise'
              'Here is the transcript : '
              f'{transcription}')
    logging.info("Analysing the transcript...")
    try:
        response = client.responses.create(
            model=model,
            input=prompt
        )
        logging.info("Analysed the transcript.")
        return response
    except Exception as e:
        logging.error(f"Failed to generate a response. \nError : {e}")
        return None

if __name__=="__main__":
    transcribe(r"C:\Users\kusagra\Desktop\zorcha\test_videos\v1.mp4")