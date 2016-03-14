""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import os
import sys
import anydbm
import pickle

def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

        A new counter will be created and initialized to 1 if none exists or if
        the reset flag is True.

        If the counter already exists and reset is False, the counter's value will
        be incremented.

        file_name: the file that stores the counter to be incremented.  If the file
                   doesn't exist, a counter is created and initialized to 1.
        reset: True if the counter in the file should be reset.
        returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    db = anydbm.open('dump.db','c')
    if os.path.exists('file_name') and reset==False:
        openfile = open('file_name','r+')
        val = int(openfile.readline()) + 1
        openfile.close()
        openfile = open('file_name','w')
        openfile.write(str(val))
    else:
        openfile = open('file_name','w')
    	if reset==True:
        	openfile.write('1')
    	else:
        	openfile.write('1')
    openfile.close()
    openfile = open('file_name','r+')
    line = openfile.readline()
    count = pickle.dumps(line.strip()[0])
    count1 = pickle.loads(count)
    db['count'] = count1  
    openfile.close()
    return int(db['count'])
    db.close()
    



if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print "new value is " + str(update_counter(sys.argv[1]))