myFolder = 'D:\Pre_Data_Image';
save_folder = 'D:\CAPTCHA_Processing_01';

% Get a list of all files in the folder with the desired file name pattern.
filePattern = fullfile(myFolder, '*.jpg'); % Change to whatever pattern you need.
theFiles = dir(filePattern);
for k = 1 : length(theFiles)
    baseFileName = theFiles(k).name;
    fullFileName = fullfile(theFiles(k).folder, baseFileName);
    fprintf(1, 'Now processing %s\n', fullFileName);
    
    % Now do whatever you want with this file name,
    % such as reading it in as an image array with imread()
    imageArray = imread(fullFileName);
    
    % Apply minimum variance quantization with color quantization
    numColors = 64; % Define the number of colors for quantization
    [indexedImage, colorMap] = rgb2ind(imageArray, numColors, 'nodither');
    
    % Convert indexed image back to RGB
    quantizedImage = ind2rgb(indexedImage, colorMap);
    
    % Apply Gaussian filter with size 7
    filteredImage = imgaussfilt(quantizedImage, 7);
    
    % Apply Gaussian blur with sigma 3
    blurredImage = imgaussfilt(filteredImage, 3);
    
    % Apply Gaussian noise with standard deviation 3
    noisyImage = imnoise(blurredImage, 'gaussian', 0, 3^2);
    
    % Apply Poisson noise with lambda 3
    poissonNoisyImage = imnoise(noisyImage, 'poisson');
    
    % Apply salt and pepper noise with density 0.05
    saltAndPepperNoisyImage = imnoise(poissonNoisyImage, 'salt & pepper', 0.05);
    
    % Save the processed image to the save_folder
    [~, name, ext] = fileparts(baseFileName);
    processedFileName = sprintf('%s_processed%s', name, ext);
    processedFilePath = fullfile(save_folder, processedFileName);
    imwrite(quantizedImage,processedFilePath);
    imwrite(filteredImage,processedFilePath);
    imwrite(blurredImage,processedFilePath);
    imwrite(noisyImage,processedFilePath);
    imwrite(poissonNoisyImage,processedFilePath)
    imwrite(saltAndPepperNoisyImage, processedFilePath);
end

% Display message when all files are processed
fprintf('All files processed successfully!\n');

