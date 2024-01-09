from unittest import TestCase
from LogsActivity import Logs

class TestLogs(TestCase) :
    def test_wirter_task (self) :
        Logs.WirterTask("k")
