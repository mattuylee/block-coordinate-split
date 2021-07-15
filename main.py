#!/usr/bin/python3
# coding=utf-8
import csv

# 输入文件
INPUT_PATH = "./demo-input.csv"
# 输出文件
OUTPUT_PATH = "./output.csv"
# 唯一标识符字段
ID_FIELD = "A"
# 拐点数据字段
DATA_FIELD = "ZB"
# 新生成的唯一ID字段名，为空则不生成
GENERATED_ID = None

try:
    in_file = out_file = None
    in_file = open(INPUT_PATH)
    out_file = open(OUTPUT_PATH, mode="x")
    # 读入csv区块坐标文件
    reader = csv.DictReader(in_file)
    # 写入导出文件的头部
    fields = list(reader.fieldnames)
    if GENERATED_ID:
        fields.insert(0, GENERATED_ID)
    writer = csv.DictWriter(out_file, fields)
    writer.writeheader()
    # 分别对每一个区块数据按区域拆分为多个区块数据
    for row in reader:
        data = row[DATA_FIELD].split(",")
        # 第一个数为区域数
        area_count = int(data[0])
        cursor = 1
        # 按每个区域拆分原数据，将每个区域的拐点数据重导出为仅含一个区域的区块坐标数据
        for i in range(0, area_count):
            if cursor >= len(data):
                break
            # 除数据字段外，复制其他字段
            new_row = row.copy()
            new_row[DATA_FIELD] = None
            point_count = int(data[cursor])
            # 拆分后的数据只有一个区域，先初始化填入区域数和拐点数
            new_data = ["1", str(point_count)]
            # 将当前位置+1，开始处理拐点坐标
            cursor += 1
            # 取拐点数*2个数，即拐点坐标数据，并暂存到new_data数组
            for item in data[cursor : (cursor + point_count * 2)]:
                new_data.append(item)
                cursor += 1
            # 如果下一个区域拐点数为0或者-1，则为主区域或挖空区域标识，直接加入当前区域拐点数据后面
            nextItem = int(data[cursor]) if cursor < len(data) else None
            if nextItem == 0 or nextItem == -1:
                new_data.append(data[cursor])
                new_data.append(data[cursor + 1])
                new_data.append(data[cursor + 2])
                cursor += 3
            # 为新数据插入唯一ID字段
            if GENERATED_ID:
                new_row[GENERATED_ID] = row[ID_FIELD] + "_" + str(i)
            # 用逗号拼接数据数组
            new_row[DATA_FIELD] = ",".join(new_data)
            # 写入拆分区域拐点数据后的新行
            writer.writerow(new_row)
except FileNotFoundError:
    print("ERROR: 输入文件不存在")
except FileExistsError:
    print("ERROR: 输出文件已存在")
except Exception as e:
    print("ERROR: 未知错误")
    raise e
finally:
    if in_file:
        in_file.close()
    if out_file:
        out_file.close()