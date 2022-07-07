'''
Problem:
Given a list of topics with topic words and a list of strings, return how many times the topic has been mentioned in the strings.

Example:

input:

topics = {"price":['cheap', 'expensive', 'price'], "greeting":['hello','hi','how are you'], "genome":["genomes", "genome"]}

strings = ["Expensive cheap hi Hi how to do are you","PRICE cheap hello! 'how are You'","HOW ARE YOU genomes genome"]

output:
{"price":4, "greeting":5, "genome":2}
'''
from collections import Counter, defaultdict
import re

def wordCount(topics, strings):

    wordMap=defaultdict(int)

    wholeTxt = " ".join(strings).lower()

    wordMap.update(Counter(re.findall(r'\w+',wholeTxt)))

    res=defaultdict(int)

    for topic in topics:
        for word in topics[topic]:
            if len(word.split())>1:
                for i in strings:
                    res[topic]+=i.lower().count(word.lower())
            else:
                res[topic]+=wordMap[word]
                
    return res

if __name__ == '__main__':
    topics = {"price":['cheap', 'expensive', 'price'], "greeting":['hello','hi','how are you'], "genome":["genomes", "genome"]}

    strings = ["Expensive cheap hi Hi how to do are you","PRICE cheap hello! 'how are You'","HOW ARE YOU genomes genome"]

    res = wordCount(topics, strings)
    
    print(res)
