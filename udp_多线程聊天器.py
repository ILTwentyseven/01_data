# -*- coding:utf-8 -*-
import socket
import threading


def recv(udp_socket):
    while True:
        # 接受数据
        recv_data = udp_socket.recvfrom(1024).decode('utf-8')
        print(recv_data)


def send(udp_socket, send_ip, send_port):
    while True:
        send_data = input("请输入要发送的内容：")
        udp_socket.sendto(send_data.encode('utf-8'), (send_ip, send_port))

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_ip = ""
    udp_port = 8989
    udp_addr = (udp_ip, udp_port)
    udp_socket.bind(udp_addr)
    # 发送数据
    send_ip = input("请输入要发送的ip")
    send_port = input("请输入要发送的port")
    # 创建多线成
    recv_start = threading.Thread(target=recv, args=(udp_socket,))
    send_stare = threading.Thread(target=send, args=(udp_socket, send_ip, send_port))
    recv_start.start()
    send_stare.start()

    # # 关闭套接字
    # udp_socket.close()


if __name__ == "__main__":
    main()
