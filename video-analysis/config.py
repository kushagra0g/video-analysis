import logging

# Use a local whisper model
use_local_model = True

# Directory where transcripts will be stored
path_to_audio_files_directory = ""

# Only needed if use_local_model is enabled
path_to_local_model = ""

path_to_video_directory = ""

path_to_logging_directory = ""

# Model for the analysis of the transcript.
analysis_model = "gpt-4.1-2025-04-14"

SUPPORTED_VIDEO_EXTENSIONS = [
    ".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv",
    ".webm", ".mpeg", ".mpg", ".m4v", ".3gp"
]

def logging_config():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s-%(levelname)s-%(message)s",
                        datefmt="%d/%m/%Y %I:%M:%S %p",
                        filename=path_to_logging_directory
                        )