import os, sys, random
import shutil

def extract_document(src_path="./processed/", tar_path = "./main/"):
    if not os.path.exists(tar_path):
        os.mkdir(tar_path)
    authors = os.listdir(src_path)
    for author in authors:
        filenames = os.listdir(src_path+author+"/")
        # rep = random.choice(filenames)
        for fn in filenames:
            with open(src_path+author+"/"+fn) as f:
                if len(f.readlines()) < 10:
                    continue
        # print(author.decode("utf-8", errors="ignore"))
        # print(rep.decode("utf-8", errors="ignore"))
            if not os.path.exists(tar_path+author+"/"):
                os.mkdir(tar_path+author+"/")
            shutil.copy(src_path+author+"/"+fn, tar_path+author+"/"+fn)

extract_document()
        