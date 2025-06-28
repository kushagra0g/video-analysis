import os
import logging
import datetime

# Use a local model for transcription
use_local_model = False

# Directory where transcripts will be stored
path_to_audio_files_directory = ""

# Only needed when use_local_model is enabled
path_to_local_model = ""

path_to_video_directory = ""

path_to_logging_directory = ""

# Show logs in console
show_logs_in_console = True

# Model for the analysis of the transcript.
analysis_model = "gpt-4.1-2025-04-14"

SUPPORTED_VIDEO_EXTENSIONS = [
    ".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv",
    ".webm", ".mpeg", ".mpg", ".m4v", ".3gp"
]

def logging_config():
    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%d-%m-%Y_%H-%M-%S")


    if not path_to_logging_directory:
        os.makedirs("logs", exist_ok=True)
        file_path = f"logs\\{timestamp}.log"
    else:
        file_path = os.path.join(path_to_logging_directory, f"{timestamp}.log")
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s-%(levelname)s-%(message)s",
                        datefmt="%d/%m/%Y %I:%M:%S %p",
                        filename=file_path,
                        filemode="w"
                        )

    # Show logs in console.
    if show_logs_in_console:
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter("%(levelname)s - %(message)s")
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)