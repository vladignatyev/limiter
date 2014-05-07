limiter
=======

Very simple query time limiter written in Python. 
No additional dependencies needed.

It allows you to delay call of functions to keep timing limits. 
For example, if you have any API demanding to query rarely than 
8 queries per second, you may use limiter to match this limitation.

It is experimental and could be used freely for scrapers and little utils
where whole process lock is possible.

NOTE: If you need it for continuously working service or website, please refer 
to queues and schedulers based solutions.

Usage
-----
Limitation per second. In the example below we emulate querying service 
not more often than 2 times per second.

```
import limiter

@limit(per_second=2)
def query_limited_ping():
	print 'PONG'

while True:
	query_limited_ping()  # will print 'PONG' not more than 2 times per second
```

Features
--------
* "Greedy" limitation: when time limit exceeds it will sleep 
(lock your process) until limit become free
