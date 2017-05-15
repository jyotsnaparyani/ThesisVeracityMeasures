#!/usr/bin/env python



import sys,math,nltk,itertools

def readFileandReturnAnArray(fileName, readMode, isLower):
    myArray=[]
    with open(fileName, readMode) as readHandle:
        for line in readHandle.readlines():
            lineRead = line
            if isLower:
                lineRead = lineRead.lower()
            myArray.append(lineRead.strip().lstrip())
    readHandle.close()
    return myArray



for line in sys.stdin:
  try:
    line = line.strip()
    #if line!="" and line is not None:
    date = line[-12:]
    line = line[:-12]
    Tokens = nltk.word_tokenize(line)
    cnt = len(Tokens)
    sample_space = cnt * cnt
    if sample_space!=0:
        individual = (float((2 * cnt) - 1)) / (sample_space)
    topicfiles = ["foodtopic1", "foodtopic2", "foodtopic3"]
    for i in topicfiles:
        alphabet = readFileandReturnAnArray(i, "r", True)
        topicId = alphabet.pop(0)
        for subset in itertools.combinations(alphabet, 2):
                if subset.__len__() != 0:
                    first = Tokens.count(subset[0])
                    words = nltk.word_tokenize(subset[0])
                    if(words.__len__()==2):
                        cnt1 = Tokens.count(words[0])
                        cnt2 = Tokens.count(words[1])
                        if (cnt1 == cnt2):
                            first = cnt1
                        elif (cnt1 < cnt2):
                            first = cnt1
                        else:
                            first = cnt2
                    second = Tokens.count(subset[1])
                    words1 = nltk.word_tokenize(subset[1])
                    if (words1.__len__() == 2):
                        cnt1 = Tokens.count(words1[0])
                        cnt2 = Tokens.count(words1[1])
                        if (cnt1 == cnt2):
                            second = cnt1
                        elif (cnt1 < cnt2):
                            second = cnt1
                        else:
                            second = cnt2
                    result = 0
                    if first != 0 and second != 0:
                        intermediate = 2.00/sample_space
                        firstresult = (float(first)) * intermediate
                        secresult = (float(second)) * intermediate
                        combine = float(firstresult) + secresult
                        final = (float(combine)) / (individual * individual)
                        result = math.log(final)
                        print '%s\t%s\t%s' % (topicId, result, date)
  except ValueError:
    continue
