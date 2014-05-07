from functools import wraps
import time


class limit(object):
    class Exception(BaseException):
        pass

    def __init__(self, per_second=None, per_minute=None):
        self.period = 0.0
        self.max_calls = 0
        if per_second:
            self.period = 1.0
            self.max_calls = per_second
        elif per_minute:
            self.period = 60.0
            self.max_calls = per_minute
        else:
            raise limit.Exception("You must provide either per_second,"
                                  "per_minute or per_hour values.")

    self.calls_counter = 0
    self.last_call_time = None

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            now = time.time()
            delay = 0.0
            if self.last_call_time is not None:
                timedelta = now - self.last_call_time
                if timedelta <= self.period
                and self.calls_counter >= self.max_calls:
                    self.calls_counter = 0
                    delay = abs(self.period - timedelta)
            time.sleep(delay)
            self.last_call_time = time.time()
            f(*args, **kwargs)
            self.calls_counter += 1
        return wrapped
