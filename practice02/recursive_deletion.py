def num(input,str):
    if len(input)==0 and len(str)==0:
        return True
    if len(str)==0:
        return False
    while(len(input)!=0):
        index=input.find(str)
        if (index==(-1)):
            return False
        
        input=input[0:index] + input[index +len(str):]
        return True
    
if __name__ == "__main__":
    input ='GEEGEEKSKS'
    str ='GEEKS'
    print (num(input, str))