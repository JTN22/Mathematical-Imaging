% Input the image
image = imread('Fig5.26a.jpg');

% Print the input image
imshow(image)
[M, N] = size(image);
image = double(image);
A = 100;
u_0 = 134.4;
v_0 = 0;
n = zeros(M, N);

% Sinusoidal noise
for x = 1:M
    for y = 1:N
        n(x, y) = A*sin(2*pi*x*u_0 + 2*pi*y*v_0);
        image(x, y) = image(x, y) + n(x, y);
    end
end

image = uint8(image);

% Print degraged image
figure()
imshow(image)

% Shift and Fourier Transform
F = fft2(image);
F_shifted = fftshift(F);

% Compute the degraded image's spectrum
R = abs(F_shifted);
c = 5;
S = zeros(M, N);

for i = 1:M
    for j = 1:N
        S(i, j) = c*log(1 + R(i, j));
    end
end

figure()
imshow(S, []);
colormap(gray);
axis on;
title('Degraded Spectrum');

% Notch Filter
H_NR = ones(M, N);
n_centers = [129.2062, 27.1593; 129.2062, 79.0655; 129.2062, 180.4062; 128.8531, 230.5469];
rectangle_size = [5, 5];

for i = 1:size(n_centers, 1)
    u_k = n_centers(i, 1);
    v_k = n_centers(i, 2);
    rows = round(v_k - (rectangle_size(1) - 1)/2):round(v_k + (rectangle_size(1) - 1)/2);
    cols = round(u_k - (rectangle_size(1) - 1)/2):round(u_k + (rectangle_size(1) - 1)/2);
    rows(rows < 1 | rows > M) = [];
    cols(cols < 1 | cols > N) = [];
    H_NR(rows, cols) = 0;
    H_NR(M - rows + 1, N - cols + 1) = 0;
end

% Notch Filter
F_filter = F_shifted .* H_NR;

% Inverse Fourier Transform
image_filter = ifft2(ifftshift(F_filter));
image_filter = real(image_filter);

% Print Notch Image
figure()
imshow(uint8(image_filter));

% Compute filtered image's spectrum
R_filter = abs(fftshift(fft2(uint8(image_filter))));
S_filter = log(1 + R_filter);

figure()
imagesc(S_filter);
colormap(gray);
axis image;
title('Filtered Spectrum')
