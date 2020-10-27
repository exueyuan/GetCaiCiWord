import requests, random, json, os, time, re
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Referer": "https://www.gushiwen.org/"
}
qianzui_url = "https://www.gushiwen.org/"


def find_url(file_name):
    soup = BeautifulSoup(open(file_name, encoding='utf-8'), "html.parser")
    url_list = []
    tagList = soup.find_all("a")
    for tag in tagList:
        url_list.append(qianzui_url + tag.attrs['href'])
        # print(qianzui_url + tag.attrs['href'])
    return url_list

def get_shiju(url):
    r = requests.get(url, headers=headers)
    html_str = r.content.decode('utf-8')
    soup = BeautifulSoup(html_str, "html.parser")
    aTagList = soup.find_all("a", attrs={"href": re.compile("^https://so.gushiwen.org/mingju/")})
    word_list = []
    for tag in aTagList:
        if len(tag.string) > 3:
            print(tag.string)
            word_list.append(tag.string)
    return word_list

def baocuncihui(file_name, all_word_list, num=10):
    with open("./{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")



if __name__ == "__main__":
    url_list = find_url("诗词.html")
    all_word_list = []
    for url in url_list:
        word_list = get_shiju(url)
        all_word_list.extend(word_list)
    random.shuffle(all_word_list)
    all_word_list_ = list(set(all_word_list))
    baocuncihui("诗句", all_word_list_)


