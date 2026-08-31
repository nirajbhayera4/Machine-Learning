#to write the code shorter and cleaner 
#we use comprehensions 

#THE THREE CONCEPTS ARE :
#1. COMPREHENSIONS 
#2. LAMBDA FUNCTIONS
#3. MAP, FILTER, REDUCE

#1. COMPREHENSIONS 

#there are three types of comprehensions 
        #1. list comprehension

        #2. set comprehension
        #3. dictionary comprehension
        
        
#normal way of writing a list is :
numbers=[1,2,3]
ans=[]
for i in numbers :
    ans.append(i*i)
print(ans)

# 1. list comprehensions
ans=[i * i for i in numbers]
print(ans)
