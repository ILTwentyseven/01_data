# -*- coding:utf-8 -*-
import multiprocessing
import os


def down_file_name(q, file_name, old_file_name, new_file_name):
    # print("旧文件：%s --->新文件：%s文件名是：%s" % (old_file_name, new_file_name, file_name))
    old_f = open(old_file_name + "/" + file_name, "rb")
    file_content = old_f.read()
    old_f.close()
    new_f = open(new_file_name + "/" + file_name, "wb")
    new_f.write(file_content)
    new_f.close()
    # 检测是否完成文件的复制
    q.put(file_name)


def main():
    # 输入要下载的文件夹
    old_file_name = input("请输入要下载的文档的名字：")
    # 创建一个新的文件夹
    try:
        new_file_name = old_file_name + "[附件]"
        os.mkdir(new_file_name)
    except:
        pass
    # 打开要下载的文件夹
    file_names = os.listdir(old_file_name)
    # print(file_names)
    # 创建进程池
    po = multiprocessing.Pool(3)
    # 创建一个队列
    q = multiprocessing.Manager().Queue()
    # 向进程池中添加要执行的文件
    for file_name in file_names:
        po.apply_async(down_file_name, args=(q, file_name, old_file_name, new_file_name))
    po.close()
    # po.join()
    all_file_num = len(file_names)
    file_num = 0
    while True:
        file_name = q.get()
        # print("已经完成复制%s" % file_name)
        print("\r已经完成的进度%.2f %%" % (file_num*100/all_file_num), end='')
        file_num += 1
        if file_num >= all_file_num:
            break


if __name__ == "__main__":
    main()