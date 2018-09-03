# -*- coding:utf-8 -*-
import socket


def file_download(new_client_socket, client_addr ):
    # 服务器接受数据
    recv_data = new_client_socket.recv(1024)
    # 打印接受的数据
    print("客户端要下载文件:%s" % recv_data.decode('utf-8'))
    file_content = None
    try:
        download_file = open(recv_data, "rb")
        file_content = download_file.read()
    except Exception as ret:
        print("没有要下载的文件%s" % recv_data)
    # 文件传输
    if file_content:
        new_client_socket.send(file_content)


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
    # 等待服务器连接
    new_client_socket, client_addr = tcp_server_socket.accept()
    # 文件传输
    file_download(new_client_socket, client_addr)
    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
