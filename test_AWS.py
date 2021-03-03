# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:49:40 2021

@author: call0015
"""
import unittest
import sys

from AWS import AWS

class AWSTest(unittest.TestCase):
    
    FILLER_VALUE = -int(sys.maxsize)
    
    # https://stackoverflow.com/questions/17353213/init-for-unittest-testcase/17353262
    def __init__(self, *args, **kwargs):
        super(AWSTest, self).__init__(*args, **kwargs)
        self.original = [1,2,3]
        
    def setUp(self):
        try:
            self.originalAWS = AWS(self.original)
        except:
            print("Exception happened")
            
    def test_GetValues(self):
        self.assertFalse(True)
        
    def test_str(self):
        self.assertFalse(True)
        
    def test_AWS(self):
        expected = [1,2,3]
        x = [1,2,3]
        aws = AWS(x) 
        
        x[1] = 100
        actual = aws.getValues()
        self.assertEqual(actual[0], expected[0])
        self.assertEqual(actual[1], expected[1])
    
    def test_FillAndExpand(self):
        position = 1
        numberOfTimes = 2
        org = self.originalAWS.getValues()
        expectedValue = org[position]
        first = org[0]

        expected = len(self.originalAWS.getValues()) + numberOfTimes
        self.originalAWS.fillAndExpand(position, numberOfTimes)
        result = self.originalAWS.getValues()
        self.assertEqual(expected, len(result))
		
        a = result[1]
        b = result[2]
        c = result[3]
        self.assertEqual(expectedValue, a)
        self.assertEqual(expectedValue, b)
        self.assertEqual(expectedValue, c)
        
        self.assertEqual(first, result[0])

if __name__ == '__main__':
    unittest.main()