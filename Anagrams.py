import string
str1=input('Enter the first string: ')
str2=input('Enter the second string: ')
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print('Anagrams exists')
else:
    print('No anagrams')
