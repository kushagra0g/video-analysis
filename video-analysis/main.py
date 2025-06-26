import os
from config import (use_local_model, path_to_local_model,
                    path_to_video_directory, analysis_model, path_to_logging_directory)
import ai
import video_to_audio
import logging_config

logging_config.logging_config(path_to_logging_directory)
for filename in os.listdir(path_to_video_directory):
    audio_path = video_to_audio.extract_audio(filename)
    if use_local_model:
        transcription = ai.transcribe_local(path_to_local_model, audio_path)
    else:
        transcription = ai.transcribe(audio_path)

    response = ai.analyse(transcription, analysis_model)
    print(response.output_text)
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write("-------------------------------------------\n")
        f.write(f"Filename : {filename}\n")
        f.write("-------------------------------------------\n")
        f.write(f"Transcription : {transcription}\n")
        f.write("-------------------------------------------\n")
        f.write(f"Structured Response : {response.output_text}\n\n\n")