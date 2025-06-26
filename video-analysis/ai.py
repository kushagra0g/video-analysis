from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch
import os
from dotenv import load_dotenv
from openai import OpenAI
import logging

def transcribe_local(model_path, aud_path):
    try:
        if torch.cuda.is_available():
            device = "cuda"
        else:
            device = "cpu"
        torch_dtype = torch.float16 if device == "cuda" else torch.float32
        try:
            model = AutoModelForSpeechSeq2Seq.from_pretrained(
                model_path, torch_dtype=torch_dtype, low_cpu_mem_usage=True
            ).to(device)
        except (OSError, ValueError) as e:
            logging.error("Failed to load model.")
            logging.error(str(e))
            return None
        try:
            processor = AutoProcessor.from_pretrained(model_path)
        except (OSError, ValueError) as e:
            logging.error("Failed to load processor.")
            logging.error(str(e))
            return None

        pipe = pipeline(
            task="automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            chunk_length_s=30,
            torch_dtype=torch_dtype,
            device=device
        )
        logging.info("Transcribing the audio file using local Whisper")
        result = pipe(aud_path)
        return result["text"]

    except OSError:
        logging.error("Invalid model path or model files missing.")
    except ValueError:
        logging.error("Model files are either corrupted or incompatible")
    except Exception as E:
        logging.error("Error occurred while trying to generate transcription using the local model.")
        logging.error(str(E))
        return None

# Transcribing using the OpenAI api.
def transcribe(audio_path):
    load_dotenv()
    client = OpenAI(api_key=os.getenv("openai_key"))
    try:
        audio_file = open(audio_path, "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        return transcription.text

    except Exception as e:
        logging.error(f"Error occurred while trying to fetch a response from the OpenAI API.")
        logging.error(f"Error : {e}")

# Analyse the transcript.
def analyse(transcription, model):
    load_dotenv()
    client = OpenAI(api_key=os.getenv("openai_key"))
    if transcription is None:
        logging.error("Failed to analyse transcription.")
        return None
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
        logging.info("Successfully analysed the transcript.")
        return response
    except Exception as e:
        logging.error(f"Failed to generate a response. \nError : {e}")
        return None