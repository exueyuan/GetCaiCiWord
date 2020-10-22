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
    ulList = soup.find_all("ul", attrs={"class": "clearfix listIcon2 col666"})
    for ultag in ulList:
        atagList = ultag.find_all("a")
        for tag in atagList:
            word = tag.string
            if word:
                word_list.append(word)
    random.shuffle(word_list)
    return word_list

def find_word_save(*name_list):
    all_word_list = []
    for name in name_list:
        file_name = name + ".html"
        word_list = find_word(file_name)
        all_word_list.extend(word_list)
    all_word_list = list(set(all_word_list))
    random.shuffle(all_word_list)
    baocuncihui("俗语", all_word_list, 10)

if __name__ == "__main__":
    find_word_save("俗语1", "俗语2", "俗语3")