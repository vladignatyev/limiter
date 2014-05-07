import unittest

import time
import os
from limiter import limit


class LimiterTests(unittest.TestCase):
    def marker_function(self):
        self.timestamps.append(time.time())

    def setUp(self):
        self.timestamps = []

    def test_shouldFailWhenNoLimitsProvided(self):
        with self.assertRaises(limit.Exception):
            limit()

    def test_shouldRunNoMoreThanProvidedTimesPerSecond(self):
        calls = 20
        per_second = 10
        limited = limit(per_second=per_second)
        for i in range(0, calls + 1):
            limited(self.marker_function)()

        first = self.timestamps[0]
        last = self.timestamps[-1]

        self.assertTrue(last - first > calls / per_second,
                        "Should run all %s calls to function for time greater"
                        " than %s seconds."
                        % (calls, calls / per_second))

    # todo: avoid slow test and copy-paste! test only boundary conditions
    @unittest.skipIf("SLOW" not in os.environ,
                     "skipping due to test is very slow")
    def test_shouldRunNoMoreThanProvidedTimesPerMinute(self):
        calls = 20
        per_minute = 10
        limited = limit(per_minute=per_minute)
        for i in range(0, calls + 1):
            limited(self.marker_function)()

        first = self.timestamps[0]
        last = self.timestamps[-1]

        self.assertTrue((last - first) > 60.0 * calls / per_minute,
                        "Should run all %s calls to function for time greater"
                        "than %s minutes."
                        % (calls, 60.0 * calls / per_minute))


if __name__ == '__main__':
    unittest.main()