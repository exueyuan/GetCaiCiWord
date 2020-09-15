import requests, random, json, os, time, re
from bs4 import BeautifulSoup
# https://www.lxybaike.com/index.php?category-view-13-151.html

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Referer": "https://www.lxybaike.com/index.php"
}

my_url = "https://www.lxybaike.com/index.php?category-view-13-{}.html"

def get_liuxingyu(num = 0):
    url = my_url.format(num)
    print("开始接受html")
    r = requests.get(url, headers=headers)
    html_str = r.content.decode('utf-8')
    print("已经接收到html")
    soup = BeautifulSoup(html_str, "html.parser")
    aTagList = soup.find_all("a", attrs={"href": re.compile("^index.php\\?doc-view-"), "class":"clink f20"})
    word_list = [item.string for item in aTagList]

    # 获取词汇摘要
    parent_tag_list = soup.find_all("dl", attrs={"class":"col-dl"})
    zhaiyao_list = []
    for item in parent_tag_list:
        p_tag = item.find_all("p")
        zhaiyao = p_tag[0].contents[0]
        zhaiyao_list.append(zhaiyao)
    return word_list, zhaiyao_list

def get_all_word(save_file_path):
    with open(save_file_path, "w", encoding="utf-8") as file:
        for i in range(100):
            word_list, zhaiyao_list = get_liuxingyu(i)
            position = 1
            for word,zhaiyao in zip(word_list,zhaiyao_list):
                write_content = "{}/{}.{}\n{}\n".format(i, position, word, zhaiyao[:min(20,len(zhaiyao))])
                print(write_content)
                file.write(write_content)
                position += 1
            file.write("\n")

if __name__ == "__main__":
    save_file_path = "./网络流程词汇.txt"
    get_all_word(save_file_path)