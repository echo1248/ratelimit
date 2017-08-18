ratelimit
=====
ratelimit is for python to limit to limit flow for web service.


Example:
----------

	from ratelimit import new_bucket


	fill_interval = 500
	capacity = 3
	bucket = new_bucket(fill_interval, capacity)

	availale = bucket.take_available(2)


Support
----------

if you have any problem or suggest, please contact me with my email of 819070918@qq.com.
