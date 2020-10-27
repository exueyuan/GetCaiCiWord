import requests, random, json, os, time, re
from bs4 import BeautifulSoup

def baocuncihui(file_name, all_word_list, num=10):
    with open("./{}.txt".format(file_name), "w", encoding="utf-8") as file:
        for position, word in enumerate(all_word_list):
            file.write("{}/{}.{}\n".format(position // num + 1, position % num + 1, word))
            if (position + 1) % num == 0:
                file.write("\n")

class FileUtils:
    @staticmethod
    def read_line(file_name, is_return_none=False):
        if os.path.exists(file_name):
            for line in open(file_name):
                line = line.strip()
                if line:
                    yield line
                else:
                    if is_return_none:
                        yield line
        else:
            return []

def get_all_word(file_path):
    zhiye_list = []
    for line_num, line in enumerate(FileUtils.read_line(file_path)):
        # print(line_num, line)
        line_list = []
        if line_num == 0:
            line_list = line.split("、")
            # print(line_list)
        elif line_num == 1:
            line_list = line.split("，")
            # print(line_list)
        elif line_num == 2:
            line_list = line.split(" ")
            # print(line_list)
        elif line_num == 3:
            line_list = []
            line_list_ = line.split(" ")
            for ying_word in line_list_:
                word_list = ying_word.split("--")
                if len(word_list) >= 2:
                    zhongwen = word_list[1].strip()
                    if zhongwen:
                        line_list.append(zhongwen)
                # print(word_list)
            print(line_list)
        zhiye_list.extend(line_list)
    zhiye_list = list(set(zhiye_list))
    random.shuffle(zhiye_list)
    baocuncihui("职业词", zhiye_list)


if __name__ == "__main__":
    save_file_path = "./职业.txt"
    get_all_word(save_file_path)