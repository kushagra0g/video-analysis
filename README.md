**Video Analysis**
  
  This project extracts audio from videos, transcribes it using OpenAI Whisper (either through OpenAI API or locally). Then it analyzes the transcript through another GPT API call.

  *Usage :*

  in config.py, put the path to the directory containing the videos you want to analyse. You can set the variable use_local_model to switch between using a local Whisper model or the OpenAI
  API.
  Create a .env file and put your OpenAI API key.

  To transcribe using the local model, here is the link to the Whisper model. https://huggingface.co/openai/whisper-large-v3
  After downloading the model, put the path of the directory in config.py
