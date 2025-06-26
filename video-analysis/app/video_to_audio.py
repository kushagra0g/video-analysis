from moviepy import VideoFileClip
import logging
import os
from tempfile import NamedTemporaryFile
import base64

def audio_to_base64(video_path):
    if not os.path.isfile(video_path):
        logging.warning(f"No video found at {video_path}")
        return None
    video_name = os.path.basename(video_path)
    logging.info(f"Extracting audio from {video_name}")
    video, audio = None, None
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio is None:
            logging.warning(f"No audio track found in {video_name}")
            return None
        logging.info(f"Successfully extracted audio from  {video_name}.")
        base64_string = audiofileobject_to_base64(audio)
        return base64_string
    except Exception as e:
        logging.error(f"Failed to extract audio from {video_name}. Error : {e}")
        return None
    finally:
        if audio:
            audio.close()
        if video:
            video.close()

def audiofileobject_to_base64(aud):
    tmp = NamedTemporaryFile(delete=False, suffix=".wav")
    logging.info(f"Created a temporary file {tmp.name}")
    tmp.close()
    base64_string = ''
    # Writing the audio into a temp file so it can be converted into a base64 string
    try:
        aud.write_audiofile(tmp.name, codec="pcm_s16le")
        logging.info(f"Wrote the audio file to the temp file")
        with open(tmp.name, 'rb') as b:
            # Reading the audio in binary
            binary_data = b.read()
            logging.info(f"Extracted binary data from {tmp.name}")

            # Encoding the binary data into a base64 string
            base64_string = base64.b64encode(binary_data).decode('utf-8')
            logging.info("Successfully created the base64 string")
            return base64_string
    finally:
            try:
                os.remove(tmp.name)
                logging.info("Successfully deleted the temp file.")
            except OSError as e:
                logging.warning(f"Failed to remove the temp file {tmp.name}\nError : {e}")

def extract_audio(video_path):
    if not os.path.isfile(video_path):
        logging.warning(f"No video found at {video_path}")
        return None
    video_name = os.path.basename(video_path)
    logging.info(f"Extracting audio from {video_name}")
    video, audio = None, None
    temp = NamedTemporaryFile(suffix='.wav', delete=False)
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio is None:
            logging.warning(f"No audio track found in {video_name}")
            return None
        logging.info(f"Successfully extracted audio from  {video_name}.")
        audio.write_audiofile(temp.name, codec="pcm_s16le")
        logging.info(f"Wrote the audio file to the temp file")
        return temp.name

    except Exception as e:
        logging.error(f"Failed to extract audio from {video_name}. Error : {e}")
        return None
    finally:
        if audio:
            audio.close()
        if video:
            video.close()


if __name__ == "__main__":
    print(extract_audio(r"C:\Users\kusagra\Desktop\zorcha\test_videos\v4.mp4"))