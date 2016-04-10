#!/usr/bin/python

import re
import random
import sys


class MarkovTest():
    
    def __init__(self):

        self.filename = 'all_utf-8.txt'
        self.tempMapping = {}
        self.mapping = {}
        self.starts = []

    def gen_sent(self):
        # KT: changed length here from "1" to "3"
        markovLength = 3
        self.buildMapping(self.wordlist(self.filename), markovLength)
        print(self.genSentence(markovLength))

    def fixCaps(self, word):
        if word.isupper() and word != "I":
            word = word.lower()
            # Ex: "LaTeX" => "Latex"
        elif word [0].isupper():
            word = word.lower().capitalize()
            # Ex: "wOOt" -> "woot"
        else:
            word = word.lower()
        return word

    def toHashKey(self, lst):
        return tuple(lst)

    def wordlist(self, filename):
        f = open(self.filename, encoding='utf-8')
        wordlist = [self.fixCaps(w) for w in re.findall(r"[\w']+|[.,!?;]", f.read())]
        f.close()
        return wordlist

    def addItemToTempMapping(self, history, word):
        while len(history) > 0:
            first = self.toHashKey(history)
            if first in self.tempMapping:
                if word in self.tempMapping[first]:
                    self.tempMapping[first][word] += 1.0
                else:
                    self.tempMapping[first][word] = 1.0
            else:
                self.tempMapping[first] = {}
                self.tempMapping[first][word] = 1.0
            history = history[1:]

    def buildMapping(self, wordlist, markovLength):
        # putting in word here
        self.starts.append(wordlist [0])
        for i in range(1, len(wordlist) - 1):
            if i <= markovLength:
                history = wordlist[: i + 1]
            else:
                history = wordlist[i - markovLength + 1 : i + 1]
            follow = wordlist[i + 1]
            # if the last elt was a period, add the next word to the start list
            if history[-1] == "." and follow not in ".,!?;":
                self.starts.append(follow)
            self.addItemToTempMapping(history, follow)
        # Normalize the values in tempMapping, put them into mapping
        for first, followset in self.tempMapping.items():
            total = sum(followset.values())
            # Normalizing here:
            self.mapping[first] = dict([(k, v / total) for k, v in followset.items()])

    def next(self, prevList):
        sum = 0.0
        retval = ""
        index = random.random()
        # Shorten prevList until it's in mapping
        while self.toHashKey(prevList) not in self.mapping:
            prevList.pop(0)
        # Get a random word from the mapping, given prevList
        for k, v in self.mapping[self.toHashKey(prevList)].items():
            sum += v
            if sum >= index and retval == "":
                retval = k
        return retval

    def genSentence(self, markovLength):
        # Start with a random "starting word"
        curr = random.choice(self.starts)
        # curr = "my"
        sent = curr.capitalize()
        prevList = [curr]
        # Keep adding words until we hit a period
        while (curr not in "."):
            curr = self.next(prevList)
            prevList.append(curr)
            # if the prevList has gotten too long, trim it
            if len(prevList) > markovLength:
                prevList.pop(0)
            if (curr not in ".,!?;"):
                sent += " " # Add spaces between words (but not punctuation)
            sent += curr
        return sent

