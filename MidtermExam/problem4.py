# Problem 4
#
# Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. 
# For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]
#
# This function takes in a list of strings and returns a list of strings. Your function should not modify aList.

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    sublist = []
    for element in aList:
        if len(element) < 4:
            sublist.append(element)
    return sublist

def main():
    aList = ["apple", "cat", "dog", "banana"]
    print(lessThan4(aList))

if __name__ == '__main__':
    main()