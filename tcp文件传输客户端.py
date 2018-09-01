# -*- coding:utf-8 -*-
import socket


def main():
    # 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 输入要连接的服务器的信息
    server_ip = input("请输入要连接的服务器的ip：")
    server_port = int(input("请输入要连接的服务器的端口："))
    server_addr = (server_ip, server_port)
    # 链接服务器
    tcp_client_socket.connect(server_addr)
    # 输入要下载的文件
    download_file_name = input("请输入要下载的文件名：")
    # 将文件名发送给服务端
    tcp_client_socket.send(download_file_name.encode('utf-8'))
    # 接受服务器发送过来的文件
    recv_file = tcp_client_socket.recv(1024)
    with open("download_file", "wb") as f:
        f.write(recv_file)
        print("接受成功")
    # 关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()




