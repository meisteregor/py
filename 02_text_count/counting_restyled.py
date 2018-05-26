# -*- coding: utf-8 -*-
# Appending strings. Triple quotes used for simple copypasting from terminal
# as it was in task and to avoid reading this text from file (it brings undesirable characters
# which are not considered for manipulations with Python Philosophy text).

s1 = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
s2 = "egorgulenkov@gmail.com"
s = s1 + s2

# From now "s" is the main string variable in this script, which will be transforming for our needs
alphabet = "abcdеfjhijklmnopqrstuvwxyz"
# Here it is an interesting case, looks like method is.alpha isn't taking only literals.
# And it gives greater result than when we set 28 letter of an alphabet. So I decided to leave
# this method without any changes
letters = sum(1 for _ in s.lower() if _ in alphabet)
print("Number of letters: {}".format(letters))

vow = "aeiouy"
vowels = sum(1 for _ in s.lower() if _ in vow)
print("Number of vowels: {}".format(vowels))

for c, value in list(enumerate(list(s.swapcase()), 1))[17::18]:
    print "{}{}".format(c, value)

# First two outputs are similar to each other. We are using .lower() not to forget UPPER CASE letters and cycling the
# counter(t). Third output. We feel unchained ridding of the brackets! Inner python function "enumerate" takes 2 args:
# value, counter(1) from which we are going to count to avoid 0,1,2. Enumerate also breaks free from brackets.
# Insight list helps us to cut string into characters, outside - to make stepping by 18 possible. S.swapcase()
# inverting cases of our literals.
