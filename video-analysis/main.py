from app import ai
from app import local_ai
from app import video_to_audio
from app import logging_config
logging_config.logging_config()

audio_path = video_to_audio.extract_audio(video_path=r"C:\Users\kusagra\Desktop\zorcha\test_videos\v3.mp4")
transcription = local_ai.transcribe(aud_path=audio_path)
structured_response = ai.analyse(transcription)
print(structured_response.output_text)
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("-------------------------------------------\n")
    f.write(f"Transcription : {transcription}\n")
    f.write("-------------------------------------------\n")
    f.write(f"Structured Response : {structured_response.output_text}")