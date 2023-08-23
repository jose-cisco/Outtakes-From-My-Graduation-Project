import cv2
import numpy as np
import os
from random import randint

# Set the parameters
numImages = 500
imageSize = 256

# Specify the directory to save the images
saveFolder = 'D:\Random Geometry Image'
os.makedirs(saveFolder, exist_ok=True)

for imageIdx in range(1, numImages + 1):
    # Create a black background image
    background = np.zeros((imageSize, imageSize, 3), dtype=np.uint8)

    # Generate random shapes
    numShapes = randint(3, 5)
    shapes = []
    centroids = np.zeros((numShapes, 2))
    minDistance = 20
    maxDistance = 180

    for i in range(numShapes):
        # Random shape type
        shapeType = randint(1, 6)

        # Random shape size
        shapeSize = randint(10, 30)

        # Random shape color
        shapeColor = tuple(randint(0, 255) for _ in range(3))

        # Random shape position
        posX = randint(shapeSize, imageSize - shapeSize)
        posY = randint(shapeSize, imageSize - shapeSize)

        # Generate the shape based on the shape type
        if shapeType == 1:  # Equilateral Triangle
            triangleHeight = np.sqrt(3) * shapeSize / 2
            pts = np.array([[posX - shapeSize / 2, posY + triangleHeight / 3],
                            [posX + shapeSize / 2, posY + triangleHeight / 3],
                            [posX, posY - triangleHeight * 2 / 3]], np.int32)
            shape = cv2.fillPoly(background.copy(), [pts], shapeColor)
        elif shapeType == 2:  # Square
            pts = np.array([[posX - shapeSize / 2, posY - shapeSize / 2],
                            [posX + shapeSize / 2, posY - shapeSize / 2],
                            [posX + shapeSize / 2, posY + shapeSize / 2],
                            [posX - shapeSize / 2, posY + shapeSize / 2]], np.int32)
            shape = cv2.fillPoly(background.copy(), [pts], shapeColor)
        elif shapeType == 3:  # Rectangle
            pts = np.array([[posX - shapeSize / 2, posY - shapeSize / 4],
                            [posX + shapeSize / 2, posY - shapeSize / 4],
                            [posX + shapeSize / 2, posY + shapeSize / 4],
                            [posX - shapeSize / 2, posY + shapeSize / 4]], np.int32)
            shape = cv2.fillPoly(background.copy(), [pts], shapeColor)
        elif shapeType == 4:  # Diamond
            pts = np.array([[posX - shapeSize / 2, posY],
                            [posX, posY - shapeSize / 2],
                            [posX + shapeSize / 2, posY],
                            [posX, posY + shapeSize / 2]], np.int32)
            shape = cv2.fillPoly(background.copy(), [pts], shapeColor)
        elif shapeType == 5:  # Trapezium
            pts = np.array([[posX - shapeSize / 2, posY - shapeSize / 4],
                            [posX + shapeSize / 2, posY - shapeSize / 4],
                            [posX + shapeSize / 4, posY + shapeSize / 4],
                            [posX - shapeSize / 4, posY + shapeSize / 4]], np.int32)
            shape = cv2.fillPoly(background.copy(), [pts], shapeColor)
        elif shapeType == 6:  # Irrational Quadrilateral
            pts = np.array([[posX, posY - shapeSize / 2],
                            [posX + shapeSize / 2, posY],
                            [posX, posY + shapeSize / 2],
                            [posX - shapeSize / 2, posY]], np.int32)
            shape = cv2.fillPoly(background.copy(), [pts], shapeColor)

        shapes.append(shape)

    # Combine all shapes into one image
    combinedImage = background.copy()
    for shape in shapes:
        combinedImage = cv2.add(combinedImage, shape)
    # Save the image with a unique filename
    filename = os.path.join(saveFolder, f'random_shapes_{imageIdx}.jpeg')
    cv2.imwrite(filename, combinedImage)

# Display a success message
print('All images generated and saved successfully!')