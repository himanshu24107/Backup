# Program 12
n = input("Enter a String:") #GitHub
vowel =0
con = 0
vo = ['a','e','i','o','u']
for i in n:
    if i in ['a','e','i','o','u']:
        vowel = vowel + 1
    else:
        con = con + 1
print(f'No. of Vowels:{vowel}') 
print(f'No. of Consonants:{con}')
#Output: No. of Vowels:2
# No. of Consonants:4
