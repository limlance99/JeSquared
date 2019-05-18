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
            
            if s[j][i] == "p0h\n" or s[j][i] =="p0h":
                out+=';'
            elif s[j][i] == '$':   #comment
                out+='//'
            elif s[j][i] == "b174n6":
                out+='int '
            elif s[j][i] == "l0d1m0n":
                out+='main'
            elif s[j][i] == "lut4n6":
                out+='float'
            elif s[j][i] == 'p450k':  #input
                out+='scanf'
            elif s[j][i] == 'l4b45':  #output
                out+='printf'
                toPrint +=1
            elif s[j][i] == 'b471k':
                out+='return '
            elif s[j][i] == 'h4b4n6':
                out+='while'
            elif s[j][i] == 'kUn6':
                out+='if'
            elif s[j][i] == 'ed1':
                out+= 'else'
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

