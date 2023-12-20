% Read the input image 
image = imread('Fig5.07(b).jpg');

% Print the input image 
imshow(image)
[M,N] = size(image);
image = double(image);
image_hat = zeros(M,N);

% Geometric Mean Filter
for x = 1:M
    for y = 1:N
        L_sum = 1;
        count = 0;
        for i = -1:1
            for j = -1:1
                x_index = max(1, min(M, x + i));
                y_index = max(1, min(N, y + j));
                L_sum = L_sum * image(x_index, y_index);
                count = count + 1;
            end
        end
        image_hat (x,y) = (L_sum)^(1/count) ;
     end
end

% Print Geometric Mean Filter
figure()
image_hat = uint8(image_hat);
imshow(image_hat)
title('Geometric Mean Filter Image');