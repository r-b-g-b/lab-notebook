#!/usr/bin/env python
import zmq
ctx = zmq.Context()
s = ctx.socket(zmq.SUB)
s.connect('tcp://localhost:5556')
s.setsockopt(zmq.SUBSCRIBE, 'hi')
print 'receiving'
for i in range(3):
    msg = s.recv()
    print msg