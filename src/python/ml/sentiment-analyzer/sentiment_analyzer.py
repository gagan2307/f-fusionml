# run_multilingual_sentiment.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Specify the local directory where the model is saved
local_model_dir = "./multilingual_sentiment_model"

# Load the tokenizer and model from the local directory
tokenizer = AutoTokenizer.from_pretrained(local_model_dir)
model = AutoModelForSequenceClassification.from_pretrained(local_model_dir)

# Sample text for sentiment analysis (you can replace this with any text)
text = "I amnotin the moodright now"

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

print(f"Text: {text.strip()}")
print(f"Predicted sentiment: {sentiment}")
