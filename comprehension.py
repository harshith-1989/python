zenPython = '''
The Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!
'''


words = zenPython.split(" ")

'''The statement in the list comprehension has to be a single statement, but you could always make it a function call'''

def sanitize(str):
  str = str.replace("\n",'')
  str = str.strip('*-!@#$%^&*')
  str = str.lower()
  return str

''' list comprehensions'''
words = [sanitize(str) for str in words]

''' Dictionary comprehensions'''
count_details = dict({(str, words.count(str)) for str in words})
#print (type(count_details))
frequent_words = [str for str in count_details.keys() if count_details[str]>5 ]

'''You can get the unique values by converting the list to a set.'''
words = set(words)

print (words)
print (count_details)
print (frequent_words)
