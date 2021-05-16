#!/bin/sh

echo "==================== start clean docker containers logs =========================="

logs=$(find /var/lib/docker/containers/ -name *-json.log)
logs2=$(find /data/dockerfiles/logs/ -name *.log.gz)
RmLog=$(find /var/lib/docker/overlay2/ -name *.log.gz)

for log1 in $logs1
        do
                echo "clean logs : $log"
                cat /dev/null > $log1
        done
		
for del_log in $RmLog
        do
                rm -rf $RmLog
        done
		
for del_logs in $logs2
        do
                rm -rf $logs2
        done


echo "==================== end clean docker containers logs   =========================="
