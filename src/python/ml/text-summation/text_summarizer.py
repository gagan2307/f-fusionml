# run_text_summarizer.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Specify the local directory where the model and tokenizer are saved
local_model_dir = "./local_text_summarizer_model"

# Load the tokenizer and model from the local directory
tokenizer = AutoTokenizer.from_pretrained(local_model_dir)
model = AutoModelForSeq2SeqLM.from_pretrained(local_model_dir)

# Input text to summarize
text = "Your input text goes here."

# Encode the input
inputs = tokenizer.encode(
    "summarize: " + text,
    return_tensors="pt",
    max_length=1024,
    truncation=True
)

# Generate the summary
summary_ids = model.generate(
    inputs,
    max_length=150,
    num_beams=4,
    early_stopping=True
)

# Decode and print the summary
summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

print("Summary:", summary)
