#!/usr/bin/env python
import zmq
ctx = zmq.Context()
s = ctx.socket(zmq.PUB)
s.bind('tcp://*:5556')
for i in range(3):
    print 'sending'
    s.send('hi there')