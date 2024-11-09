# image_sentiment_analyzer.py

import sys
import os
import torch
import torch.nn.functional as F
from torchvision import transforms
from torch import nn
import numpy as np
import cv2
import json

# Define emotion dictionary
emotion_dict = {
    0: "Angry",
    1: "Disgusted",
    2: "Fearful",
    3: "Happy",
    4: "Neutral",
    5: "Sad",
    6: "Surprised"
}

# Define the CNN model structure (should match your training model)
class EmotionCNN(nn.Module):
    def __init__(self):
        super(EmotionCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.conv4 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.dropout = nn.Dropout(0.25)
        self.fc1 = nn.Linear(128 * 6 * 6, 1024)
        self.fc2 = nn.Linear(1024, 7)
        self.fc_dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = self.dropout(x)
        
        x = F.relu(self.conv3(x))
        x = self.pool(x)
        x = F.relu(self.conv4(x))
        x = self.pool(x)
        x = self.dropout(x)

        x = x.view(-1, 128 * 6 * 6)
        x = F.relu(self.fc1(x))
        x = self.fc_dropout(x)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

def main():
    import warnings
    warnings.filterwarnings("ignore")
    
    # Read the image path from command line arguments
    if len(sys.argv) < 2:
        print("Error: No image file path provided.", file=sys.stderr)
        sys.exit(1)
    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(f"Script directory: {script_dir}", file=sys.stderr)
    print(f"Current working directory: {os.getcwd()}", file=sys.stderr)

    # Paths to model and Haar Cascade files
    model_path = os.path.join(script_dir, 'emotion_model.pth')
    cascade_path = os.path.join(script_dir, 'haarcascade_frontalface_default.xml')

    # Print paths for debugging
    print(f"Model path: {model_path}", file=sys.stderr)
    print(f"Cascade path: {cascade_path}", file=sys.stderr)

    # Check if Haar Cascade file exists
    if not os.path.isfile(cascade_path):
        print(f"Haar Cascade file not found at '{cascade_path}'", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"Haar Cascade file found at '{cascade_path}'", file=sys.stderr)

    # Load the trained model weights
    model = EmotionCNN()
    try:
        model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    except Exception as e:
        print(f"Error loading model from '{model_path}': {e}", file=sys.stderr)
        sys.exit(1)
    model.eval()  # Set model to evaluation mode

    # Define a transformation to match the input shape and preprocessing used during training
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Grayscale(),
        transforms.Resize((48, 48)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # Load the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading image: '{image_path}'", file=sys.stderr)
        sys.exit(1)

    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Face detector
    face_cascade = cv2.CascadeClassifier(cascade_path)
    if face_cascade.empty():
        print(f"Error loading Haar Cascade XML file from '{cascade_path}'", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"Haar Cascade loaded successfully from '{cascade_path}'", file=sys.stderr)

    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
    print(f"Number of faces detected: {len(faces)}", file=sys.stderr)

    results = []
    for (x, y, w, h) in faces:
        roi_gray_frame = gray_frame[y:y + h, x:x + w]
        try:
            cropped_img = cv2.resize(roi_gray_frame, (48, 48))
        except Exception as e:
            print(f"Error resizing face region: {e}", file=sys.stderr)
            continue

        # Apply transformations and add batch dimension
        input_tensor = transform(cropped_img).unsqueeze(0)

        # Make predictions
        with torch.no_grad():
            output = model(input_tensor)
            maxindex = int(output.argmax(dim=1))
            emotion = emotion_dict[maxindex]

        # Append the result along with face coordinates
        results.append({
            'emotion': emotion,
            'box': [int(x), int(y), int(w), int(h)]
        })

    # Output the results as JSON
    print(json.dumps(results))

if __name__ == "__main__":
    main()
