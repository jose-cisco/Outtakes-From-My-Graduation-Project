i=imread('random_shapes_11.png');
j=imgaussfilt(i,2);
k=imnoise(j,'gaussian',0,0.01);
% Display the original and processed images
figure;
subplot(1, 3, 1);
imshow(i);
title('Original Image');
subplot(1, 3, 2);
imshow(j);
title('Gaussian Blur');
subplot(1, 3, 3);
imshow(k);
title('Gaussian Blur + Gaussian Noise');