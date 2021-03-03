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
        temp = self.originalAWS.getValues()
        # Changing assigned new value
        temp[0] = 100
        
        actual = self.original
        stored = self.originalAWS.getValues()
        
        self.assertEqual(actual[0], stored[0])

        
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
        
    def test_removeBiggerThan(self):
        list_1 = [0,1,2,3,4,5,6]
        aws_list1 = AWS(list_1)
        
        threshold = 3
        
        n_remove = aws_list1.removeBiggerThan(threshold)
                
        aws_after_remove = aws_list1.getValues()

        self.assertEqual(n_remove, 3)
        self.assertEqual(aws_after_remove[4], self.FILLER_VALUE)
        self.assertEqual(aws_after_remove[5], self.FILLER_VALUE)
        self.assertEqual(aws_after_remove[6], self.FILLER_VALUE)

        

if __name__ == '__main__':
    unittest.main()