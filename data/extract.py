import os, sys, random
import shutil

def extract_document(src_path="./processed/"):
    authors = os.listdir(src_path)
    for author in authors:
        filenames = os.listdir(src_path+author+"/")
        for fn in filenames:
            with open(src_path+author+"/"+fn) as f:
                if len(f.readlines()) < 10:
                    os.remove(src_path+author+"/"+fn)
        if len(os.listdir(src_path+author+"/")) == 0:
            shutil.rmtree(src_path+author+"/")

if __name__ == "__main__":
    extract_document()