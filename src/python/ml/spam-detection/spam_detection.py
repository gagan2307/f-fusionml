# spam_detection.py
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import sys

# Load the tokenizer and model from the local directory
local_model_dir = "./local_spam_model"
tokenizer = AutoTokenizer.from_pretrained(local_model_dir)
model = AutoModelForSequenceClassification.from_pretrained(local_model_dir)

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




# #OLD-----------------
# import torch
# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# # Load the tokenizer and model from the local directory
# local_model_dir = "./local_spam_model"
# tokenizer = AutoTokenizer.from_pretrained(local_model_dir)
# model = AutoModelForSequenceClassification.from_pretrained(local_model_dir)

# def make_prediction(input_text):
#     # Tokenize and encode the input text
#     inputs = tokenizer(input_text, return_tensors="pt")

#     # Make predictions
#     with torch.no_grad():
#         outputs = model(**inputs)
#         predictions = torch.argmax(outputs.logits, dim=-1)

#     # Interpret the results
#     if predictions[0] == 1:
#         return "The email is predicted to be spam."
#     else:
#         return "The email is predicted to be not spam."

# if __name__ == "__main__":
#     # Get input from the user
#     input_text = 'Hi i wanted to ask are you free tomorrow ?'

#     # Make the prediction and print the result
#     result = make_prediction(input_text)
#     print(result)
