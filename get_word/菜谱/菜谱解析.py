import requests, random, json, os, time, re
from bs4 import BeautifulSoup

url = "https://home.meishichina.com/ajax/ajax.php?ac=recipe&op=getMoreDiffStateRecipeList&classid={}&orderby={}&page={}"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    "Referer": ""
}

def get_word(classid, orderby, page_num):
    try:
        r = requests.get(url.format(classid, orderby, page_num), headers=headers)
        json_str = r.content.decode('utf-8')
        word_dict = json.loads(json_str)
        result_list = word_dict['data']
        word_list = []
        for result in result_list:
            word_list.append(result['title'])
        return word_list
    except Exception as ex:
        return []

def baocuncihui(file_name, all_word_list, num=10):
    with open("./{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")

new_tuijian = 0
new_fabu = 0
recai = 102
liangcai = 202
tanggeng = 57
zhushi = 59
xiaochi = 62
xican = 160
hongpei = 60
shicai = 69
mulu_list = [recai, liangcai, tanggeng, zhushi, xiaochi, xican, hongpei, shicai]


if __name__ == "__main__":
    all_word_list = []
    for page in range(100):
        word_list = get_word(new_fabu, "new", page)
        if word_list:
            all_word_list.extend(word_list)
        else:
            break
    for mulu in mulu_list:
        for page in range(100):
            word_list = get_word(mulu, "tag", page)
            print("mulu:{}, {}".format(mulu, word_list))
            if word_list:
                all_word_list.extend(word_list)
            else:
                break
    all_word_list = list(set(all_word_list))
    random.shuffle(all_word_list)

    baocuncihui("菜谱词汇", all_word_list)