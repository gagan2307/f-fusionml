# image_captioner.py

from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from PIL import Image
import sys
import os

# Read the image path from stdin (for server communication)
image_path = sys.stdin.read().strip()

# Check if image path is provided
if not image_path:
    print("Error: No image file path provided.")
    sys.exit(1)

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' does not exist.")
    sys.exit(1)

# Specify the local directory where the model is saved
local_model_dir = "./blip_image_caption_model"

# Load the processor and model from the local directory
try:
    processor = BlipProcessor.from_pretrained(local_model_dir)
    model = BlipForConditionalGeneration.from_pretrained(local_model_dir)
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)

# Open the image
try:
    image = Image.open(image_path).convert('RGB')
except Exception as e:
    print(f"Error opening image: {e}")
    sys.exit(1)

# Prepare the inputs
inputs = processor(images=image, return_tensors="pt")

# Generate caption
try:
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=50, num_beams=5)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
except Exception as e:
    print(f"Error generating caption: {e}")
    sys.exit(1)

# Output the caption
print(caption)
