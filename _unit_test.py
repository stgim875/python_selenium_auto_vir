# import HtmlTestRunner
import unittest
import HtmlTestRunner
from HtmlTestRunner.runner import HTMLTestRunner
from test import start, remotelogin

class Remotetest(unittest.TestCase):
    
    def test_start(self):
        start()
        
    def test_remotelogin(self):
        remotelogin()

if __name__ == '__main__':
    # unittest.main()
    reportFoler = "ReportTest"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reportFoler))