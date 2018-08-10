#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys

# 指定一个路径
##path = "django-docs-2.1-zh-hans"

 #  函数参数文件夹路径
def getfile(path):
    # 获取该路径下的所以目录及文件
    dir_list = os.listdir(path)
    # 如果目录存在
    for dir in dir_list:
        # 目录 加上根目录 形成新路径
        dirpath = path + "/" + dir
        # 如果是一个目录
        if os.path.isdir(dirpath):
            # 递归调用函数继续遍历
            getfile(dirpath)
            # print(dirpath)
        else:
            # 如果不是目录  判断是否是html文件
            if dirpath.split(".")[-1] == "html":
                print(dirpath)
                # # 打开文件  设置读取权限   用w+权限会出现问题 所以读取与存储分开
                f = open(dirpath, "r", encoding="utf-8")
                # 读取文件
                content = f.read()
                # 关闭文件
                f.close()
                # 统计<script 出现次数   因为有标签  所以用<script
                num = content.count("<script")
                i = 0
                while i < num :
                    # 判断<script是否在文件中
                    if "<script" in content:
                        # 获取<script 开始索引位置
                        start = content.index("<script")
                        # 获取 ript> 结束位置
                        end = content.index("ript>")
                        # 截取 js代码内容
                        res = content[start:end + 5]
                        # print(res)
                        # 替换为空
                        content = content.replace(res," ")
                        i += 1
                    # 可以删去
                    else:
                        print("没有js代码")
                        break

                if "<script" in content:
                    print("还存在js代码块")
                else:
            # 将新文件重新写入文件  并覆盖之前的内容
                    f = open(dirpath,"w",encoding="utf-8")
                    f.write(content)
                    f.close()
    
getfile(sys.argv[1])
print("文件清理完成。。。")
