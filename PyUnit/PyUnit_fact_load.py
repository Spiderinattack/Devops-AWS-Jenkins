import unittest
import os
import sqlite3


db_list = ["PyUnit/northwind.db","ignore.db"]
delta_count_lst= [5,None]
db_ptr=0


class Pyunit_Test(unittest.TestCase):
    
    def setUp(self):
        ''' A setUp function(predefined: not user defined) is used to "Arrange" all required data for testing.
            Executed before every Test case function.
        '''
        print("\nSetUp Called for Arrange operations")
        '''Arrange: Gather all required data for current test case.
        '''
        global db_list
        global delta_count_lst
        global db_ptr
        
        self.conn = sqlite3.connect(db_list[db_ptr])
        self.command = "sqlite3 "+db_list[db_ptr]+" < PyUnit/fact_load.sql"
        self.delta_count=delta_count_lst[db_ptr]
        db_ptr=db_ptr+1
                
        self.rec_cnt, self.dupe_cnt = self.method(self.conn)
    
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
        exe_stat = os.system(self.command)
        if exe_stat != 0:
            raise Exception("file "+self.command+" not found")
        
        rec_cnt_inc,dupe_cnt_inc = self.method(self.conn)
           
        
        #Assert Operations
        '''Assert: Match stored result against result genrated in "Act" operation for the current test case.
        '''
        
        self.assertEqual(self.delta_count,rec_cnt_inc-self.rec_cnt)
        self.assertEqual(dupe_cnt_inc,0)
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
        self.conn.close()
        del(self.command)
        
    def method(self,conn):
        '''User defined method of class'''
        cursor = conn.execute("select count(*) from fact_order")
        rec_cnt = [i[0] for i in cursor]
        rec_cnt = int(rec_cnt[0])
        cursor = conn.execute("select count(orderid)- count(distinct orderid) as dulplicates from fact_order")
        dupe_cnt = [i[0] for i in cursor]
        dupe_cnt = int(dupe_cnt[0])
        return rec_cnt,dupe_cnt
        
def main():
    '''create the test suite for test case above'''
    suite = unittest.TestLoader().loadTestsFromTestCase(Pyunit_Test)
    '''run test suite'''
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
