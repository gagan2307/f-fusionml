# image_sentiment_analyser.py

from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import torch
from PIL import Image
import sys
import os

def load_model_and_extractor(model_dir):
    """
    Load the feature extractor and model from the specified directory.
    """
    try:
        feature_extractor = AutoFeatureExtractor.from_pretrained(model_dir)
        model = AutoModelForImageClassification.from_pretrained(model_dir)
        return feature_extractor, model
    except Exception as e:
        print(f"Error loading model and extractor: {e}", file=sys.stderr)
        sys.exit(1)

def preprocess_image(image_path, feature_extractor):
    """
    Load and preprocess the image.
    """
    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Error opening image: {e}", file=sys.stderr)
        sys.exit(1)
    inputs = feature_extractor(images=image, return_tensors="pt")
    return inputs

def predict_sentiment(inputs, model, sentiment_mapping):
    """
    Perform prediction and map the result to a sentiment.
    """
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        predicted_label = model.config.id2label[predicted_class_idx]
        sentiment = sentiment_mapping.get(predicted_label.lower(), "Unknown")
    return sentiment

def main():
    # Read the image path from stdin
    image_path = sys.stdin.read().strip()

    if not image_path:
        print("Error: No image file path provided.", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Define the directory where the model and feature extractor are saved
    model_dir = "./local_image_analyzer_model"

    # Define the mapping from model labels to sentiments
    # Adjust this mapping based on your model's labels
    sentiment_mapping = {
        "happy": "Happy",
        "sad": "Sad",
        "angry": "Angry",
        "surprised": "Surprised",
        "neutral": "Neutral",
        # Add more mappings as needed
    }

    try:
        feature_extractor, model = load_model_and_extractor(model_dir)
        inputs = preprocess_image(image_path, feature_extractor)
        sentiment = predict_sentiment(inputs, model, sentiment_mapping)
        print(sentiment)  # Output the sentiment to stdout
    except Exception as e:
        print(f"Error during prediction: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
