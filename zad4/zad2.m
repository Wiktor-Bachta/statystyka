% Parametry
N_values = [5, 10, 15, 20, 25, 30, 100]; % różne wartości N
Liczba_prob = 10000; % liczba prób dla każdego N

% Inicjalizacja wykresów
figure;

% Pętla po różnych wartościach N
for i = 1:length(N_values)
    N = N_values(i);
    
    % Generowanie N zmiennych losowych Xn i obliczanie sumy SN
    SN = zeros(1, Liczba_prob);
    for j = 1:Liczba_prob
        Xn = 2 * (rand(1, N) > 0.5) - 1;
        SN(j) = sum(Xn);
    end
    
    % Oblicz dystrybuantę empiryczną
    [f_emp, x_emp] = ecdf(SN);
    
    % Oblicz dystrybuantę rozkładu normalnego (aproksymacja)
    mu = 0; % średnia rozkładu normalnego
    sigma = sqrt(N); % odchylenie standardowe dla sumy N zmiennych losowych
    f_norm = normcdf(x_emp, mu, sigma);
    
    % Tworzenie wykresu schodkowego dystrybuanty empirycznej i rozkładu normalnego
    subplot(2, 4, i);
    stairs(x_emp, f_emp, 'LineWidth', 1.5, 'DisplayName', 'Empiryczna');
    hold on;
    plot(x_emp, f_norm, 'r--', 'LineWidth', 1.5, 'DisplayName', 'Normalny');
    hold off;
    title(['N = ', num2str(N)]);
    xlabel('Wartość');
    ylabel('Dystrybuanta');
    legend('show');
    xlim([-N, N]);
end
