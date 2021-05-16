#coding=UTF-8
from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest
import json,sys

ID = sys.argv[1]
Secret = sys.argv[2]
RegionId = sys.argv[3]

clt = client.AcsClient(ID,Secret,RegionId)

DBInstanceIdList = []
DBInstanceIdDict = {}
ZabbixDataDict = {}
def GetRdsList():
    RdsRequest = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
    RdsRequest.set_accept_format('json')
    #RdsInfo = clt.do_action(RdsRequest)
    RdsInfo = clt.do_action_with_exception(RdsRequest)
    for RdsInfoJson in (json.loads(RdsInfo))['Items']['DBInstance']:
        DBInstanceIdDict = {}
        try:
            DBInstanceIdDict["{#DBINSTANCEID}"] = RdsInfoJson['DBInstanceId']
            DBInstanceIdDict["{#DBINSTANCEDESCRIPTION}"] = RdsInfoJson['DBInstanceDescription']
            DBInstanceIdList.append(DBInstanceIdDict)
        except Exception, e:
            print Exception, ":", e
            print "Please check the RDS alias !Alias must not be the same as DBInstanceId！！！"
            


GetRdsList()
ZabbixDataDict['data'] = DBInstanceIdList
print json.dumps(ZabbixDataDict)
