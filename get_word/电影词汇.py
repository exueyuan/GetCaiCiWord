import requests, random, json, os, time, re
from bs4 import BeautifulSoup

def baocuncihui(file_name, all_word_list, num=10):
    with open("./{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")

def find_dianying(file_name):
    soup = BeautifulSoup(open(file_name, encoding='utf-8'), "html.parser")
    aList = soup.find_all("a", attrs={"class": "figure_title figure_title_two_row bold"})
    movie_list = []
    for tag in aList:
        movie: str = tag.string.strip()
        if '[' in movie and ']' in movie:
            num = movie.index('[')
            movie = movie[:num]
        if movie:
            movie_list.append(movie)
    random.shuffle(movie_list)
    return movie_list


if __name__ == "__main__":
    name = "电影1"
    file_name = name + ".html"
    movie_list = find_dianying(file_name)
    baocuncihui("../"+name, movie_list, 10)