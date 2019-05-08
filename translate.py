
def translate(s):
    out = ''
    s = s.split(" ")
    print(s)
    for i in range (len(s)):
        if s[i] == "p0h\n" or s[i] =="p0h":
            out+=';'
        elif s[i] == '$':   #comment
            out+='//'
        elif s[i] == "b174n6":
            out+='int '
        elif s[i] == "l0d1":
            out+='main'
        elif s[i] == "lut4n6":
            out+='float'
        elif s[i] == 'p4s0k':  #input
            out+='scanf'
        elif s[i] == 'l4b45':  #output
            out+='printf'
        elif s[i] == 'b471k':
            out+='return '
        elif s[i] == 'h4b4n6':
            out+='while'
        elif s[i] == '':
            out+= ' '
        else:
            out+=s[i]
        out+=' '
    out+='\n'
    return out
out = ''
out = '#include <stdio.h>\n'
str = input("Enter j3j3 file name: ")
inp = open(str + ".txt","r")
output = open(str + ".c", "w+")
inp = [i for i in inp.readlines()]
for i in range(len(inp)):
    translate(inp[i])
    out+=translate(inp[i])
output.write(out)

