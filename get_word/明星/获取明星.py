import requests, random, json, os, time, re
from bs4 import BeautifulSoup
# https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28266&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=明星&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=24&rn=12&cb=jQuery110201995055402859678_1600423833192&_=1600423833314

# https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28266&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=明星&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=48&rn=12&cb=jQuery110201995055402859678_1600423833192&_=1600423833317

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Referer": "https://www.baidu.com/s"
}

uri = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28266&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=明星&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn={}&rn={}&cb=jQuery110201995055402859678_1600423833192&_=1600423833317"

def baocuncihui(file_name, all_word_list, num=10):
    with open("./{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")

def get_word(position, num):
    try:
        r = requests.get(uri.format(position, num), headers=headers)
        get_json_str = r.content.decode('utf-8')
        regx = "\\((\\{.*\\})\\)"
        result = re.search(regx, get_json_str)
        json_str = result.group(1)
        word_dict = json.loads(json_str)
        result_list = word_dict['data'][0]['result']
        word_list = []
        for result in result_list:
            word_list.append(result['ename'])
        return word_list
    except Exception as ex:
        return []

def get_all_ci():
    position = 0
    num = 100
    all_word_list = []
    for _ in range(100):
        word_list = get_word(position, num)
        print(word_list)
        if not word_list:
            break
        all_word_list.extend(word_list)
        position += num
    return all_word_list
    pass

if __name__ == "__main__":
    # baocuncihui("二字词")
    # word_list = get_word(0, 100)
    all_word_list = get_all_ci()
    # baocuncihui('明星词汇', all_word_list)
    print(all_word_list)