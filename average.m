% Read the input image f
f = imread('Fig5.26a.jpg');

% Print the input image f
imshow(f)
[M,N] = size(f);
f = double(f);

% Calculate the average value
avg = mean(f(:));

% Display the result
fprintf('Average value of the input image: %.5f\n', avg);
