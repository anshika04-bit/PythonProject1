from typing import final

h=("hello ducat india this is python programming")
print(len(h))
t=h.count(" ")# space count krega
print(t)
print(len(h)-t)
print(h.title())
print(h.upper())
print(h.lower())
print(h.capitalize())
t=h.split()#space se tutega
print(len(t))#direct to nhi word count hoga esliye split use kiya h
t=h.split()
t.remove("ducat")#tod ke data ko join
k=" ".join(t)
print(k)
print(h.startswith("hello"))
print(h.endswith("programming"))
print(h.replace("hello","an",1))
#original data me change nhi krega immuteable
t=h.split()

# k=0
# for i in range(0,len(t)):
#     if(t[i]-'ducat'):
#         k+=1
#         if(k-2):
#             t[i]- 'rama'
#
# h=" ".join(t)
# print(h)
t=h.split()#phle toda then
t.sort()# alphabetic charachter 
g=" ".join(t)
print(g)
h= ("hello ducat india this is python programming")
t=h.split()
k=[]
for i in t:
    k.append(i[::-1])
    final_string=" ".join(k)
    print(final_string)





h="hello"
print(h.isalpha())
print(h.isnumeric())
print(h.isupper())
print(h.islower())
h="hello ducat india"
t=h.split()
k=[]
p=i[-1]+i[1:-1]+i[0]
k.append(p)
k=" ".join(p)
print(p)

h="hello ducat india"
print(h.center(50))


#print ke age piche se special character ko htana
h="@hello ducat india@"
print(h.strip('@'))
print(h.lstrip('@'))#aage se htaya
print(h.rstrip('@'))#piche se htaya
h = " hello ducat india "
t = h.strip()                # Strip → starting aur ending ke spaces hata deta hai
print(t.endswith('india'))

h="hello ducat india my sky this rythm"# aisa word find out vowel character na ho
t=h.split()
vowels = "aeiouAEIOU"
k=[]

for i in k:
    if not any(ch in vowels for ch in word):   # agar word me koi vowel nahi hai
        result.append(word)

print("Words without vowels:", result)


