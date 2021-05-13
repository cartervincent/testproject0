from ftplib import FTP

ip = 'ftpupload.net'
port = 21


def test_ftp():
    ftp = FTP()
    ftp.connect(ip, port)
    ftp.login("b18_27162378", "NBfeGavYE4Q5z6q")  # 如果是匿名登录，直接ftp.login()
    files = ftp.dir()
    print(files)


if __name__ == '__main__':
    test_ftp()
