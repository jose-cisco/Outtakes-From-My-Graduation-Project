import os
import cv2
import numpy as np
import json
import shutil

# Define the directory containing the existing JPEG images
image_dir = 'D:/Random Geometry Image'

# Define the directory where you want to save the COCO dataset
output_dir = 'D:/Geometry Dataset'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define the path for the output COCO annotations file
annotations_file = os.path.join(output_dir, 'annotations.json')

# Initialize the COCO annotation dictionary
coco_annotations = {
    "info": {},
    "licenses": [],
    "images": [],
    "annotations": [],
    "categories": []
}

# Define the category labels if applicable
category_labels = ['rectangle', 'square', 'rhombus' ,'paralellogram','trapezoid','kite' ,'equilateral_triangle','acute triangle','obtuse triangle', 'right_triangle', 'isosceles_triangle','scalene triangle']  # Customize based on your dataset

# Iterate over each image in the directory
image_id = 1
for filename in os.listdir(image_dir):
    image_path = os.path.join(image_dir, filename)

    # Load and preprocess the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width, _ = image.shape

    # Save the image to the output directory
    output_image_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_image_path, image)

    # Add image information to the COCO annotation dictionary
    coco_annotations['images'].append({
        "id": image_id,
        "width": 256,
        "height": 256,
        "file_name": filename,
        "license": 0,  # Set the license ID if applicable
        "flickr_url": "",  # Add the image URL if applicable
        "coco_url": "",  # Add the image URL if applicable
        "date_captured": ""  # Add the image capture date if applicable
    })

    # Add annotation information to the COCO annotation dictionary
    # Customize this part based on your dataset and annotation requirements
    # If you don't have annotations, you can skip this step

    image_id += 1

# Save the annotations to a JSON file
with open(annotations_file, 'w') as f:
    json.dump(coco_annotations, f)

# Move the annotations file to the output directory
shutil.move(annotations_file, os.path.join(output_dir, 'annotations.json'))
