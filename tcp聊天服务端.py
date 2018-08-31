# -*- coding:utf-8 -*-
import socket


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务器地址
    server_ip = ""
    server_port = 8798
    server_addr = (server_ip, server_port)
    tcp_server_socket.bind(server_addr)
    # 将套接字转换为被动
    tcp_server_socket.listen(128)
    while True:
        # 等待服务器连接
        new_client_socket, client_addr = tcp_server_socket.accept()
        # 服务器接受数据
        while True:
            # 服务器接受数据
            recv_data = new_client_socket.recv(1024)
            # 打印接受的数据
            print("客户端发送:%s" % recv_data.decode('utf-8'))
            if recv_data:
                # 返回值给客户端
                new_client_socket.send("欢迎使用Tcp".encode('utf-8'))
            else:
                break
        new_client_socket.close()
    # 关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
