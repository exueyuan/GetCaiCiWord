import requests, random, json, os, time, re
from bs4 import BeautifulSoup
"""
电影：
http://top.baidu.com/buzz?b=26&c=1&fr=topbuzz_b26_c1
电视剧：
http://top.baidu.com/buzz?b=4&c=2&fr=topcategory_c2
综艺：
http://top.baidu.com/buzz?b=19&c=3&fr=topcategory_c3
动漫：
http://top.baidu.com/buzz?b=23&c=5&fr=topcategory_c5
动画片：
http://top.baidu.com/buzz?b=1677&c=536&fr=topcategory_c536
纪录片：
http://top.baidu.com/buzz?b=1678&c=537&fr=topcategory_c537
小说：
http://top.baidu.com/buzz?b=7&fr=topbuzz_b1678_c537
网页游戏：
http://top.baidu.com/buzz?b=173&c=16&fr=topcategory_c16
网络游戏：
http://top.baidu.com/buzz?b=62&c=16&fr=topbuzz_b173_c16
手机游戏：
http://top.baidu.com/buzz?b=524&c=16&fr=topbuzz_b62_c16
单机游戏：
http://top.baidu.com/buzz?b=451&c=16&fr=topbuzz_b524_c16
"""
replace_prefix = "http://top.baidu.com"
word_tag_link_dict = {
    "电影":"http://top.baidu.com/buzz?b=26&c=1&fr=topbuzz_b26_c1",
    "电视剧":"http://top.baidu.com/buzz?b=4&c=2&fr=topcategory_c2",
    "综艺":"http://top.baidu.com/buzz?b=19&c=3&fr=topcategory_c3",
    "动漫":"http://top.baidu.com/buzz?b=23&c=5&fr=topcategory_c5",
    "动画片":"http://top.baidu.com/buzz?b=1677&c=536&fr=topcategory_c536",
    "纪录片":"http://top.baidu.com/buzz?b=1678&c=537&fr=topcategory_c537",
    "小说":"http://top.baidu.com/buzz?b=7&fr=topbuzz_b1678_c537"
}

youxi_dict = {
    "网页游戏":"http://top.baidu.com/buzz?b=173",
    "网络游戏":"http://top.baidu.com/buzz?b=62",
    "手机游戏":"http://top.baidu.com/buzz?b=524",
    "单机游戏":"http://top.baidu.com/buzz?b=451"
}

people_dict = {
    "热点人物":"http://top.baidu.com/buzz?b=258",
    "名家人物":"http://top.baidu.com/buzz?b=260",
    "公益人物":"http://top.baidu.com/buzz?b=612",
    "财经人物":"http://top.baidu.com/buzz?b=261",
    "体坛人物":"http://top.baidu.com/buzz?b=255",
    "主持人":"http://top.baidu.com/buzz?b=454",
    "历史人物":"http://top.baidu.com/buzz?b=259",
    "互联网人":"http://top.baidu.com/buzz?b=257",
    "女明星":"http://top.baidu.com/buzz?b=1570",
    "男明星":"http://top.baidu.com/buzz?b=1569",
    "欧美明星":"http://top.baidu.com/buzz?b=491"
}

car_dict = {
    "热搜汽车":"http://top.baidu.com/buzz?b=1540",
    "电动汽车":"http://top.baidu.com/buzz?b=1676",
    "微型车":"http://top.baidu.com/buzz?b=1543",
    "小型车":"http://top.baidu.com/buzz?b=1544",
    "紧凑车型":"http://top.baidu.com/buzz?b=1541",
    "中级车":"http://top.baidu.com/buzz?b=1545",
    "中高级车":"http://top.baidu.com/buzz?b=1546",
    "豪华车":"http://top.baidu.com/buzz?b=1548",
    "SUV":"http://top.baidu.com/buzz?b=1542",
    "MPV":"http://top.baidu.com/buzz?b=1549",
    "汽车月度":"http://top.baidu.com/buzz?b=1564"
}

shenghuo_dict = {
    "旅游城市":"http://top.baidu.com/buzz?b=302",
    "宠物":"http://top.baidu.com/buzz?b=24",
    "小吃":"http://top.baidu.com/buzz?b=1434",
    "畅销书":"http://top.baidu.com/buzz?b=450",
    "高校":"http://top.baidu.com/buzz?b=12",
    "化妆品":"http://top.baidu.com/buzz?b=1565",
    "奢侈品":"http://top.baidu.com/buzz?b=270",
    "慈善公益组..":"http://top.baidu.com/buzz?b=367"
}

keji_dict = {
    "手机":"http://top.baidu.com/buzz?b=1566",
    "软件":"http://top.baidu.com/buzz?b=1627",
}

lvyou_dict = {
    "岛屿":"http://top.baidu.com/buzz?b=1590",
    "国内景点":"http://top.baidu.com/buzz?b=1581",
    "国外景点":"http://top.baidu.com/buzz?b=1582",
    "中国名镇":"http://top.baidu.com/buzz?b=1591",
    "风景名胜":"http://top.baidu.com/buzz?b=14",
    "博物馆":"http://top.baidu.com/buzz?b=1579",
}


mulu_url = "http://top.baidu.com/boards?fr=topcategory_c513"

url = "http://top.baidu.com/buzz?b=26&c=1&fr=topbuzz_b26_c1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Referer": "http://top.baidu.com/buzz"
}

def baocuncihui(file_name, all_word_list, num=10):
    with open("./{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")

# 获取榜单链接
def get_mulu_list():
    r = requests.get(mulu_url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    aList = soup.find_all("a", attrs={"href": re.compile("^[.]/buzz[?]b=")})
    mulu_list = []
    for tag in aList:
        mulu_list.append(tag.string)
        print("\"{}\":\"{}\",".format(tag.string, str(tag.attrs['href']).replace(".", replace_prefix)))
    print(mulu_list)

def get_word_list(url):
    r = requests.get(url, headers=headers)
    # print(r.content)
    try:
        get_html = r.content.decode('gbk')
    except BaseException:
        get_html = r.content
    soup = BeautifulSoup(get_html, "html.parser")
    aList = soup.find_all("a", attrs={"class":"list-title"})
    word_list = []
    for tag in aList:
        word_list.append(tag.string)
    # print(html_str)
    return word_list

def get_save_dict_word(file_name, dict):
    all_word_list = []
    for url in dict.values():
        word_list = get_word_list(url)
        random.shuffle(word_list)
        all_word_list.extend(word_list)
    random.shuffle(all_word_list)
    baocuncihui(file_name,all_word_list)

def save_word_key_value(word_dict):
    for key, url in word_dict.items():
        word_list = get_word_list(url)
        random.shuffle(word_list)
        baocuncihui(key, word_list)


def get_word_from_dict():
    save_word_key_value(word_tag_link_dict)
    save_word_key_value(shenghuo_dict)
    get_save_dict_word("游戏", youxi_dict)
    get_save_dict_word("人物", people_dict)
    get_save_dict_word("汽车", car_dict)
    get_save_dict_word("科技", keji_dict)
    get_save_dict_word("旅游", lvyou_dict)


if __name__ == "__main__":
    # get_mulu_list()
    # print(get_word_list())
    get_word_from_dict()