#creatring sentence using context free grammar
import random

#here are my rules of my grammar
rules = {
"start" : [["to","action","material"]],
"action" : [["cook"],["eat"],["clean"]],
"material" : [["vegetables"],["fruits"]]
}

#createSentence() function generate sentence
def createSentence(start,storage):
    if(start in rules.keys()):
       pickData = random.choice(rules[start])
       for data in pickData:
           createSentence(data,storage)
    else:
       storage.append(start)
    returnString = " "
    returnString = returnString.join(storage)
    return returnString


print(createSentence("start",[]))
