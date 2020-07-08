#! /usr/bin/env python3

import redis
import time

class Scpt01():
    def __init__(self,host="localhost",port="6379"):
        self.rs  = redis.Redis(host='localhost',port=6379)
        self.pub = self.rs.pubsub()
        self.switch = False
        #开始模块
        self.__startup()

    #######
    def __loop(self):
        while self.switch:
            # self.rs.publish("GAIT_FORWARD","......")
            # time.sleep(5)
            self.rs.publish("GAIT_BACK","....")
            # time.sleep(5)

            #只执行一次
            self.rs.publish("GAIT_RELEASE",".....")



 

    #########
    #关闭模块
    def __release(self):
        self.switch = False

    #开启模块
    def __startup(self):
        self.switch = True
        self.__loop()
    
    


    


