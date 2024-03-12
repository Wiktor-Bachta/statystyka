#include <iostream>
#include <algorithm>

void insertionSort(int A[], int n, int &key_cmp, int &key_swp);

int main()
{
    FILE *fpt;
    fpt = fopen("./dane.csv", "w");
    fprintf(fpt, "n, key_cmp, key_swp\n");

    int k = 50;
    int N[100];

    for (int i = 0; i < 100; i++)
    {
        N[i] = 100 * (i + 1);
    }

    for (auto &n : N)
    {
        for (int i = 0; i < k; i++)
        {
            int array[n];
            for (int j = 0; j < n; j++)
            {
                array[j] = j + 1;
            }
            int key_cmp = 0;
            int key_swp = 0;

            std::random_shuffle(array, array + n);

            insertionSort(array, n, key_cmp, key_swp);

            fprintf(fpt, "%d, %d, %d\n", n, key_cmp, key_swp);
        }
        std::cout << "n = " << n << " done" << std::endl;
    }
    fclose(fpt);
}

void insertionSort(int A[], int n, int &key_cmp, int &key_swp)
{
    for (int j = 1; j < n; j++)
    {
        int key = A[j];
        int i = j - 1;

        key_cmp++;

        while (i >= 0 && A[i] > key)
        {
            key_cmp++;
            A[i + 1] = A[i];
            i = i - 1;
            key_swp++;
        }

        A[i + 1] = key;
    }
}