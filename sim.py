#!/usr/bin/python

import os 
import time
import random

def gen_reqs(elb, request_times):
    it = time.time()

    for j in range(1,10): # 10 secs
        for i in range(1,100): # 100rps
            request_times[j*1000 + i] = elb.transport(i)-it        

        sl_time = time.time() - it
        if sl_time < 1:
            time.sleep(sl_time)
            
    return request_times

class Elb(object):
    """ In this simulation ELB acts as the enabler for running "gravorg"
    and identifying/starting the number of required servers""" 
    def __init__(self):
        self.l_server = []
        s = Server(0)
        self.l_server.push_back(s)

    def transport(self):
        serv_num = random.choice(self.l_server)
        
    
    
class Server(object):
    """ assumed = 10rps, real = 5rps"""
    def __init__(self, num, real_limit, assumed_limit):
        self.sid = num
        self.count = 0
        self.rlimit = real_limit
        self.alimit = assumed_limit

    def resolve(self, req_id):
        if self.count < self.real_limit:
            return random.randint(1,100)/100
        else:
            return None
        
def main():
    request_times = {}

    t_hash = gen_reqs(request_times)
    for k,v in t_hash.iteritems():
        print k,v


if __name__ == '__main__':
    main()
