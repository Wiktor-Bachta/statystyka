#include <iostream>
#include <random>

int main()
{    
    std::random_device rand_dev;
    std::mt19937 generator(rand_dev());

    FILE *fpt;
    fpt = fopen("./dane.csv", "w");
    fprintf(fpt,"n, max\n");

    int k = 50;
    int N[100];

    for (int i = 0; i < 100; i++) {
        N[i] = 10000 * (i + 1);
    }

    for (auto& n : N) {
        std::uniform_int_distribution<int> distr(0, n - 1);
        for (int i = 0; i < k; i++) {
            int slots[n] = { 0 };
            int balls = 0;
            int max = 0;
            while (true) {
                int r1 = distr(generator);
                int r2 = distr(generator);
                balls += 1;
                if (slots[r1] > slots[r2]) {
                    slots[r2] += 1;
                }
                else {
                    slots[r1] += 1;
                }
                if (balls == n) {
                    break;
                }
            }
            for (int j = 0; j < n; j++) {
                if (slots[j] > max) {
                    max = slots[j];
                }
            }
            fprintf(fpt,"%d, %d\n", n, max);
        }
        std::cout << "n = " << n << " done" << std::endl;
    }
    fclose(fpt);
}