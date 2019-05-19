import re 

def translate(str):
    out = '#include <stdio.h>\n'
    inp = open(str + ".txt","r")
    output = open(str + ".c", "w+")
    s = [i for i in inp.readlines()]
    
    for j in range(len(s)):
        s[j] = s[j].split()
        toPrint = 0
        for i in range (len(s[j])):
            
            if "p0h" in s[j][i]:
                out+= s[j][i].replace('p0h',';')
            elif '$' in s[j][i]:   #comment
                out+= s[j][i].replace('$','//')
            elif "b174n6" in s[j][i]:
                out+=s[j][i].replace('b174n6','int')
                
            elif "l0d1m0n" in s[j][i]:
                out+=s[j][i].replace('l0d1m0n','main')
                
            elif "lut4n6" in s[j][i]:
                out+=s[j][i].replace('lut4n6','float')
                
            elif 'p450k' in s[j][i]:  #input
                out+=s[j][i].replace('p450k','scanf')
                
            elif 'l4b45' in s[j][i]:  #output
                out+=s[j][i].replace('l4b45','printf')
                
                toPrint +=1
            elif 'b471k' in s[j][i]:
                out+=s[j][i].replace('b471k','return')
                
            elif 'h4b4n6' in s[j][i]:
                out+=s[j][i].replace('h4b4n6','while')
                
            elif 'kUn6' in s[j][i]:
                out+=s[j][i].replace('kUn6','if')
            
            elif 'ed1' in s[j][i]:
                out+=s[j][i].replace('ed1','else')
                
            elif s[j][i] == '':
                out+= ' '
            else:
                out+=s[j][i]
            out+=' '
        if(toPrint > 0):
            toPrint = 0
            string = "printf(\"" + "\\" +"n" +"\");"
            out+=string
        out+='\n'
    """ translate(s[j])
    out+=translate(inp[i]) """
    output.write(out)
    print("%s.c successfully created!" %str)

