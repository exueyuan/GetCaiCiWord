import requests, random, json, os, time, re
from bs4 import BeautifulSoup

def baocuncihui(file_name, all_word_list, num=10):
    with open("./{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")

def find_music(file_name):
    soup = BeautifulSoup(open(file_name, encoding='utf-8'), "html.parser")
    spanList = soup.find_all("span", attrs={"class": "song_name"})
    song_list = []
    for tag in spanList:
        song_name:str = tag.a.text
        if song_name:
            if " - " in song_name:
                song_name = song_name.split(" - ")[0]
            song_list.append(song_name)
    return song_list

if __name__ == "__main__":
    all_song_list = []
    song_list_1 = find_music("./好听的歌曲.html")
    song_list_2 = find_music("./2020新歌.html")
    song_list_3 = find_music("./流行歌曲.html")
    song_list_4 = find_music("./经典歌曲.html")
    song_list_5 = find_music("./网络歌曲.html")
    all_song_list.extend(song_list_1)
    all_song_list.extend(song_list_2)
    all_song_list.extend(song_list_3)
    all_song_list.extend(song_list_4)
    all_song_list.extend(song_list_5)
    all_song_list = list(set(all_song_list))
    random.shuffle(all_song_list)
    print(all_song_list)
    baocuncihui("音乐文件", all_song_list)