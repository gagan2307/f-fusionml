# image_sentiment_analyser.py

from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image
import sys
import os

def load_model_and_processor(model_dir):
    """
    Load the image processor and model from the specified directory.
    """
    try:
        processor = AutoImageProcessor.from_pretrained(model_dir)
        model = AutoModelForImageClassification.from_pretrained(model_dir)
        return processor, model
    except Exception as e:
        print(f"Error loading model and processor: {e}", file=sys.stderr)
        sys.exit(1)

def preprocess_image(image_path, processor):
    """
    Load and preprocess the image.
    """
    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Error opening image: {e}", file=sys.stderr)
        sys.exit(1)
    inputs = processor(images=image, return_tensors="pt")
    return inputs

def predict_sentiment(inputs, model):
    """
    Perform prediction and return the predicted label.
    """
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        predicted_label = model.config.id2label[predicted_class_idx]
    return predicted_label

def main():
    # Read the image path from command line arguments
    if len(sys.argv) < 2:
        print("Error: No image file path provided.", file=sys.stderr)
        sys.exit(1)
    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Define the directory where the model and processor are saved
    model_dir = "./local_image_analyzer_model"

    try:
        processor, model = load_model_and_processor(model_dir)
        inputs = preprocess_image(image_path, processor)
        predicted_label = predict_sentiment(inputs, model)
        print(predicted_label)  # Output the predicted label to stdout
    except Exception as e:
        print(f"Error during prediction: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
