Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#logical
a=3
b=6
a<b and b>a
True
>>> a<=b and b>=a
True
>>> a!=b and a==
SyntaxError: invalid syntax
>>> a!=b and a==b
False
>>> a<b or b>a
True
>>> a>b or b>a
True
>>> a!=b or a==b
True
>>> a!=b and a==b
False
>>> a<b or b>a
True
>>> a>b or b>a
True
>>> a<=b or b>=a
True
>>> not True
False
>>> not False
True
>>> #identify
>>> a=3
>>> type(a) is int
True
>>> type(a) is not int
False
>>> a="python"
>>> type(a) is str
True
>>> b=6+9j
>>> type (b) is complex
True
>>> #membership
>>> a=2,3,4,5,6,7,8,9
>>> 9 in a
True
>>> 10 in a
False
>>> 10 not in a
True
