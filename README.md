# Video Analysis
  
  This project extracts audio from videos, transcribes it via OpenAI Whisper (either through OpenAI API or locally). It then analyzes the transcript through another GPT API call.

  ## Usage :
1. Open `config.py` and set the following:
   - `path_to_video_directory`: path to the folder containing your videos.
   - `use_local_model`: set to `True` to use a local Whisper model, or `False` to use the OpenAI API.
   - `path_to_local_model`: path to the downloaded local Whisper model (if using locally).

   **Link to local model:** [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)

3. Create a `.env` file and add your OpenAI API key:
   ```env
   openai_key=your_api_key_here
