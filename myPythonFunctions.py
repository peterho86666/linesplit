from random import randint 
from os import remove, rename

def getUserScore(userName):

    try:    

        f = open('userScore.txt', 'r')
    
        for line in f:
            content = line.split(',')
            if content[0] == userName:
                f.close()
                return content[1]
        #content[0] != userName:
        f.close()
        return "-1"
            
    except IOError as e:

        print ("File not found: ", e)
        f1 = open('userScore.txt', 'w')
        f1.close()
        return "-1"

    except Exception as f:

        print ("Unknown error: ", f)


