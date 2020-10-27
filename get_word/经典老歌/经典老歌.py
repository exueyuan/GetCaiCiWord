import requests, random, json, os, time, re
from bs4 import BeautifulSoup

def baocuncihui(file_name, all_word_list, num=10):
    with open("./{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")

def find_word(file_name):
    soup = BeautifulSoup(open(file_name, encoding='utf-8'), "html.parser")
    word_list = []
    aList = soup.find_all("a", attrs={"target": "_1"})
    for tag in aList:
        word_list.append(tag.string)
    return word_list

if __name__ == "__main__":
    word_list = find_word("./经典老歌.html")
    print(word_list)
    baocuncihui("经典老歌", word_list)