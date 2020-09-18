import requests, random, json, os, time, re
from bs4 import BeautifulSoup
# https://node.video.qq.com/x/api/float_vinfo2?callback=jQuery191006699335478044044_1600356282590&cid=k0u5qlva0ot526i&_=1600356282637

# url = "https://node.video.qq.com/x/api/float_vinfo2?callback=jQuery191006699335478044044_1600356282590&cid=k0u5qlva0ot526i&_=1600356282637"
# url = "https://v.qq.com/x/bu/pagesheet/list?_all=1&append=1&channel=tv&listpage=2&offset=30&pagesize=30&sort=16"

url = "https://v.qq.com/x/bu/pagesheet/list?_all=1&append=1&channel=variety&listpage=2&offset={}&pagesize={}&sort=4"
url2 = "https://v.qq.com/x/bu/pagesheet/list?_all=1&append=1&channel=variety&listpage=2&offset=150&pagesize=30&sort=4"
url3_dianshiju = "https://v.qq.com/x/bu/pagesheet/list?_all=1&append=1&channel=tv&listpage=2&offset={}&pagesize={}&sort=16"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Referer": "https://v.qq.com/channel/variety?"
}
html = """
<!doctype html>
<html lang="zh-cn" dir="ltr">
<head>
    <meta charset="utf-8" />
</head>
<body>
{}
</body>
</html>
"""



def baocuncihui(file_name, all_word_list, num=10):
    with open("../{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")

def find_dianying(offset, pagesize = 30):
    r = requests.get(url3_dianshiju.format(offset, pagesize), headers=headers)
    get_html = r.content.decode('utf-8')
    html_str = html.format(get_html)
    soup = BeautifulSoup(html_str, "html.parser")
    aList = soup.find_all("a", attrs={"class":"figure_title figure_title_two_row bold"})
    zongyi_list = []
    for tag in aList:
        zongyi_list.append(tag.string)
    # print(html_str)
    return zongyi_list

def find_all_zongyi():
    offset = 0
    pagesize = 30
    all_zongyi_list = []
    while offset < 2000:
        zongyi_list = find_dianying(offset, pagesize)
        print(zongyi_list)
        if not zongyi_list:
            break
        all_zongyi_list.extend(zongyi_list)
        offset += pagesize
    print(all_zongyi_list)
    random.shuffle(all_zongyi_list)
    baocuncihui("电视剧2", all_zongyi_list)

find_all_zongyi()