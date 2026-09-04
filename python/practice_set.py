#python coding practice 

#STRINGS 
#reverse the string - 
def reverse_string(s):
    return s[::-1]

#check palindrome 
def is_palindrome(s):
    s=s.lower()
    return s==s[::-1]

#count vowels
def count_vowels(s):
    return sum(1 for i in s.lower() if i in "aeiou")


#count frequency 
def count_freq(sentence) :
    freq={}
    for word in sentence.split() :
        freq[word] =freq.get(word, 0) +1
    return freq