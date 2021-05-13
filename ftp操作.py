import ftplib
import os
import socket

HOST = 'wewetwet235'
USER = 'wtwtwtwtwt'
PASSWD = 'rhjhjrh'


def FtpConnect(host, username, passwd):
    try:
        ftp = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('Error, cannot reach ' + HOST)
        return
    else:
        print('Connect To Host Success...')

    try:
        ftp.login(USER, PASSWD)
    except ftplib.error_perm:
        print('Username or Passwd Error')
        ftp.quit()
        return
    else:
        print('Login Success...')

    return ftp


def FtpDownload(ftp, remotepath, localpath):
    try:
        ftp.retrbinary('RETR %s' % remotepath, open(localpath, 'wb').write)
    except ftplib.error_perm:
        print('File Error')
        os.unlink(localpath)
    else:
        print('Download Success...')
    ftp.quit()


def FtpUpload(ftp, remotepath, localpath):
    try:
        ftp.storbinary('STOR %s' % remotepath, open(localpath, 'rb'))
    except ftplib.error_perm:
        print('File Error')
        os.unlink(localpath)
    else:
        print('Upload Success...')
    ftp.quit()


if __name__ == '__main__':
    ftp = FtpConnect(HOST, USER, PASSWD)
    # FtpDownload(ftp, './连ftp.py', './')  # 下载
    FtpUpload(ftp, './htdocs/', './连ftp.py')  # 上传






