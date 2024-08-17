import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

# Check for GPU availability
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
print(f"Using device: {device}")
print(torch.cuda.is_available())


# Use a verified model ID
model_id = "openai/whisper-large-v3"

# Load the model
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True
)
model.to(device)

# Load the processor
processor = AutoProcessor.from_pretrained(model_id)

# Create the pipeline
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

input("----------")
# Provide the path to your audio file
audio_path = r"audio_2024-06-21_08-49-03.wav"

# Run the pipeline
result = pipe(audio_path)
print(result["text"])
print(result)
