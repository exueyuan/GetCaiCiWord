import requests, random, json, os, time, re
from bs4 import BeautifulSoup

# http://baike.baidu.com/fenlei/诗人?limit=30&index=1&offset=0
# http://baike.baidu.com/fenlei/%E8%AF%97%E4%BA%BA?limit=30&index=2&offset=30
# http://baike.baidu.com/fenlei/%E8%AF%97%E4%BA%BA?limit=30&index=3&offset=60
# http://baike.baidu.com/fenlei/%E8%AF%97%E4%BA%BA?limit=30&index=4&offset=90

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Referer": "http://baike.baidu.com/"
}

url = "http://baike.baidu.com/fenlei/{}?limit=30&index={}&offset={}"


def get_word(fenlei):
    word_list = []
    for index in range(1, 100):
        offset = (index-1)*30
        r = requests.get(url.format(fenlei, index, offset), headers=headers)
        html_str = r.content.decode('utf-8')
        soup = BeautifulSoup(html_str, "html.parser")
        divList = soup.find_all("div", attrs={"class":"list"})
        new_word_list = []
        for div in divList:
            aTagList = div.find_all("a", attrs={"href": re.compile("^/view/"), "target":"_blank", "class":re.compile("^nslog:")})
            word_list_temp = [item.text for item in aTagList]
            for word in word_list_temp:
                if word.strip() and len(word) > 1:
                    new_word_list.append(word)
        print(new_word_list)
        if new_word_list:
            word_list.extend(new_word_list)
        else:
            break
    return word_list

def write_to_file(fenlei):
    word_list = get_word(fenlei)
    word_str = ",".join(word_list)
    with open("../百科词汇.txt", "a", encoding="utf-8") as file:
        file.write(fenlei+"\n")
        file.write(word_str+"\n")
        file.write("\n")

if __name__ == "__main__":
    write_to_file("天文")
