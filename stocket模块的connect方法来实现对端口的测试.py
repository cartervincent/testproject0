# -*- coding:UTF-8 -*-
import socket


def monitor(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    host = (ip, port)
    try:
        s.connect(host)
        print('已经成功连接%s的%d端口!' % (ip, port))
    except Exception:
        print('无法连接%s的%d端口!' % (ip, port))
    s.close()


if __name__ == "__main__":
    ip = input('请输入需要测试的主机ip地址:')
    port = int(input('请输入测试的端口:'))
    monitor(ip, port)
