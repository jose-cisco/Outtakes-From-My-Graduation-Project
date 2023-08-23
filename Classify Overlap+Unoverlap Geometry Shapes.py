import os
import cv2
import numpy as np
import shutil
from PIL import Image
import torch
from torchvision import models, transforms

# Define the list of models to use for classification
models_list = [
    models.resnet152(pretrained=True),
    models.resnext101_64x4d(pretrained=True)
]

# Move the models to the GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
models_list = [model.to(device) for model in models_list]

# Load the pre-trained models
for model in models_list:
    model.eval()

# Define the transformations for the input image
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Function to classify an image using multiple models and move it to the corresponding directory
def classify_and_move_image(image_path, models):
    # Load and preprocess the image
    image = Image.open(image_path).convert('RGB')
    input_tensor = preprocess(image)
    input_tensor = input_tensor.to(device)
    input_batch = input_tensor.unsqueeze(0)

    # Classify the image using each model
    predicted_labels = []
    for model in models:
        with torch.no_grad():
            output = model(input_batch)
        _, predicted_idx = torch.max(output, 1)
        predicted_labels.append(predicted_idx.item())

    # Determine if the image overlaps or not
    non_overlaps = image_not_overlap(image_path)

    # Create the directory if it doesn't exist
    if non_overlaps:
        output_dir = 'D:/No_Overlap'
    else:
        output_dir = 'D:/Overlap'
    os.makedirs(output_dir, exist_ok=True)

    # Move the image to the output directory
    image_filename = os.path.basename(image_path)
    output_path = os.path.join(output_dir, image_filename)
    shutil.move(image_path, output_path)

# Function to check if an image has overlap
def image_not_overlap(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Convert the grayscale image to a NumPy array
    image_array = np.array(grayscale_image)

    # Apply binary thresholding to segment the image
    _, binary_image = cv2.threshold(image_array, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contours are detected
    non_overlap = len(contours) > 0

    # Close the images
    image.close()
    grayscale_image.close()

    return non_overlap
    

# Path to the directory containing the images
input_dir = 'D:/Random Geometry Image'

# Process each image in the input directory
for filename in os.listdir(input_dir):
    image_path = os.path.join(input_dir, filename)
    classify_and_move_image(image_path, models_list)

