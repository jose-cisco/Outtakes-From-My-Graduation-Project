% Set the parameters
numImages = 5000; % Total number of images
imageSize = 256; % Size of the image in pixels

% Specify the directory to save the images
saveFolder = 'D:/Random Geometry Image - JPEG';

for imageIdx = 1:numImages
    % Create a black background image
    background = zeros(imageSize, imageSize, 3, 'uint8');

    % Generate random shapes
    numShapes = randi([3, 5]); % Random number of shapes between 3 and 5
    shapes = cell(1, numShapes);
    centroids = zeros(numShapes, 2); % Store centroids of shapes
    minDistance = 30; % Minimum distance between shape centroids

    for i = 1:numShapes
        % Random shape type
        shapeType = randi([1, 7]); % 1: Triangle, 2: Square, 3: Rectangle, 4: Parallelogram, 5: Rhombus, 6: Trapezium, 7: Kite

        % Random shape size
        shapeSize = randi([10, 20]); % Random size between 10 and 20 pixels

        % Random shape color
        shapeColor = randi([0, 255], 1, 3, 'uint8'); % Random RGB color

        % Random shape position
        posX = randi([shapeSize, imageSize - shapeSize]);
        posY = randi([shapeSize, imageSize - shapeSize]);

        % Generate the shape based on the shape type
        switch shapeType
            case 1 % Equilateral Triangle
                triangleHeight = sqrt(3) * shapeSize / 2;
                shape = insertShape(background, 'FilledPolygon', [posX-shapeSize/2, posY+triangleHeight/3; posX+shapeSize/2, posY+triangleHeight/3; posX, posY-triangleHeight*2/3], 'Color', shapeColor);
            case 2 % Square
                shape = insertShape(background, 'FilledRectangle', [posX-shapeSize/2, posY-shapeSize/2, shapeSize, shapeSize], 'Color', shapeColor);
            case 3 % Rectangle
                shape = insertShape(background, 'FilledRectangle', [posX-shapeSize/2, posY-shapeSize/4, shapeSize, shapeSize/2], 'Color', shapeColor);
            case 4 % Parallelogram
                shape = insertShape(background, 'FilledPolygon', [posX-shapeSize/2, posY-shapeSize/4; posX+shapeSize/2, posY-shapeSize/4; posX+shapeSize/4, posY+shapeSize/4; posX-shapeSize/4, posY+shapeSize/4], 'Color', shapeColor);
            case 5 % Rhombus
                shape = insertShape(background, 'FilledPolygon', [posX-shapeSize/2, posY; posX, posY-shapeSize/2; posX+shapeSize/2, posY; posX, posY+shapeSize/2], 'Color', shapeColor);
            case 6 % Trapezium
                shape = insertShape(background, 'FilledPolygon', [posX-shapeSize/2, posY-shapeSize/4; posX+shapeSize/2, posY-shapeSize/4; posX+shapeSize/4, posY+shapeSize/4; posX-shapeSize/4, posY+shapeSize/4], 'Color', shapeColor);
            case 7 % Kite
                shape = insertShape(background, 'FilledPolygon', [posX, posY-shapeSize/2; posX+shapeSize/2, posY; posX, posY+shapeSize/2; posX-shapeSize/2, posY], 'Color', shapeColor);
        end

        shapes{i} = shape;
    end

    % Combine all shapes into one image
    combinedImage = background;
    for i = 1:numShapes
        combinedImage = imadd(combinedImage, shapes{i});
    end

    % Save the image with a unique filename
    timestamp = datestr(now, 'yyyymmdd_HHMMSS');
    filename = fullfile(saveFolder, ['generated_image_', timestamp, '_', num2str(imageIdx), '.jpg']);
    imwrite(combinedImage, filename);
end

% Display a success message
disp('All images generated and saved successfully!');
