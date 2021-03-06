# Style-Sensitive Continuous Space Topic Model

## Environment

- Using Docker (docker must installed to local environment)

```
$ docker build -t cstmenv .
$ docker run -it -v [local path]:/workspace/ cstmenv
$ docker exec -it [container id] /bin/bash
```

## Prepare

### Corpus

- prepare data
    - for SGNS training: need to organize dataset in sentence-base unit
    - for topic modeling: need to organize dataset in document-base unit
- train validation split
- locate data for training at `train/` and data for validation at `validation/`.
- train SGNS with training dataset.
- pass these location as a parameter to trainer(CSTMTrainer).

### Train Style2Vec

```
$ make prepare
$ cd bin/ && ./style2vec -size 40 -size-s 20 -train ../data/all.txt -output ./vec_dim20.bin
```

- My settings

```
SETTINGS={size:40, size-s:20, train:../data/all.txt, save-vocab:, read-vocab:, debug:2, binary:1, cbow:1, alpha:0.050000, output:../bin/vec_dim20.bin, iwindow-threshold:5, fix-threshold:1, sample:0.001000, negative:5, threads:12, iter:10, min-count:5, classes:0}
Starting training using file ../data/all.txt
Vocab size: 202498
Words in train file: 304492532
```

## Train CSTM

```
$ make
$ cd bin/ && ./cstm -ndim_d=20 -ignore_word_count=4 -epoch=100 -num_threads=1 -data_path=../train/ -validation_data_path=../validation/ -vec_path=./vec_dim20.bin -model_path=./cstm.model
```

- `ndim_d` must be same to dimention size of pre-trained word vector
- `ignore_count` must be same to ignore count in pre-training

## Visualize Result

### Distance between words

```
$ make distance
$ cd bin && ./distance -load ./vec_dim20.bin
```

### Distance between documents [WIP]

```
$ make install
$ python3
>>> import pycstm
>>> cstm = pycstm.cstm("./bin/cstm.model")
```

## References

- [Mochihashi et al. (2013) Modeling Text through Gaussian Process](http://chasen.org/~daiti-m/paper/nl213cstm.pdf)
- [Akama et al. (2018) Learning Style-sensitive Word Vector via Unsupervised-manner](https://www.jstage.jst.go.jp/article/pjsai/JSAI2018/0/JSAI2018_1N203/_article/-char/ja/)
