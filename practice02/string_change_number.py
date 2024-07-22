dict={
    "one" : '1',
    "two" :'2',
    "three"  : '3',
    "four":'4',
    "five": '5',
    "six": '6',
    "seven" : '7',
    "eigth":'8',
    "nine":'9',
    "ten":'10',
}

re="five two five one"
print(re)

res=''.join(dict[ele] for ele in re.split())
print(res)
