import cv2
import numpy as np
import os
from random import randint

# Set the parameters
numImages = 500
imageSize = 256
overlap_percentage = 0.1  # Adjust the overlap percentage as needed

# Specify the directory to save the images
saveFolder = 'D:/Overlap 2D Shape 10 Percent'
os.makedirs(saveFolder, exist_ok=True)

# Loop through image generation
for imageIdx in range(1, numImages + 1):
    # Create a black background image
    background = np.zeros((imageSize, imageSize, 3), dtype=np.uint8)

    # Generate random shapes
    numShapes = randint(3, 5)
    shapes = []

    # Loop through shape generation
    for i in range(numShapes):
        # Random shape type
        shapeType = randint(1, 6)

        # Random shape size
        shapeSize = randint(40, 60)

        # Random shape color
        shapeColor = tuple(randint(0, 255) for _ in range(3))

        # Generate the shape based on the shape type
        shape_img = np.zeros((imageSize, imageSize, 3), dtype=np.uint8)

        if shapeType == 1:  # Equilateral Triangle
            triangleHeight = np.sqrt(3) * shapeSize / 2
            pts = np.array([[posX - shapeSize / 2, posY + triangleHeight / 3],
                            [posX + shapeSize / 2, posY + triangleHeight / 3],
                            [posX, posY - triangleHeight * 2 / 3]], np.int32)
            shape_img = cv2.fillPoly(shape_img, [pts], shapeColor)
        elif shapeType == 2:  # Square
            pts = np.array([[posX - shapeSize / 2, posY - shapeSize / 2],
                            [posX + shapeSize / 2, posY - shapeSize / 2],
                            [posX + shapeSize / 2, posY + shapeSize / 2],
                            [posX - shapeSize / 2, posY + shapeSize / 2]], np.int32)
            shape_img = cv2.fillPoly(shape_img, [pts], shapeColor)
        elif shapeType == 3:  # Rectangle
            pts = np.array([[posX - shapeSize / 2, posY - shapeSize / 4],
                            [posX + shapeSize / 2, posY - shapeSize / 4],
                            [posX + shapeSize / 2, posY + shapeSize / 4],
                            [posX - shapeSize / 2, posY + shapeSize / 4]], np.int32)
            shape_img = cv2.fillPoly(shape_img, [pts], shapeColor)
        elif shapeType == 4:  # Diamond
            pts = np.array([[posX - shapeSize / 2, posY],
                            [posX, posY - shapeSize / 2],
                            [posX + shapeSize / 2, posY],
                            [posX, posY + shapeSize / 2]], np.int32)
            shape_img = cv2.fillPoly(shape_img, [pts], shapeColor)
        elif shapeType == 5:  # Trapezium
            pts = np.array([[posX + shapeSize / 2, posY + shapeSize / 4],
                            [posX - shapeSize / 2, posY + shapeSize / 4],
                            [posX - shapeSize / 4, posY - shapeSize / 4],
                            [posX + shapeSize / 4, posY - shapeSize / 4]], np.int32)
            shape_img = cv2.fillPoly(shape_img, [pts], shapeColor)
        elif shapeType == 6:  # Irrational Quadrilateral
            pts = np.array([[posX, posY - shapeSize / 2],
                            [posX + shapeSize / 2, posY],
                            [posX, posY + shapeSize / 2],
                            [posX - shapeSize / 2, posY]], np.int32)
            shape_img = cv2.fillPoly(shape_img, [pts], shapeColor)

        # Add the new shape to the list
        shapes.append(shape_img)

# Loop over images
for imageIdx in range(1, numImages + 1):
    # Create a black background image
    background = np.zeros((imageSize, imageSize, 3), dtype=np.uint8)

    # Generate random shapes
    numShapes = randint(3, 5)
    shapeSize = randint(40, 60)
    shapes = []

    for i in range(numShapes):
        # Generate random shape type and color
        shapeType = randint(1, 6)
        shapeColor = tuple(randint(0, 255) for _ in range(3))

        # Get a new position for the shape that does not overlap with existing shapes
        position = get_new_position(shapeSize, shapes, imageSize)

        # Generate the shape and add it to the list
        shape = generate_shape(shapeType, position, shapeSize, shapeColor)
        shapes.append((position[0], position[1], shapeSize, shapeSize))

        # Add the shape to the background image
        background[position[1]:position[1] + shapeSize, position[0]:position[0] + shapeSize] = shape

    # Save the image with a unique filename
    filename = os.path.join(saveFolder, f'random_shapes_{imageIdx}.jpeg')
    cv2.imwrite(filename, background)

# Display a success message
print('All images generated and saved successfully!')
