######################################################################
# Author: Ntentia Dimitrios         TODO: Change this to your names
# Username: ntentiad                TODO: Change this to your usernames
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

def is_binary(bitstring):
    '''This function takes a bitstring as input,
    returning True if it is at least 7-bits and consists solely of 0s and 1s
    and returning False otherwise
    Hint: You might use the len() function compared to the sum the 0s and 1s'''
    flag=False
    if len(bitstring)>6:
        for i in bitstring:
            if i==0 or i==1:
                flag=True
            else:
                return False
    else:
        return flag
    #FIXME: Add code here

def is_div_by_sevens(bitstring):
    '''This function takes a bitstring as input,
    returning True if the length of the string is evenly divisible by 7
    and returning False otherwise.
    Hint: use the % modulus operator'''
    if len(bitstring)%7==0:
        return True
    else:
        return False
    #FIXME: Add code here



def split_into_sevens(bitstring):
    '''This function takes a bitstring whose length is evenly divisible by 7 as input,
    It returns the resultant list of 7-bit long strings as output.
    Hint 1: divide the length of your bitstring by 7, converting the result to an integer.
    Loop that many times and use slicing to "chunk" the string
    Hint 2: The list append method will also be useful.'''
    chunks=len(bitstring)/7
    temp=""
    list_of_chunks = []

    for i in range(chunks):
        for k in range(6):
            temp+=str(bitstring(i*7+k))
        temp=""
        list_of_chunks.append(temp)
    return list_of_chunks

    #FIXME Add code here

def add_parity(list_of_chunks):
    '''This function takes a list of binary strings as input, each 7 bits long,
    Using even parity, this function prepends a parity bit at the front end of each string,
    and returns the resulting list of 8-bit binary strings.'''

    # This function is already correct and tested

    parity_chunks = []
    for byte in list_of_chunks: # for each 7-bit chunk of binary
        count1s = 0 # count the 1's
        for letter in byte:
            count1s = count1s + int(letter)
        parity_chunks.append(str(count1s % 2) + byte) #count1s%2 is 0 when count1s is even and 1 when count1s is odd
    # print(parity_chunks) # for debugging
    return parity_chunks


def run_all(bitstring):
    '''This function takes bitstring as input,
    if bitstring is only 0s and 1s with length evenly divisible by 7
    it uses even parity to return the resulting list of 8-bit binary strings.
    otherwise it returns "Input Error" '''

    # This function is already correct and tested

    if is_binary(bitstring) and is_div_by_sevens(bitstring):
        my_list = split_into_sevens(bitstring)
        return (add_parity(my_list))
    else:
        return ("Input Error")


def main():
    '''The main() function--used to call all other functions.'''
    my_bits = input("Please enter a bitstring with length evenly divisible by 7: ")
    print(run_all(my_bits)) # This and the line above run the program interactively.


if __name__ == '__main__':
    main()  # calls the main() function
