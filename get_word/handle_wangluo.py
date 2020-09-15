
# with open("../网络流程词汇.txt", mode="r") as file:
#     danci_list = []
#     position = 0
#     for line in open():
#         position += 1
#         if position % 2 == 0:
#             danci_list.append(text)
#     print(danci_list)
with open("../网络流行词汇(不含词)", "w", encoding="utf-8") as write_file:
    for line in open("../网络流程词汇.txt"):
        line = line.strip()
        if "摘要: " in line:
            continue
        write_file.write("{}\n".format(line))