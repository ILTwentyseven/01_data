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
    while True:
        # 发送信息
        server_content = input("请输入要发送的内容")
        if server_content:
            tcp_client_socket.send(server_content.encode('utf-8'))
        # 关闭套接字
        tcp_client_socket.close()


if __name__ == "__main__":
    main()




