#include <iostream>
#include <random>

int main()
{    
    std::random_device rand_dev;
    std::mt19937 generator(rand_dev());

    FILE *fpt;
    fpt = fopen("./dane.csv", "w");
    fprintf(fpt,"n,b,u,c,d,d - c\n");

    int k = 50;
    int N[100];

    for (int i = 0; i < 100; i++) {
        N[i] = 1000 * (i + 1);
    }

    for (auto& n : N) {
        std::uniform_int_distribution<int> distr(0, n - 1);
        for (int i = 0; i < k; i++) {
            int slots[n] = { 0 };
            int balls = 0;
            int b = 0;
            int u = 0;
            int c = 0;
            int d = 0;
            int empties = n;
            int ones = n; // ones = less than 2s
            while (true) {
                int r = distr(generator);
                balls += 1;
                slots[r] += 1;
                if (b == 0 && slots[r] == 2) {
                    b = balls;
                }
                if (balls == n) {
                    u = empties;
                }
                if (slots[r] == 1) {
                    empties -= 1;
                    if (empties == 0) {
                        c = balls;
                    }
                }
                else if (slots[r] == 2) {
                    ones -= 1;
                    if (ones == 0) {
                        d = balls;
                        break;
                    }
                }
            }
            fprintf(fpt,"%d,%d,%d,%d,%d,%d\n", n, b, u, c, d, (d - c));
        }
        std::cout << "n = " << n << " done" << std::endl;
    }
    fclose(fpt);
}