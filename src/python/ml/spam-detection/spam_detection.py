# spam_detection.py
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import sys

# Load the tokenizer and model from the local directory
local_model_dir = "./local_spam_model"
tokenizer = AutoTokenizer.from_pretrained(local_model_dir)
model = AutoModelForSequenceClassification.from_pretrained(local_model_dir)

accessToken = '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'

def make_prediction(input_text):
    # Tokenize and encode the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)

    # Interpret the results
    if predictions[0] == 1:
        return "spam"
    else:
        return "not spam"

if __name__ == "__main__":
    # Read input text from stdin
    input_text = sys.stdin.read()

    # Make the prediction and print the result
    result = make_prediction(input_text)
    print(result)



# API-VERSION-----------------
# # src/python/ml/spam-detection/spam_detection.py
# import requests
# import sys
# import os

# def make_prediction(input_text, api_token):
#     # Use the publicly available spam detection model
#     api_url = "https://api-inference.huggingface.co/models/mrm8488/bert-tiny-finetuned-sms-spam-detection"

#     headers = {
#         "Authorization": f"Bearer {api_token}"
#     }

#     payload = {
#         "inputs": input_text
#     }

#     response = requests.post(api_url, headers=headers, json=payload)
#     response.raise_for_status()  # Raise an exception for HTTP errors

#     # The response is a list of dictionaries
#     predictions = response.json()

#     if not predictions:
#         return "No prediction returned."

#     # The model returns a list of dictionaries with 'label' and 'score'
#     # We will use the label with the highest score
#     prediction = predictions[0]
#     label = prediction.get('label', 'Unknown')

#     if label == 'spam' or label == 'LABEL_1':
#         return "spam"
#     elif label == 'ham' or label == 'LABEL_0':
#         return "not spam"
#     else:
#         return f"Unknown prediction: {label}"

# if __name__ == "__main__":
#     # Read input text from stdin
#     input_text = sys.stdin.read().strip()

#     # Get the API token from environment variable
#     api_token = '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'

#     if not api_token:
#         print("Error: Hugging Face API token not found. Please set the HF_API_TOKEN environment variable.")
#         sys.exit(1)

#     # Make the prediction and print the result
#     try:
#         result = make_prediction(input_text, api_token)
#         print(result)
#     except Exception as e:
#         print(f"Error during prediction: {e}")
#         sys.exit(1)

