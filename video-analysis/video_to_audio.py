from moviepy import VideoFileClip
import logging
import os
from tempfile import NamedTemporaryFile

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
    print(extract_audio(r"/test_videos/v4.mp4"))