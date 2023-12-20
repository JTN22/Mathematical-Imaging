% Read the input image f
f = imread('Fig5.26a.jpg');

% Print the input image f
imshow(f)
[M,N] = size(f);
f = double(f);
b = zeros(M,N);

% Use a for loop to shift the center
for i = 1:M
    for j = 1:N
        d = (-1)^((i-1) + (j-1));
        b(i,j) = f(i,j)*d;
    end
end

% Use command fft2 to perform discrete Fourier Transformation
F = fft2(b);

% Compute the spectrum
R = abs (F);

% Use log transformation, which is s = clog (I+r)
c = 5; % Set constant c = 5
S = zeros(M,N);

% Use for loop to run log transformation
for i = 1:M
    for j = 1:N
        S(i,j) = c*log (1 + R(i,j));
    end
end

% Print the Fourier Spectrum
S = uint8(S);
figure()
imshow(S)
