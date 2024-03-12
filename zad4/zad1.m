% Parameters of the binomial distribution
n = 100;  % Number of trials
p = 0.5; % Probability of success

% Generate values for the random variable (number of successes)
x = n*p*1.2:n;

% Calculate the probability mass function (PMF) using binopdf
pmf = binopdf(x, n, p);

disp(num2str(sum(pmf)));
