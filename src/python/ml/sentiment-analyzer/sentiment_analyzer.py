# sentiment_analyzer.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import sys

# Read input text from stdin
text = sys.stdin.read().strip()

# Handle empty input
if not text:
    print("Error: No input text provided.")
    sys.exit(1)

# Specify the local directory where the model is saved
local_model_dir = "./multilingual_sentiment_model"

# Load the tokenizer and model from the local directory
tokenizer = AutoTokenizer.from_pretrained(local_model_dir)
model = AutoModelForSequenceClassification.from_pretrained(local_model_dir)

# Encode the text
inputs = tokenizer.encode_plus(
    text,
    add_special_tokens=True,
    max_length=512,
    truncation=True,
    return_tensors='pt'
)

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# Get the predicted class
predicted_class = torch.argmax(logits, dim=1).item()

# Map predicted class to sentiment
# The labels for this model are: 0 - negative, 1 - neutral, 2 - positive
label_map = {0: 'positive', 1: 'neutral', 2: 'negative'}
sentiment = label_map.get(predicted_class, 'unknown')

# Output the sentiment result
print(sentiment)
