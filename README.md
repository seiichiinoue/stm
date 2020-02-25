# Modeling Text through Gaussian Process using Style-sensitive Word Vectors

## Environment

- Using Docker (docker must installed to local environment)

```
$ docker build -t wvtmenv .
$ docker run -it -v [local path]:/workspace/ wvtmenv
$ docker exec -it wvtm /bin/bash
```

## Prepare

### Corpus

- download aozorabunko data(git)

```
$ cd data/
$ git clone --branch master --depth 1 https://github.com/aozorabunko/aozorabunko.git
```

- parse to create cleansed data and process (wakati-gaki) cleansed data

```
$ python3 parse.py && python3 process.py
```

### Train Style2Vec

```
$ cd style2vec/
$ g++ style2vec.cpp -o style2vec -lm -pthread -O3 -march=native -Wall -Wextra -funroll-loops -Wno-unused-result
$ ./style2vec -train ../data/all.txt -output ../data/vec.bin
```

- My settings

```
SETTINGS={size:600, size-s:300, train:../data/all.txt, save-vocab:, read-vocab:, debug:2, binary:1, cbow:1, alpha:0.050000, output:../data/vec.bin, iwindow-threshold:5, fix-threshold:1, sample:0.001000, negative:5, threads:12, iter:10, min-count:5, classes:0}
Starting training using file ../data/all.txt
Vocab size: 202498
Words in train file: 304492532
```

## Train CSTM


## References

- [Mochihashi et al. (2013) Modeling Text through Gaussian Process](http://chasen.org/~daiti-m/paper/nl213cstm.pdf)
- [Akama et al. (2018) Learning Style-sensitive Word Vector via Unsupervised-manner](https://www.jstage.jst.go.jp/article/pjsai/JSAI2018/0/JSAI2018_1N203/_article/-char/ja/)
