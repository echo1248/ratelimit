# -*- coding:utf8 -*-
# Create @ 2017-08-17 09:13:58
# Author @ 819070918@qq.com

from __future__ import with_statement

import time

from ratelimit import new_bucket


def bucket_print(bucket):
	# print bucket.start_time
	# print bucket.capacity
	# print bucket.quantum
	# print bucket.fill_interval
	# print bucket.clock
	# print bucket.avail
	# print bucket.avail_tick
	pass

def test_bucket():

	fill_interval = 500
	capacity = 3
	bucket = new_bucket(fill_interval, capacity)

	availale = bucket.take_available(2)
	print availale
	availale = bucket.take_available(1)
	print availale
	availale = bucket.take_available(1)
	print availale
	availale = bucket.take_available(1)
	print availale

	time.sleep(0.0005)
	availale = bucket.take_available(2)
	print availale

	time.sleep(0.001)
	availale = bucket.take_available(2)
	print availale




if __name__ == '__main__':
	test_bucket()
	
