######################################################################
# Author: Ntentia Dimitrios            TODO: Change this to your names
# Username: ntentiad                   TODO: Change this to your usernames
#
# Assignment: A09: Error Detection
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################
# Acknowledgements:
#   Modified from original code written by Dr. Jan Pearce
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

from inspect import getframeinfo, stack
from a09_error_detection import *

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def parity_test_suite():
    '''Designed to test the following functions:
    is_binary(bitstring)
    is_div_by_sevens(bitstring)
    split_into_sevens(bitstring)
    add_parity(list_of_chunks)
    run_all(bitstring)
    '''

    # tests for is_binary()
    unittest(is_binary('1001010') == True)
    unittest(is_binary('100 1010') == False)
    unittest(is_binary('100') == False)
    
    # Add your own tests here

    # tests for is_div_by_sevens(bitstring)
    unittest(is_div_by_sevens('1001010') == True)
    unittest(is_div_by_sevens('1001') == False)

    # Add your own tests here
    
    #tests for split_into_sevens(bitstring)
    unittest(split_into_sevens('1001010') == ['1001010'])
    unittest(split_into_sevens('100100011010010100001') == ['1001000','1101001','0100001'])

    # Add your own tests here
    
    #tests for add_parity(list_of_chunks)
    unittest(add_parity('') == [])
    unittest(add_parity(['1001010']) == ['11001010'])
    unittest(add_parity(['1001000','1101001','0100001']) == ['01001000','01101001','00100001'])

    # Add your own tests here
    
    #tests for run_all(bitstring)
    unittest(run_all('1001010') == ['11001010'])
    unittest(run_all('100100011010010100001') == ['01001000','01101001','00100001'])
    unittest(run_all('10010') == 'Input Error')

    # Add your own tests here
    
def main():
  
    parity_test_suite()
    
    
in __name__ == '__main__':
  main()
