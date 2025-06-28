import logging
import os
from config import (use_local_model, path_to_local_model, path_to_audio_files_directory,
                    path_to_video_directory, analysis_model, logging_config, SUPPORTED_VIDEO_EXTENSIONS)
import ai
import video_to_audio

def main():

    # Loading the logging config.
    logging_config()

    # Analyses every video
    for filename in os.listdir(path_to_video_directory):

        # Checking if the file extension is supported.
        if not any(filename.lower().endswith(ext) for ext in SUPPORTED_VIDEO_EXTENSIONS):
            continue

        # extract_audio returns the extracted audio's path
        audio_path = video_to_audio.extract_audio(os.path.join(path_to_video_directory, filename), path_to_audio_files_directory)
        if use_local_model:
            transcription = ai.transcribe_local(path_to_local_model, audio_path)
        else:
            transcription = ai.transcribe(audio_path)

        # Analysing the transcript
        response = ai.analyse(transcription, analysis_model)
        if response is None:
            logging.error("No response received from analysis model.")
            return

        os.makedirs("outputs", exist_ok=True)
        with open(r"outputs/output.txt", "a", encoding="utf-8") as f:
            f.write("-------------------------------------------\n")
            f.write(f"Filename : {filename}\n")
            f.write("-------------------------------------------\n")
            f.write(f"Transcription : {transcription}\n")
            f.write("-------------------------------------------\n")
            f.write(f"Structured Response : {response.output_text}\n\n\n")

if __name__ == "__main__":
    main()