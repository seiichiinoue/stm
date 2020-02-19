#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <malloc/malloc.h>
#include <vector>
#include <string>
#include <iostream>
#include <ostream>
using namespace std;

const long long max_size = 2000; // max length of strings
const long long N = 15;          // number of closest words that will be shown
const long long max_w = 50;      // max length of vocabulary entries

int ArgPos(char *str, int argc, char **argv) {
    int a;
    for (a = 1; a < argc; a++)
        if (!strcmp(str, argv[a])) {
            if (a == argc - 1) {
                printf("Argument missing for %s\n", str);
                exit(1);
            }
            return a;
        }
    return -1;
}

int main(int argc, char **argv) {
    // remove some unused variables
    // add some variables for stylistic and syntactic/semantic vectors
    FILE *f;
    char st1[max_size];
    char *bestw[N];
    char file_name[max_size], st[100][max_size];
    float dist, len, len1, len2, bestd[N], vec[max_size];
    long long words, size, a, b, c, d, cn, bi[100];
    long long sizes = -1, sized;
    float *M, *M1, *M2;
    char *vocab;
    // usage
    if (argc < 2) {
        printf("Usage:\n");
        printf("./distance_stylevec -load vec.bin\n");
        printf("\nOptions:\n");
        printf("\t-load <file>\n");
        printf("\t\t<file> contains word projections in the BINARY FORMAT\n");
        printf("\t-d <int>\n");
        printf("\t\tSet size of style vectors; default is half size of the whole vector\n\n");
        return 0;
    }
    int argi;
    if ((argi = ArgPos((char *)"-load", argc, argv)) > 0)
        strcpy(file_name, argv[argi + 1]);
    if ((argi = ArgPos((char *)"-d", argc, argv)) > 0)
        sizes = atoi(argv[argi + 1]);

    f = fopen(file_name, "rb");
    if (f == NULL) {
        printf("Input file not found\n");
        return -1;
    }
    fscanf(f, "%lld", &words);
    fscanf(f, "%lld", &size);

    /* size of stylistic (sizes) and syntactic/semantic (sized) vector */
    if (sizes == -1) {
        sizes = size / 2;
    }
    sized = size - sizes;

    vocab = (char *)malloc((long long)words * max_w * sizeof(char));
    for (a = 0; a < N; a++)
        bestw[a] = (char *)malloc(max_size * sizeof(char));
    M = (float *)malloc((long long)words * (long long)size * sizeof(float));
    M1 = (float *)malloc((long long)words * (long long)sizes * sizeof(float)); //stylistic
    M2 = (float *)malloc((long long)words * (long long)sized * sizeof(float)); //syntactic/semantic
    if (M == NULL) {
        printf("Cannot allocate memory: %lld MB    %lld  %lld\n", (long long)words * size * sizeof(float) / 1048576, words, size);
        return -1;
    }
    for (b = 0; b < words; b++) {
        a = 0;
        while (1) {
            vocab[b * max_w + a] = fgetc(f);
            if (feof(f) || (vocab[b * max_w + a] == ' '))
                break;
            if ((a < max_w) && (vocab[b * max_w + a] != '\n'))
                a++;
        }
        vocab[b * max_w + a] = 0;
        for (a = 0; a < size; a++) {
            fread(&M[a + b * size], sizeof(float), 1, f);
            if (a < sizes)
                M1[a + b * sizes] = M[a + b * size];
            else
                M2[(a - sizes) + b * sized] = M[a + b * size];
        }
    }
    fclose(f);
    printf("vocab size: %lld\n", words);
    // for (b=0; b<words; ++b) {
    //     printf("%s\n", &vocab[b * max_w]);
    // }
    
    /* convert array to vector */
    vector<string> vocab_list(words);
    vector<vector<double>> word_vec(words, vector<double>(size, 0));
    vector<vector<double>> semantic_vec(words, vector<double>(sized, 0));
    vector<vector<double>> stylistic_vec(words, vector<double>(sizes, 0));
    for (b=0; b<words; ++b) {
        // words
        string s = &vocab[b * max_w];
        vocab_list[b] = s;
        // word vector
        for (a=0; a<size; ++a) {
            double tmp = M[a+b+size];
            word_vec[b][a] = tmp;
            if (a < sizes) {
                double tmp1 = M1[a + b * sizes];
                stylistic_vec[b][a] = tmp1;
            } else {
                double tmp2 = M2[(a - sizes) + b * sized];
                semantic_vec[b][a-sizes] = tmp2;
            }
        }
    }
    cout << size << " " << sizes << " " << sized << endl;
}