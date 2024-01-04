import unittest
from log_analyzer import LogEntry

class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        # TODO: Create THREE LogEntry objects
        self.log1 = LogEntry('2022-01-01 04:06:51 UTC','192.168.162.83','5060','SIP - Session Initiation Protocol','Allow','146','US','United States','107.154.148.26')
        self.log2 = LogEntry('2022-01-02 04:26:29 UTC','10.96.247.230','20','FTP - Data','Allow','146','US','United States','128.99.73.63')
        self.log3 = LogEntry('2022-02-01 04:32:51 UTC','10.133.38.22','21','FTP - Control','Allow','92','US','United States','200.213.122.173')
        self.log4 = LogEntry('2022-02-02 04:49:06 UTC','10.66.172.199','161','SNMP - Simple Network Management Protocol','Deny','307','CN','China','230.177.69.220')
        self.log5 = LogEntry('2022-03-01 04:54:12 UTC','10.200.87.244','20','FTP - Data','Log','367','HK','Hong Kong','240.57.53.74')

    def testEventTime(self):
        # TODO: Test LogEntry objects created in the setUp() method. 
        self.assertEqual(self.log1.event_time.month, 1)
        self.assertEqual(self.log2.event_time.day, 2)
        self.assertEqual(self.log3.event_time.month, 2)
        self.assertEqual(self.log4.event_time.day, 2)
        self.assertEqual(self.log5.event_time.hour, 4)
        
        self.assertNotEqual(self.log1.event_time.hour, 5)
        self.assertNotEqual(self.log1.event_time.month, 3)



    def testClassIP(self):
        # TODO: Test LogEntry objects created in the setUp() method. 
        self.assertEqual(self.log1.ipv4_class, 'A')
        self.assertEqual(self.log2.ipv4_class, 'B')
        self.assertEqual(self.log3.ipv4_class, 'C')
        self.assertEqual(self.log4.ipv4_class, 'D')
        self.assertEqual(self.log5.ipv4_class, 'E')

        self.assertNotEqual(self.log1.ipv4_class, 'B')
        self.assertNotEqual(self.log1.ipv4_class, 'E')

if __name__ == '__main__':
    unittest.main()