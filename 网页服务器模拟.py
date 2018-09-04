# -*- coding:utf-8 -*-
import re
import socket
    service_alient(new_tcp_socket, client_addr):
    # 1 接受客户端传递的信息
    client_content = new_tcp_socket.recv(1024)
    recv_content = client_content.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)", recv_content[0])
    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"
    # 2 将本地信息反馈给客户端
    try:
        f = open("/html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        send_message = "not found"
        new_tcp_socket.send(response.encode('utf-8'))
        new_tcp_socket.send(send_message.encode('utf-8'))
    else:
        send_messge = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_tcp_socket.send(response)
        new_tcp_socket.send(send_messge)
    new_tcp_socket.close()  # 将其关闭就成为长连接方式



def main():
    # 1 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2 绑定ip和端口
    tcp_socket.bind(("", 3424))
    # 3 将套接字转换为被动
    tcp_socket.listen(128)
    while True:
        # 4 等待服务器的连接
        new_tcp_socket, client_addr = tcp_socket.accept()
        # 5 网页服务器的搭建
        service_alient(new_tcp_socket, client_addr)
    tcp_socket.close()


if __name__ == "__main__":
    main()

