import unittest
import mymodule

input_lst=[5,2,7,1,4,7,8]
final_out=[1, 4, 16, 25, 49, 49, 64]

class Pyunit_Test(unittest.TestCase):
    
    def setUp(self):
        ''' A setUp function(predefined: not user defined) is used to "Arrange" all required data for testing.
            Executed before every Test case function.
        '''
        print("\nSetUp Called for Arrange operations")
        '''Arrange: Gather all required data for current test case.
        '''
        self.lst=input_lst.copy()
        self.op_tst=final_out.copy
        self.op=None
    
    def test_case1(self):
        ''' A test case function is any function that starts with prefix : "test", used for "Act" and "Assert" operations.
            Test case function is executed after SetUp function.
            There can me multiple Test case functions in a class derived from "unittest"
            All test case functions are independent of each other
        '''
        print("Test Case 1 called for Act and Assert operations")
        '''Act: Run test cases.
                create resultsets for next assert operation.
        '''
        #Act Operations
        self.op = self.method(self.lst)        
        
        #Assert Operations
        '''Assert: Match stored result against result geenrated in "Act" operation for the current test case.
        '''
        self.assertTrue(self.op==final_out)
        '''
            Other Assert functions:
            assertEqual(a,b)
            assertNotEqual(a,b)
            assertFalse(x)
            assertAlmostEqual(a,b,precision_digits)
        '''
        
    def test_case2(self):
        '''Dummy Test Case'''
        print("inside Test case 2")

    def tearDown(self):
        ''' Tear down function(predefined: not user defined) is used to wrap up the current test case for next test case execution by:
                a)closing any connections
                b)removing any variables to free up program heap memory for next test case
            Executed after every test case function
        '''
        print("Wrapping up the current test case")
        del(self.op)
        del(self.lst)
        del(self.op_tst)

    def method(self,param_list):
        '''User defined method of class'''
        temp = mymodule.SqSeries(param_list)
        temp.sort()
        return temp
        
def main():
    '''create the test suite for test case above'''
    suite = unittest.TestLoader().loadTestsFromTestCase(Pyunit_Test)
    '''run test suite'''
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()