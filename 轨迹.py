import re
import json


def txtToJson():
    # 文件路径
    path = "星期六热力图.txt"
    # 读取文件
    with open(path, 'r') as file:
        # 定义一个用于切割字符串的正则
        seq = re.compile(",")
        # 逐行读取
        item = []
        for line in file:
            lst = seq.split(line.strip())
            time1 = int(lst[3])/10000
            time1 = int(time1)
            if time1<18 and time1 > 16:
                items = [float(lst[0]),float(lst[1])]
                item.append(items)
    # 关闭文件
    with open('Sat_txtToJson.json', 'w') as dump_f:
        json.dump(item, dump_f)


if __name__ == '__main__':
    txtToJson()