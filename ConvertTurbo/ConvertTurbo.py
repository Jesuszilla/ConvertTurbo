import io
import os
import re
import sys

'''
Modify this parameter to skip 1 in x frames. In the default,
4, this would skip 1 frame every 4 frames.

So, [5,3,4,3,4,4,1] would become [4,2,3,3,3,3,0].
'''
SKIP_FRAME = 4

'''
Modify this parameter to modify the range of animations which
will be converted to turbo. The first argument is the start
animation, and the second is the end animation
'''
ANIM_RANGE = range(200,3999)

'''
Modify this parameter to specify a list of ranges to ignore.
For example, to ignore animations in [0,42] and [700,799]:

IGNORE_RANGES = [range(0,42), range(700,799)]
'''
IGNORE_RANGES = [range(700,726)]

##################################################
#          DO NOT MODIFY ANYTHING BELOW          #
##################################################

ANIM_BEGIN_REGEX = re.compile("\[\s*begin\s+action\s+\d+\s*\]", re.IGNORECASE)
ANIM_NUMBER_REGEX = re.compile("\d+")
NUMBER_START_REGEX = re.compile("\s*\d+")

BASE     = "{0},{1}, {2},{3}, {4}\n"
BASEOPT  = "{0},{1}, {2},{3}, {4}, {5}\n"
BASEOPT2 = "{0},{1}, {2},{3}, {4}, {5}, {6}\n"
BASEOPT2 = "{0},{1}, {2},{3}, {4}, {5}, {6}, {7}\n"

# Test cases
#input = [5,3,4,3,4,4,1]
#expected = [4,2,3,3,3,3,0]
#input = [4,3,4,3,4,4,1]
#expected = [3,3,3,2,3,3,1]
#input = [4,4,4,4,4,4,4]
#expected = [3,3,3,3,3,3,3]
#input = [5,4,5,4,5,4,5]
#expected = [4,3,4,3,4,3,3]
#input = [1,1,1,1,1,1,1]
#expected = [1,1,1,0,1,1,1]

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: ConvertTurbo.py input_file output_file")

    input,output = sys.argv[1:]

    with open(input,'r') as f:
        with open(output,'w') as o:
            currTime = 0
            ignoreAnim = False
            for line in f:
                # Start of an animation
                if ANIM_BEGIN_REGEX.match(line):
                    currTime = 0
                    anim = int(ANIM_NUMBER_REGEX.findall(line)[0])
                    # Should we ignore the animation?
                    if anim in ANIM_RANGE:
                        for r in IGNORE_RANGES:
                            ignoreAnim = anim in r
                            if ignoreAnim:
                                break
                    else:
                        ignoreAnim = True
                    o.write(line)
                # Start of an animation element
                elif NUMBER_START_REGEX.match(line) and not ignoreAnim:
                    data = line.split(",")

                    t = int(data[4])

                    # Only do this for positive, non-zero timings
                    if t > 0:
                        tNew = t

                        framesToSkip = int((currTime+t) / SKIP_FRAME)
                        tNew -= framesToSkip
                        currTime = (currTime+t)%(SKIP_FRAME)       
                        data[4] = " " + str(tNew)

                    if not data[len(data)-1].endswith("\n"):
                        data[len(data)-1] = data[len(data)-1] + "\n"
                    o.write(",".join(data))
                else:
                    o.write(line)

if __name__ == "__main__":
    main()