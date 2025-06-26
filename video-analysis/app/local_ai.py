from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch

def transcribe(model_path=r"C:\Users\kusagra\Desktop\ai\whisper\whisper-large-v3-turbo", aud_path=""):
    try:
        if torch.cuda.is_available():
            device = "cuda"
        else:
            device = "cpu"
        print(device)
        torch_dtype = torch.float16 if device == "cuda" else torch.float32

        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_path, torch_dtype=torch_dtype, low_cpu_mem_usage=True
        ).to(device)

        processor = AutoProcessor.from_pretrained(model_path)

        pipe = pipeline(
            task="automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            chunk_length_s=30,
            torch_dtype=torch_dtype,
            device=device
        )

        result = pipe(aud_path)
        return result["text"]
    except Exception as E:
        print(f"Error occurred. \n{E}")
        return "Error"

if __name__ == "__main__":
    t = transcribe(aud_path=r"C:\Users\kusagra\AppData\Local\Temp\tmpspv5mc4q.wav")
    print(t)