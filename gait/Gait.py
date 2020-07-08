#! /usr/bin/env python3

import redis
import time

class Gait():
    def __init__(self,host="localhost",port="6379"):
        self.rs  = redis.Redis(host='localhost',port=6379)
        self.pub = self.rs.pubsub()
        #订阅事件
        self.pub.subscribe("GAIT_FORWARD")
        self.pub.subscribe("GAIT_BACK")
        self.pub.subscribe("GAIT_TURNRIGHT")
        self.pub.subscribe("GAIT_TURNLEFT")
        self.pub.subscribe("GAIT_WAIT")
        self.pub.subscribe("GAIT_TROT")
        self.pub.subscribe("GAIT_JUMP")
        self.pub.subscribe("GAIT_RUN")
        self.pub.subscribe("GAIT_RELEASE")
        self.pub.subscribe("GAIT_STARTUP")
        #因为python没有switch，这里用dict实现
        self.event={
            "GAIT_FORWARD"  : self.__gait_forward,
            "GAIT_BACK"     : self.__gait_back,
            "GAIT_TURNRIGHT": self.__gait_turnright,
            "GAIT_TURNLEFT" : self.__gait_turnleft,
            "GAIT_WAIT"     : self.__gait_wait,
            "GAIT_TROT"     : self.__gait_trot,
            "GAIT_JUMP"     : self.__gait_jump,
            "GAIT_RUN"      : self.__gait_run,
            "GAIT_RELEASE"  : self.__release,
            "GAIT_STARTUP"  : self.__startup,
            }

        self.cur_gait = None #current gait
        #开始模块
        self.__startup()

    #######
    #Loop for getMessage form MQ(Redis)
    def __loop(self):
        while self.switch:
            #handle channel and msg
            dict = self.pub.get_message()
            if dict is not None and dict["type"]=="message":
                self.__handleChannel(dict["channel"].decode(),dict["data"].decode())
            #excute current gait
            self.__excuteCurrentGait()



    #######
    # Handle message for channel
    def __handleChannel(self,ch,m):

        #第一次执行步态
        if self.cur_gait is None:
            self.__setupCurrentGait(ch,m)
            # self.__excuteCurrentGait(ch,m)

        #比较新步态与当前步态，不同则替换
        if self.cur_gait["channel"]!=ch:
            self.__setupCurrentGait(ch,m)


    #设置当前步态
    def __setupCurrentGait(self,channel,msg):
         self.cur_gait = {"channel":channel,"msg":msg}  

    #执行当前步态
    def __excuteCurrentGait(self):
        if self.cur_gait is not None:
            self.event[self.cur_gait["channel"]](self.cur_gait["msg"])

    #关闭模块
    def __release(self,msg=None):
        self.switch = False

    #开启模块
    def __startup(self,msg=None):
        self.switch = True
        self.__loop()
    
    #步态：前行
    def __gait_forward(self,msg):
        print("Dog forward....")
        pass
    #步态：后退
    def __gait_back(self,msg):
        print("Dog back....")
        pass

    #步态：右转
    def __gait_turnright(self,msg):
        pass

    #步态：左转
    def __gait_turnleft(self,msg):
        pass

    #步态：静止等待
    def __gait_wait(self,msg):
        pass
    
    #步态：跳跃
    def __gait_jump(self,msg):
        pass


    #步态：跑
    def __gait_run(self,msg):
        pass

    #步态： 踱步
    def __gait_trot(self,msg):
        pass



    


