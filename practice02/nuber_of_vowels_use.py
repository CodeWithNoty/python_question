# a='GeeksforGeeks'
# v='aeiou'
# count=sum(a.count(vowel) for vowel in v)
# print(count)

def num(n):
    count=0
    v=set('aeiouAIOUE')
    for i in n:
        if i in v:
            count=count+1
    print(count)
num('neerajA')