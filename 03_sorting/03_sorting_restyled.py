# According on dicts cannot be sorted by value as they have no order I used this module.
# Empty prints used to improve readability of outputs.
import operator

LIMIT = 10  # Selective global constant. Can be changed of your choice manually
s = """The Zen of Python, by Tim Peters

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
# Creating dict where: key = chars, value - occurrence number.
d = {_: s.count(_) for _ in s}
print(d)
print

# Sorted by alphabet.
for _ in sorted(d):
    print(_, d[_])

print
# Sorted by occurrence(reversed for an output from greater to lower)
for _ in sorted(d.items(), key=operator.itemgetter(1), reverse=True):
    print(_)
print

# Optional task global constant:
for _ in sorted(d)[:LIMIT]:
    print(_, d[_])
