# scrape single documents
import os, sys
from bs4 import BeautifulSoup

def parse(path_to_html):
    print(path_to_html)
    with open(path_to_html, 'rb') as html:
        soup = BeautifulSoup(html)
    main_text = soup.find("div", class_='main_text')
    if soup.find("h1", class_="title") is None: return 
    if soup.find("h2", class_="author") is None: return
    if main_text is None: return

    title = soup.find("h1", class_="title").text
    author = soup.find("h2", class_="author").text
    title, author = title[:120], author[:120] # because 255 byte is limit of file name in linux
    for kana in main_text.find_all(["rp","h4","rt"]):
        kana.decompose()

    sentences = [line.strip() for line in main_text.text.strip().splitlines()]
    print(title, author)
    if not os.path.exists("./raw"):
        os.mkdir("./raw")
    save_dir = "./raw/{}/".format(author)

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    with open(save_dir+title+".txt", "w") as f:
        for sent in sentences:
            if sent == "\n": continue # 改行のみの行は無視
            f.write(sent+"\n")
    return

target = "./aozorabunko/cards/"
dirs = os.listdir(target)
for d in dirs:
    # print(d)
    if not os.path.exists(target+d+"/files"): continue
    l = os.listdir(target+d+"/files")
    l = [tmp for tmp in l if tmp.endswith(".html")]
    # print(l)
    for html in l:
        parse(target+d+"/files/"+html)

        


# print(sentences) 
