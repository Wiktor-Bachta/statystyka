% Parametry
N_values = [100, 1000, 10000]; % różne wartości N
k = 5000; % liczba realizacji błądzenia losowego dla każdego N

% Inicjalizacja histogramów
figure;

% Pętla po różnych wartościach N
for i = 1:length(N_values)
    N = N_values(i);
    
    % Inicjalizacja wektora z frakcjami czasu
    PN_values = zeros(1, k);
    
    % Pętla po realizacjach błądzenia losowego
    for j = 1:k
        % Generowanie N kroków błądzenia losowego
        SN = cumsum(2 * (rand(1, N) > 0.5) - 1);
        
        % Wyznaczanie frakcji czasu PN
        Dn = SN > 0 | [0, SN(1:end-1)] > 0;
        LN = sum(Dn);
        PN_values(j) = LN / N;
    end
    
   % Tworzenie histogramu
    subplot(1, length(N_values), i);
    histogram(PN_values, 20, 'Normalization', 'pdf', 'EdgeColor', 'none','DisplayName', 'czas nad osią');
    hold on;
    
    % Gęstość rozkładu arcusa sinusa
    x_values = linspace(0, 1, 100);
    y_values = 1./(pi * sqrt(-(-1 + x_values) .* x_values));
    plot(x_values, y_values, 'r-', 'LineWidth', 2, 'DisplayName', 'arcus sinus z zad 5/7');
    
    title(['Histogram dla N = ', num2str(N)]);
    xlabel('Frakcja czasu P_N');
    ylabel('Gęstość prawdopodobieństwa');
    xlim([0, 1]);
    legend('show');
    hold off;
end
