from moviepy import VideoFileClip
import logging
import os


def extract_audio(video_path, path_to_audio_file_directory):
    # Extracts audio from the provided video path, and returns the file path of the audio file.

    # Checking if the provided video path exists
    if not os.path.isfile(video_path):
        logging.warning(f"No video found at {video_path}")
        return None

    os.makedirs(path_to_audio_file_directory, exist_ok=True)
    video_name = os.path.basename(video_path)
    base_name = os.path.splitext(video_name)[0]
    file_path = os.path.join(path_to_audio_file_directory, base_name + ".wav")

    # Checking if audio already been extracted before, if yes then returning that filepath. Helps in saving resources.
    if os.path.exists(file_path):
        logging.info(f"Audio file already exists for the video {video_name}. Using the existing transcription to save resources.")
        return file_path

    logging.info(f"Extracting audio from {video_name}")
    video, audio = None, None

    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio is None:
            logging.warning(f"No audio track found in {video_name}")
            return None
        logging.info(f"Successfully extracted audio from  {video_name}.")

        # Writing the audio in the provided directory
        audio.write_audiofile(file_path, codec="pcm_s16le")
        logging.info(f"Wrote the audio file to the temp file")
        return file_path

    except Exception as e:
        logging.error(f"Failed to extract audio from {video_name}. Error : {e}")
        return None
    finally:
        if audio:
            audio.close()
        if video:
            video.close()