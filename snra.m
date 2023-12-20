g_clean = imread('Fig5.07(a).jpg');
g = imread('Fig5.07(b).jpg');

% Print the input image 
[M,N] = size(g);
g = double(g);
g_clean = double(g_clean);
g_hat = zeros (M,N);

% Arithmetic Mean Filter
for x = 1:M
    for y = 1:N
        L_sum = 0;
        count = 0;
        for i = -1:1
            for j=-1:1
                x_index = max (1, min(M, x + i));
                y_index = max(1, min(N, y + j));
                L_sum = L_sum + g(x_index, y_index);
                count = count + 1;
            end
        end
        g_hat(x,y) = L_sum / count;
    end
end

% Calculate the SNR
SNR_noisy = 10*log10(sum(sum(g.^2))/sum(sum((g_clean - g).^2)));
SNR_denoised = 10*log10(sum(sum(g_hat.^2))/sum(sum((g_clean - g_hat).^2)));

% Print SNR
fprintf('The number of SNR before denoising: %.5f\n',SNR_noisy);
fprintf('The number of SNR after denoising by using Arithmetic mean filter: %.5f\n',SNR_denoised);