import io
import sys

'''
Modify this parameter to skip 1 in x frames. In the default,
4, this would skip 1 frame every 4 frames.

So, [5,3,4,3,4,4,1] would become [4,2,3,3,3,3,0].
'''
SKIP_FRAME = 4

##################################################
#          DO NOT MODIFY ANYTHING BELOW          #
##################################################

def main():
    output = []
    #input = [5,3,4,3,4,4,1]
    #expected = [4,2,3,3,3,3,0]
    #input = [4,3,4,3,4,4,1]
    #expected = [3,3,3,2,3,3,1]
    #input = [4,4,4,4,4,4,4]
    #expected = [3,3,3,3,3,3,3]
    #input = [5,4,5,4,5,4,5]
    #expected = [4,3,4,3,4,3,3]
    input = [1,1,1,1,1,1,1]
    expected = [1,1,1,0,1,1,1]
    currTime = 0
    for t in input:
        tNew = t

        framesToSkip = int((currTime+t) / SKIP_FRAME)
        tNew -= framesToSkip
        currTime = (currTime+t)%(SKIP_FRAME)
        #if currTime + t == SKIP_FRAME or framesToSkip + t == SKIP_FRAME:
        #    currTime = 0
        ##elif currTime == SKIP_FRAME:
        ##    currTime = tNew - 1
        #elif currTime + t >= SKIP_FRAME:
        #    currTime = ((currTime+t)%SKIP_FRAME)
        #else:
        #    currTime += t
        #else:
        #    currTime = tNew
        

        output.append(tNew)

    print("Expected: ", expected)
    print("Actual: ", output)
    for i in range(len(output)):
        if output[i] != expected[i]:
            print(False)
            return
    print(True)

if __name__ == "__main__":
    main()