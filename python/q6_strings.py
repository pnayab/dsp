# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    if count >=10:
        donuts = 'Number of donuts: many'
    else: 
        donuts = 'Number of donuts:' + str(count)
    return donuts


    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    newstr = ""
    if len(s) > 2:
        newstr = s[:2] + s[-2:]       
    return newstr
    raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    newstr = ""
    newstr += s[0]
    for i in range(1, len(s)):
        if s[i] == s[0]:
            newstr += '*'
        else:
            newstr += s[i]
    return newstr

    raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
     newstr = ""
    newstr += b[:2]
    newstr += a[2:]
    newstr += " "
    newstr += a[:2]
    newstr += b[2:]
    return newstr
    raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    newstr = s
    if len(s) >= 3:
        if s[-3:] == "ing":
            newstr += "ly"
        else:
            newstr += "ing"
    return newstr
    raise NotImplementedError


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    substr1 = "not"
    substr2 = "bad"
    newstr = ""
    if (substr1 in s) and (substr2 in s):
            a = s.find(substr1)
            b = s.find(substr2)
            if b > a:
                newstr += s[:(a-1)]
                newstr += " good"
                newstr += s[(b+3):]
            else:
                newstr = s
    else:
        newstr = s
                
    return newstr
    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    
    
    newstr1 = ""
    newstr2= ""
    str1=""
    newstr1 = split_half(a)
    newstr2 = split_half(b)
    str1 += newstr1[0] + newstr2[0] + newstr1[1] + newstr2[1]
    return(str1)

def split_half(a):
    halfa = len(a)/2.00
    a1=""
    a2=""
    if (len(a)%2 == 0):
        a1 += a[0:int(halfa)]
        a2 += a[int(halfa):(len(a))]   
    else:
        half = int(halfa) + 1
        a1 += a[:half]
        a2 += a[half:]
    return (a1,a2)
    
    
    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
