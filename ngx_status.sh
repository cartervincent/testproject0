#!/bin/bash

#定义Nginx status页面
ngx_status="http://127.0.0.1:888/ngx_status"

#在NGinx配置文件中添加：
#	server{
#	listen 888;
#	location /ngx_status {  
#            stub_status on;
#            allow 127.0.0.1;
#            access_log off;
#            deny all;
#        }
#}

#判断status页面是否存活
ngx_status_code() {
        http_code=`curl -o /dev/null -s -w %{http_code} ${ngx_status}`
        if [ ${http_code} == "200" ];then
                return 1
        else
                return 0 # return "Nginx status is not running."
        fi
}

ping() {
        ngx_status_code 
       	[ 1 == $? ]&& echo 1 || echo 0
       	# [ 1 == $? ]&& echo 0 || echo 1
}

#获取当前活动的客户端连接数
active() {
        ngx_status_code || curl -s ${ngx_status} | grep "Active" | awk '{print $NF}'
}

#获取接收客户端连接的总数量
accepts() {
        ngx_status_code || curl -s ${ngx_status} | awk NR==3 | awk '{print $1}'
}

#获取已处理的连接总数量
handled() {
        ngx_status_code || curl -s ${ngx_status} | awk NR==3 | awk '{print $2}'
}

#获取客户端请求总数量
requests() {
        ngx_status_code || curl -s ${ngx_status} | awk NR==3 | awk '{print $3}'
}

#获取正在读取请求标头的当前连接数量
reading() {
        ngx_status_code || curl -s ${ngx_status} | grep "Reading" | awk '{print $2}'
}

#获取正在将响应写回到客户端的当前连接数量
writing() {
        ngx_status_code || curl -s ${ngx_status} | grep "Writing" | awk '{print $4}'
}

#获取当前正在等待响应的客户端连接数量
waiting() {
        ngx_status_code || curl -s ${ngx_status} | grep "Waiting" | awk '{print $6}'
}

#使用位置变量控制脚本输出
case $1 in
        ping)
                ping;;
        active)
                active;;
        accepts)
                accepts;;
        handled)
                handled;;
        requests)
                requests;;
        reading)
                reading;;
        writing)
                writing;;
        waiting)
                waiting;;
        *)
                echo "Unknown options"
esac

