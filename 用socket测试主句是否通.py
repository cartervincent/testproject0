#!/usr/bin/python3
# -*-encoding: utf8 -*-
import socket

Buffer_ = 1024


def write_ip_port(file_name, host, ports):
    """
    文件操作，生成对应的记录文件
    :param file_name: 生成的文件名
    :param host: 主机IP
    :param ports: 主机端口
    :return:
    """
    with open('./%s' % file_name, mode='a+', encoding='utf8') as file_handler:
        file_handler.write("%s\t%s\n" % (host, ports))


def connection_host(host, port):
    """
    测试防火墙是否开通
    :param host: 主机ip
    :param port: 主机端口
    :return:
    """
    cli = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    cli.settimeout(1)
    try:
        """
        处理正常连接
        """
        cli.connect((host, int(port)))
        cli.close()
        file = 'successful.txt'
        write_ip_port(file, host, port)
    except ConnectionRefusedError as cre:
        """
        处理端口关闭
        """
        # print(cre)
        file = 'ConnectionRefusedError.txt'
        write_ip_port(file, host, port)
    except socket.timeout as scto:
        """
        处理主机不通
        """
        # print(scto)
        file = "failed.txt"
        write_ip_port(file, host, port)


def read_ip_list(file_name):
    """
    读取ipList.txt文件中的ip和端口，添加到ip_list列表中
    """
    ip_list = []
    with open('./%s' % file_name, mode='r', encoding='utf8') as file_handle:
        for line in file_handle.readlines():
            line = line.replace("\n", '').strip()
            if line is '':
                continue
            line = line.split(' ')
            ip_list.append(line)
    return ip_list


def main(file):
    """
    主程序入口
    :param file: ip和端口的文件名，及其为路径，默认是当前路径
    :return:
    """
    ip_list = read_ip_list(file)
    for ip_port in ip_list:
        connection_host(ip_port[0], ip_port[1])


if __name__ == '__main__':
    main("ipList.txt")
