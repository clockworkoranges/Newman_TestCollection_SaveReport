# coding=utf-8
import time
import os

class postmanApiTest:
    #运行postman生成报告
    #通过newman
    def postman(self):
        # 测试报告保存路径
        jSONfname = 'D:/newman_req_result/result' + time.strftime('%Y-%m-%d', time.gmtime())+'.html'
        # postman接口测试使用的collection地址
        cmd_1='newman run G:\postman文件夹\高德地图web服务api.postman_collection.json'
        # 基础版测试报告
        cmd_2='newman run "G:\postman文件夹\高德地图web服务api.postman_collection.json" --reporters html --reporter-html-export {}'.format(jSONfname)
        # 美化版测试报告
        cmd_3='newman run "G:\postman文件夹\高德地图web服务api.postman_collection.json" -r htmlextra,cli --reporter-htmlextra-export {}'.format(jSONfname)
        # Newman从命令行测试postman集合
        os.system(cmd_1)
        os.system(cmd_3)

        print('------------------------------------------------------------')
        print(jSONfname)

        if os.path.isfile(jSONfname):
            print(jSONfname)
            return jSONfname
        else:
            return False


if __name__ == '__main__':
    a = postmanApiTest()
    a.postman()
