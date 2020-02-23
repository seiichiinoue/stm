import argparse, os, unicodedata
import MeCab

class Text(object):
    def __init__(self, path="./data/train/kokoro.txt"):
        self.wakati = MeCab.Tagger('-Owakati')
        self.chasen = MeCab.Tagger('-Ochasen')
        with open(path, "r", encoding="utf-8") as f:
            self.text = f.readlines()
        for i in range(len(self.text)):
            self.text[i] = self.text[i].replace("\n", "")

    def _is_japanese(self, text):
        for c in ['CJK UNIFIED', 'HIRAGANA', 'KATAKANA']:
            if c in unicodedata.name(text):
                return True
        return False

    def _wakati(self, path):
        # if self._is_japanese(self.text[0][0]):
        #     self._wakati_ja(path)
        # else:
        #     self._wakati_en(path)
        self._wakati_ja(path)
        
    def _wakati_ja(self, path):
        wakatied = []
        for i in range(len(self.text)):
            new_t = self.wakati.parse(self.text[i]).strip("\n")
            wakatied.append(new_t)
        with open(path, "w") as f:
            for t in wakatied:
                f.write(t+'\n')
        with open("./all.txt", "w") as f:
            for t in wakatied:
                f.write(t+"\n")
        return None
    
    def _wakati_en(self, path):
        wakatied = []
        for i in range(len(self.text)):
            new_t = self.text[i].split(" ").strip("\n")
            wakatied.append(new_t)
        with open(path, "w") as f:
            for t in wakatied:
                f.write(t+'\n')
        return None

    # 文節機能部の連結等の処理
    def revise(self, sentence):
        return 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='this script for text processing.')
    parser.add_argument('--tar_path', help='directory located raw file', default='./raw/')
    parser.add_argument('--save_path', help='directory save processed text', default='processed/')
    args = parser.parse_args()
    authors = os.listdir(args.tar_path)
    for author in authors:
        if not os.path.exists(args.save_path+author):
            os.mkdir(args.save_path+author)
        filelist = os.listdir(args.tar_path+author)
        for file in filelist:
            if file.endswith(".txt"):
                t = Text(args.tar_path+author+"/"+file)
                t._wakati(args.save_path+author+"/"+file)