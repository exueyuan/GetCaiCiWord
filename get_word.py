import requests, random, json, os, time, re
# https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28204&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=词语&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=43230&rn=30&cb=jQuery110203961505524456099_1600140071363&_=1600140071373
# https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28204&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E8%AF%8D%E8%AF%AD&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=90&rn=30&cb=jQuery110203961505524456099_1600140071377&_=1600140071383
# https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28204&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=三字词语&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=190&rn=38&cb=jQuery110203961505524456099_1600140071377&_=1600140071392

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Referer": "https://www.baidu.com/s"
}

https = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28204&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query={}&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn={}&rn={}&cb=jQuery110203961505524456099_1600140071377&_=1600140071392"

def get_word(search_word, position, num):
    try:
        r = requests.get(https.format(search_word, position, num), headers=headers)
        get_json_str = r.content.decode('utf-8')
        regx = "\\((\\{.*\\})\\)"
        result = re.search(regx, get_json_str)
        json_str = result.group(1)
        word_dict = json.loads(json_str)
        list_num = word_dict["data"][0]["listNum"]
        word_link_list = word_dict["data"][0]["result"]
        word_list = []
        for word_link in word_link_list:
            word_list.append(word_link["ename"])
        return word_list, list_num
    except Exception as ex:
        return 0,[]

def get_all_word(search_word):
    start_position = 0
    search_num = 100
    all_word_list = []
    while True:
        word_list, _ = get_word(search_word, start_position, search_num)
        print(word_list)
        if not word_list:
            return all_word_list
        all_word_list.extend(word_list)
        start_position += search_num


def baocuncihui(search_word):
    with open("./{}.txt".format(search_word), "w", encoding="utf-8") as file:
        all_word_list = get_all_word(search_word)
        random.shuffle(all_word_list)
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // 30 + 1, position % 30 + 1, word))
            if (position+1) % 30 == 0:
                file.write("\n")

def get_all_ci():
    word_2_ci = get_all_word("二字词")
    word_2_ci = random.shuffle(word_2_ci)
    word_3_ci = get_all_word("三字词")
    word_3_ci = random.shuffle(word_3_ci)
    word_4_ci = get_all_word("四字词")
    word_4_ci = random.shuffle(word_4_ci)
    word_5_ci = get_all_word("五字词")
    word_5_ci = random.shuffle(word_5_ci)
    word_6_ci = get_all_word("六字词")
    word_6_ci = random.shuffle(word_6_ci)


if __name__ == "__main__":
    # baocuncihui("二字词")
    get_all_ci()