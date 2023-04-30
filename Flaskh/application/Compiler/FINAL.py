import re
#--------is even function--------------------------
def isEven(m):
    if m % 2 == 0:
        return True
    else:
        return False
#---------line type return funtion-------------------------
def LineTypeFunc():
    code_lines=[]
    line_type=[]
    c=-1
    int_var=[]
    float_var=[]
    char_var=[]

    tab_count=0
    for line in f:
        c=c+1
        code_lines.append(line[:-1])
        line_type.append(-1)
        line= re.sub('&&',"and",line)
        line= re.sub('\|\|',"or",line)
        line= re.sub('!',"NOT",line)

        if '[' in line and ']' in line:
            if '{' in line:
                line=re.sub('{','[',line)
                line=re.sub('};',']',line)
                a=line
                a=a.split('=')
                #print(a)
                b=a[0].split('[')[0]
                line=b+'='+a[1]
            if 'sizeof' in line:
                line = re.sub("sizeof","len",line)

        #print (line,c)
        #0 - include statements
        if(line[0:8]=="#include"):
            line_type[c]=0

        
        #1 - function
        if(line[0:3] == "int" or line[0:5] == "float" or line[0:4] == "char" or line[0:4] == "void"):
            if( "(" in line and ")" in line):
                line_type[c]=1
            
            

        #2 - variable define
        if(line[0:3] == "int" or line[0:5] == "float" or line[0:4] == "char"):
             if( "(" not in line and ")" not in line):
                 line_type[c]=2


        
        #3 - scan
        if(line[0:4]=="scan"):
            line_type[c]=3
            


        #4 - print
        if(line[0:5]=="print"):
            line_type[c]=4
            
            

        
        #5 - if
        if(line[0:2]=="if"):
            line_type[c]=5


        
        #6 - else if
        


        #7 - else
        if(line[0:4]=="else"):
            if(line[0:7]=="else if"):
                line_type[c]=6
            else:
                line_type[c]=7





        #8 - for
        if(line[0:3]=="for"):
            line_type[c]=8

        



        
        #9 - while
        if(line[0:5]=="while"):
            line_type[c]=9



        
        #10 - arithmetic statement


        
        #11 - do while
        if(line[0:2]=="do"):
            line_type[c]=11


        #12 - switch case
        if(line[0:6]=="switch"):
            line_type[c]=12

        #13 - comment
        if(line[0:2]=="//"):
            line_type[c]=13

        #14 - multi comment
        if(line[0:2]=="/*"):
            line_type[c]=14
    return line_type



f= open ("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\Sample.c",'r')
ff= open ('D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt','w')
ff.write("from math import sqrt\n")
ff.close()
ff= open ('D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt','a')

for line in f:
    ff.write(line)
f.close()
ff.close()


#----------move { to sperate lines------------------------
f=open ("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
ff=open ('D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt','w')

for line in f:
    if 'printf' not in line:
        line=re.sub('{','\n{\n',line)
        line=re.sub('}','\n}\n',line)
    ff.write(line)
f.close()
ff.close()
#--------1. Remove white lines--------------------------
f=open ("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt")
ff=open ('D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt','w')

for line in f:
    if line.isspace()==False:
        ff.write(line)
f.close()
ff.close()
#---------2. Remove spaces before lines-------------------------
f=open ("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt",'w')
ff=open ('D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt')

for line in ff:
    j=0

    if line[0] == " ":
        for i in line:
            j+=1
            if i != " ":
                break
        line1=line[j-1:]
        f.write(line1)
    else:
        f.write(line)

f.close()
ff.close()
   
f=open('D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt')
ff=open('D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt','w')
        
for line in f:          #########correct mistaakke(print case)
    '''if '{' in line:
        a=line
        cn=''
        x=a.split('{')
        x[0]=x[0].strip()+'\n{\n'
        x[1]=x[1].strip()
        for i in x:
            cn+=i
        ff.write(cn)
    else:'''
    ff.write(line)

ff.close()
f.close()
#--------3. Remove extra spaces in function declearation statement--------------------------

f= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
line_type=LineTypeFunc()
f.close()

f=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
ff=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt",'w')
p=0
for line in f:
  

    if line_type[p] !=1:
        #print('a')
        ff.write(line)
    else:
        #print('b')
        a=[]
        w=1
        z = line.split('(')[0].split()
        x = line.split('(')[1].split(",")
        for i in x:
            i=i.lstrip()
            a.append(i)
            
        #print (z)

        b=''

        #print (a)

        for j in a:
            b=b+" "+j
        c=b.split()
        c[-1]=c[-1][:-1]
        #print(c)
        k=z[0]+' '+z[1]+'('
        for e in c:
            if isEven(w):
                k=k+e+','
            else:
                k=k+e+' '
            w+=1
                
            
        line1=k[:-1]+')'
        ff.write(line1+'\n')
    p+=1

ff.close()
f.close()
#--------4. Spaces in assignment operation--------------------------
f=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt",'w')
ff=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt")
line1=''
for line in ff:
    if "print" in line or "scan" in line or "while" in line or "if" in line or "for" in line or "int" in line or "float" in line:
        f.write(line)
    elif "=" in line:
        if "'" not in line or '"' not in line:
            boho = line.split()
            for i in boho:
                if i[0]!=" " and i[-1]!=" ":
                    line1=line1+i
            f.write(line1+'\n')
            line1=''


        elif "'" in line or '"' in line:
            line = z
            line1=''
            i=0
            while i!=len(z):
                if z[i]!=" " and z[i]!=' ':
                    line1=line1+z[i]
                if z[i] == "'" or z[i] == '"':
                    i=i+1
                    break
                i=i+1

            while i!=len(z):
                line1=line1+z[i]
                i=i+1
            
            f.write(line1+'\n')
            line1=''
        
    else:
        f.write(line)
ff.close()
f.close()
#-------5. spaces in variable declearation---------------------------
f= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
line_type=LineTypeFunc()
f.close()
f=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")

ff=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt",'w')
shub=0
for line in f:
    
    if line_type[shub]==2:
        a=line
        b=''
        i=0
        while (i!=len(a)):
            if a[i]!=" ":
                b=b+a[i]
            if a[i] == " ":
                b=b+' '
                i+=1
                break
            i+=1
        while (i!=len(a)):
            if a[i] != ' ':
                b=b+a[i]

            i+=1

        c=b.split(',')
        aa=0
        l=''
        for ex in c:
            if '=' in ex:
                l=l+ex.split('=')[0]+','
            else:
                l=l+ex+','
            #print (l)
        if '=' in line:
            ff.write(l[:-1]+';'+'\n')
        if '=' not in line:
            ff.write(l[:-1])
        

        for aa in range(len(c)):
            if "=" in c[aa]:
                if aa!=0 and aa!=len(c)-1:
                    ff.write(c[aa]+';'+'\n')
                elif aa==len(c)-1:
                    ff.write(c[aa])
                elif aa==0:
                    ff.write(c[aa].split()[1]+';'+'\n')
        

    else:
        ff.write(line)
    shub+=1

ff.close()
f.close()
#--------6. Extra spaces in conditional statements--------------------------
f= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt")
line_type=LineTypeFunc()
f.close()

f=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt")
ff=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt",'w')
shub=0
blank=''

for line in f:
    #if
    if line_type[shub]==5:
        
        for i in line:
            if i!=" ":
                blank=blank+i
        ff.write(blank)
        blank=''

    #while
    elif line_type[shub]==9:
        for i in line:
            if i!=" ":
                blank=blank+i
        ff.write(blank)
        blank=''

    #for
    elif line_type[shub]==8:
        flag = 0 
        if "int" in line:
            flag = 1
        if "float" in line:
            flag = 2
        line= re.sub('int',"",line)
        line= re.sub('float',"",line)

            
        for i in line:
            if i!=" ":
                blank=blank+i
            #print(blank)
        if flag==0:
            ff.write(blank)
            blank=''

        if flag==1:
            ff.write(f'int {blank.split("(")[1].split("=")[0]};\n')    
            ff.write(blank)
            blank=''

        if flag==2:
            ff.write(f'float {blank.split("(")[1].split("=")[0]};\n')
            ff.write(blank)
            blank=''

        
    else:
        ff.write(line)
        blank=''

    shub+=1

        


f.close()
ff.close()
#-------7. spaces in function datatype and function name---------------------------

f= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
line_type=LineTypeFunc()
f.close()

f=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
ff=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt",'w')
shub=0


for line in f:
    if line_type[shub]==1:
        line1 =''

        a=line.split()
        for i in range(0,len(a)):
            line1=line1+a[i]+" "
        ff.write(line1[:-1])
    else:
        ff.write(line)


f.close()
ff.close()
#---------8. Extra spaces in print and scan statements.-------------------------
f= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt")
line_type=LineTypeFunc()
f.close()

f=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt")
ff=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt",'w')
shub=0


for line in f:
    if line_type[shub]==3 or line_type[shub]==4:
        #print('A')
        #if ',' in line:

        if len(line.split('"'))<=3:
            a=line.split('"')
            blank=''
            for i in a[0]:
                if i!=' ':
                    blank+=i
            #print(blank)
            blank=blank+'"'+a[1]+'"'
            for i in a[2]:
                if i!=' ':
                    blank+=i
            ff.write(blank)
        else:            
            blank=''
            ad=0
            flagg=0
            new=0
            for i in range(len(line)):
                if line[i]=='"':
                    flagg=1
                if flagg==0:
                    if(line[i]!=' '):
                        blank=blank+line[i]
                #print(blank)
            while(line[new]!='"'):
                new+=1
            #print(new)
            start1=new

            for j in range(len(line),0,-1):
                if line[j-1]=='"':
                    break
            #print(j)
            end1=j

            while(new!=j):
                blank=blank+line[new]
                new+=1   
            #print(blank)
            #print(j)
            while(j!=len(line)):
                if(line[j]!=" "):
                    blank=blank+line[j]
                j+=1
            #print(blank)
            allx=0
            while(start1+2!=end1-2):
                if(line[start1]=='"'):
                    allx=allx+1
                start1=start1+1
            #print(allx-1)
                            
            task=0



            start=-1
            end=len(blank)
            while(start<len(blank)):
                start+=1
                if blank[start]=='"':
                    break
                                
            #print(start)
            while(end!=0):
                end-=1
                if blank[end]=='"':
                    break
            #print(end)
                        
            blanknew=blank[start+1:end].replace('"','\\"')  

            #print(blanknew)
            ff.write(blank[:start+1]+blanknew+blank[end:])

    else:
        ff.write(line)

    shub+=1

f.close()
ff.close()
#---------9. adding brackets to loops which dont have-------------------------
f= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
line_type=LineTypeFunc()
f.close()

f=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
ff=open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt",'w')
shub=0
fflag=0
bflag=0
for line in f:
    if line_type[shub]==5 or line_type[shub]==6 or line_type[shub]==7 or line_type[shub]==8 or line_type[shub]==9:
        #print('hi')
        if fflag==1:
            ff.write('{\n'+line)
            bflag+=1
        elif fflag==0:
            ff.write(line)
        fflag=1

    elif '{' in line:
        if fflag==1:
            fflag=0
        ff.write(line)

    else:
        if fflag==1:
            ff.write('{\n'+line+'}\n')
            for i in range(0,bflag):
                ff.write('}\n')
            fflag=0
            bflag=0
        elif fflag==0:
            ff.write(line)

    shub+=1

f.close()
ff.close()
#-------------------------------------------------














def mulD(a,h,n,dt):
    print(a,h,n,dt)
    if h==n:
        for t in range (0,int(a[h])):
            if dt=='i':
                if t==int(a[h])-1:
                    print(0)
                    ff.write('0')
                else:
                    print(0,)
                    ff.write('0,')
            elif dt=='f':
                if t==int(a[h])-1:
                    ff.write('0.0')
                else:
                    ff.write('0.0,')
            elif dt=='ch':
                if t==int(a[h])-1:
                    ff.write('""')
                else:
                    ff.write('"",')
            elif dt=='bo':
                if t==int(a[h])-1:
                    ff.write('False')
                else:
                    ff.write('False,')

    else:    
        for i in range(0,int(a[h])):
            ff.write('[')
            print('[')
            mulD(a,h+1,n,dt)
            if i==int(a[h])-1:
                ff.write(']')
                print(']')
            else:
                ff.write('],')
                print('],')



def Tx_Single_Comment(line):
    line = re.sub('//', '#', line)
    for xd in range(0,tab_count):
        ff.write('    ')
    ff.write(line)

#def Tx_Multi_Comment(startline,endline):
    #startline = re.sub('/\*', "'''", startline)
    #endline = re.sub('\*/', "'''", endline)
    #print(startline,endline)
def Tx_Multi_Comment(startline):
    startline = re.sub('/\*', "'''", startline)
    for xd in range(0,tab_count):
        ff.write('    ')
   
    ff.write(startline)
    
def Tx_If(line):
    line=(line+":")
    for xd in range(0,tab_count):
        ff.write('    ')
    ff.write(line)

def Tx_Else(line):
    line=(line+":")
    for xd in range(0,tab_count):
        ff.write('    ')
    ff.write(line)

def Tx_Else_If(line):
    line= re.sub('else if',"elif",line)
    line=(line+":")
    for xd in range(0,tab_count):
        ff.write('    ')
    ff.write(line)

def Tx_For(line):
    #line="for(adepu=0;adepu>100;adepu=adepu+10)"
    a=line[4:-1]
    b=a.split(";")
    c=b[0].split("=")
    intialvalue=c[1]
    finalvalue=-1
    increment_value=1

    if("++" in b[2]):
        increment = "1"
        increment_value = 1
        
    elif("--" in b[2]):
        increment = "-1"
        increment_value = 1

    elif("++" not in b[2] and "+" in b[2]):
        increment = "1"
        increment_value = b[2].split("+")[1]

    elif("--" not in b[2] and "-" in b[2]):
        increment = "-1"
        
        increment_value = b[2].split("-")[1]
        
    if "<=" in b[1]  or ">=" in b[1]:
        finalvalue=b[1].split("=")[1]+'+1'
        

    elif "<" in b[1]:
        finalvalue=b[1].split("<")[1] 
        

    elif ">" in b[1]:
        finalvalue=b[1].split(">")[1] 
        

    elif  "!=" in b[1] and increment=="1":
        finalvalue=b[1].split("=")[1]
        

    elif  "!=" in b[1] and increment=="-1":
        finalvalue=b[1].split("=")[1] 
    finalvalue=str(finalvalue).replace('/','//')
    for xd in range(0,tab_count):
        ff.write('    ')
    ff.write(f'for {b[0].split("=")[0]} in range({intialvalue},{finalvalue},{int(increment)*int(increment_value)}):')


def Tx_While(line):
    line=(line+":")
    for xd in range(0,tab_count):
        ff.write('    ')
    ff.write(line)

def Tx_Function(line):
    #line="int main()"
    #print(line)
    bi=line.split("(")[1][:-1]
    #print(bi)
    d=line.split("(")[0].split()[1]
    if "," in line:
        bi=line.split("(")[1][:-1]
        d=line.split("(")[0].split()[1]

        a=bi.split(",")
        print(bi,d,a)

        c=[]
        for i in a:
            e=i.split()[1]
          
            c.append(e)
            c.append(",")

        c.pop()

        ff.write("def "+d+"(")
        for i in c:
            ff.write(i)
        ff.write("):")

    elif bi=="":
        bi=line.split("(")[1][:-1]
        d=line.split("(")[0].split()[1]
        
        ff.write("def "+d+"():")
    

    else:
        #print("hiii")
        #print(bi.split())
        ff.write("def "+d+"("+bi.split(" ")[1]+"):")

def Tx_Variables(line):
    #line = "char num1,num2,a[777],shubhamchutiy,shubhamyz"
    line=line[:-1]
    x = line.split(" ")
    ln=""
    if(x[0]=="signed" or x[0]=="unsigned"):
        if(x[1] == "int" or x[1] == "float" or x[1] == "char" or x[1] == "double" or x[1] == "long"):
            x.pop(0)
            for i in x:
                ln=x+" "
            Tx_Variables(ln[:-1])
        else:
            b = line.split(" ",1)
            c = b[1].split(",")
            d=[]
            
            j=""
            dt='i'
            for i in c:
                a=[]
                #print(i)
                int_var.append(i)
                if "[" in i and "]" in i:
                    if "][" in i:
                        l= i.split('[')
                        temp=l[0]
                        
                        for bi in range(1,len(l)):
                            a.append(int(l[bi][:-1]))
                        n=len(a)-1
                        for xd in range(0,tab_count):
                            ff.write('    ')
                        ff.write(f'{temp}=[')
                        mulD(a,0,n,dt)
                        ff.write(']\n')
                    else:
                        temp=i.split('[')
                        num=int(temp[1].split(']')[0])
                        #print(num)
                        j=temp[0] + '=['
                        for z in range(0,num):
                            j= j+'0,'
                        j=j[:-1]+']\n'
                else :
                    i = str(i)
                    j = i + '=0'
                d.append(j)    
            for i in d:
                for xd in range(0,tab_count):
                    ff.write('    ')
                ff.write(i+'\n')
            
    if(x[0]=="bool"):
        b = line.split(" ",1)
        c = b[1].split(",")
        d=[]
        
        j=""
        dt='bo'
        for i in c:
            a=[]
            #print(i)
            int_var.append(i)
            if "[" in i and "]" in i:
                if "][" in i:
                    l= i.split('[')
                    temp=l[0]
                    
                    for bi in range(1,len(l)):
                        a.append(int(l[bi][:-1]))
                    n=len(a)-1
                    for xd in range(0,tab_count):
                        ff.write('    ')
                    ff.write(f'{temp}=[')
                    mulD(a,0,n,dt)
                    ff.write(']\n')
                else:
                    temp=i.split('[')
                    num=int(temp[1].split(']')[0])
                    #print(num)
                    j=temp[0] + '=['
                    for z in range(0,num):
                        j= j+'False,'
                    j=j[:-1]+']\n'
            else :
                i = str(i)
                j = i + '=False'
            d.append(j)    
        for i in d:
            for xd in range(0,tab_count):
                ff.write('    ')
            ff.write(i+'\n')
        

    if(x[0]=="int" or x[0]=="long"):
        b = line.split(" ",1)
        c = b[1].split(",")
        d=[]
        
        j=""
        dt='i'
        for i in c:
            #print(i)
            a=[]
            int_var.append(i)
            if "[" in i and "]" in i:
                if "][" in i:
                    l= i.split('[')
                    temp=l[0]
                    
                    for bi in range(1,len(l)):
                        a.append(int(l[bi][:-1]))
                    print(a)
                    n=len(a)-1
                    for xd in range(0,tab_count):
                        ff.write('    ')
                    #ff.write(n)
                    ff.write(f'{temp}=[')
                    mulD(a,0,n,dt)
                    ff.write(']\n')
                else:
                    temp=i.split('[')
                    num=int(temp[1].split(']')[0])
                    #print(num)
                    j=temp[0] + '=['
                    for z in range(0,num):
                        j= j+'0,'
                    j=j[:-1]+']\n'
            else :
                i = str(i)
                j = i + '=0'
            d.append(j)    
        for i in d:
            for xd in range(0,tab_count):
                ff.write('    ')
            ff.write(i+'\n')

    if(x[0]=="float" or x[0]=="double"):
        b = line.split(" ",1)
        c = b[1].split(",")
        d=[]
        
        j=""
        dt='f'
        for i in c:
            a=[]
            float_var.append(i)
            
            if "[" in i and "]" in i:
                if "][" in i:
                    l= i.split('[')
                    temp=l[0]
                    for bi in range(1,len(l)):
                        a.append(int(l[bi][:-1]))
                    n=len(a)-1
                    for xd in range(0,tab_count):
                        ff.write('    ')
                    ff.write(f'{temp}=[')
                    mulD(a,0,n,dt)
                    ff.write(']\n')
                else:
                    temp=i.split('[')
                    num=int(temp[1].split(']')[0])
                    #print(num)
                    j=temp[0] + '=['
                    for z in range(0,num):
                        j= j+'0.0,'
                    j=j[:-1]+']\n'
            else :
                i = str(i)
                j = i + '=0.0'
            d.append(j)    
        for i in d:
            for xd in range(0,tab_count):
                ff.write('    ')
            ff.write(i+'\n')

    if(x[0]=="char"):
        b = line.split(" ",1)
        c = b[1].split(",")
        d=[]
        
        j=""
        dt='ch'
        for i in c:
            a=[]
            char_var.append(i)
            int_var.append(i)
            if "[" in i and "]" in i:
                if "][" in i:
                    l= i.split('[')
                    temp=l[0]
                    for bi in range(1,len(l)):
                        a.append(int(l[bi][:-1]))
                    n=len(a)-1
                    for xd in range(0,tab_count):
                        ff.write('    ')
                    ff.write(f'{temp}=[')
                    mulD(a,0,n,dt)
                    ff.write(']\n')
                else:
                    temp=i.split('[')
                    num=int(temp[1].split(']')[0])
                    #print(num)
                    j=temp[0] + '=['
                    for z in range(0,num):
                        j= j+'""'
                    j=j[:-1]+']\n'
            else :
                i = str(i)
                j = i + '=" "'
            d.append(j)    
        for i in d:
            for xd in range(0,tab_count):
                ff.write('    ')
            ff.write(i+'\n')

def Tx_Printf(line):
    if '",' in line:
        #line='printf("test1=%d, test2=%c, testomegalol=%s, shubhamxx",a,b,c);'

        line=line
        a = line.split('"')
        variable = a[2][:-2].split(',')
        #print(variable)
        newva= variable[1:]

        li= a[1].split("%")


        xxd=[li[0]]

        for i in range(1,len(li)):
            xxd.append(li[i][1:])

            
        #print(li)
        c=0
        for xd in range(0,tab_count):
            ff.write('    ')
        ff.write("print(f'")
        for  i in range (0,len(xxd)-1):
            ff.write(xxd[i])
            ff.write("{"+newva[i]+"}")
            c+=1

        ff.write(li[c][1:]+"')")
    else:
        a = line.split('"')
        linex=a[1]
        for xd in range(0,tab_count):
            ff.write('    ')
        ff.write("print('"+linex+"')")

def Tx_Scanf(line):
    #line = 'scanf("%s,%f,%d,%s",str1,str2,str3,str4);'
    line = line
    a=line.split('"')
    # print(a)
    if len(a[1]) == 2 or len(a[1]) == 3:
        variables = a[2][1:-2].split(",")
        for i in range(0, len(variables)):
            variables[i] = variables[i][1:]        
        if a[1] == '%d':
            for xd in range(0,tab_count):
                ff.write('    ')
            ff.write(variables[i]+" = int(input())")
        elif a[1] == '%f' or var_type[i] == '%lf':
            for xd in range(0,tab_count):
                ff.write('    ')
            ff.write(variables[i]+" = float(input())")
        elif a[1] == '%s':
            for xd in range(0,tab_count):
                ff.write('    ')
            ff.write(variables[i]+" = input()")
        
    else:  
        var_type=a[1].split(",")
        variables = a[2][1:-2].split(",")
        for i in range(0, len(variables)):
            variables[i] = variables[i][1:]
        for i in range(0,len(var_type)):
            if var_type[i] == '%d':
                for xd in range(0,tab_count):
                    ff.write('    ')
                ff.write(variables[i]+" = int(input())")
            elif var_type[i] == '%f' or var_type[i] == '%lf':
                for xd in range(0,tab_count):
                    ff.write('    ')
                ff.write(variables[i]+" = float(input())")
            elif var_type[i] == '%s':
                for xd in range(0,tab_count):
                    ff.write('    ')
                ff.write(variables[i]+" = input()")
            ff.write("\n")
        
        


f= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\bubble.txt")
ff= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt",'w')
code_lines=[]
'''for line in f:
    code_lines.append(line)'''
line_type=[]
c=-1
int_var=[]
float_var=[]
char_var=[]

tab_count=0
for line in f:
    c=c+1
    
    line_type.append(-1)
    line= re.sub('&&'," and ",line)
    line= re.sub('\|\|'," or ",line)
    line= re.sub('!'," not ",line)
    if "=true" in line:
        line=re.sub('=true',"=True",line)
    if "=false" in line:
        line=re.sub('=false',"=False",line)
    code_lines.append(line[:-1])

    if '[' in line and ']' in line:
        if '{' in line:
            line=re.sub('{','[',line)
            line=re.sub('};',']',line)
            a=line
            a=a.split('=')
            #print(a)
            b=a[0].split('[')[0]
            line=b+'='+a[1]
        if 'sizeof' in line:
            line = re.sub("sizeof","len",line)

    #print (line,c)
    #0 - include statements
    if(line[0:8]=="#include"):
        line_type[c]=0

    
    #1 - function
    if(line[0:3] == "int" or line[0:5] == "float" or line[0:4] == "char" or line[0:4] == "void"):
        if( "(" in line and ")" in line):
            line_type[c]=1
        
        

    #2 - variable define
    if(line[0:3] == "int" or line[0:5] == "float" or line[0:4] == "char" or line[0:4] == "bool" or line[0:6] == "double" or line[0:4] == "long" or line[0:6] == "signed" or line[0:8] == "unsigned" ):
         if( "(" not in line and ")" not in line):
             line_type[c]=2


    
    #3 - scan
    if(line[0:4]=="scan"):
        line_type[c]=3
        


    #4 - print
    if(line[0:5]=="print"):
        line_type[c]=4
        
        

    
    #5 - if
    if(line[0:2]=="if"):
        line_type[c]=5


    
    #6 - else if
    


    #7 - else
    if(line[0:4]=="else"):
        if(line[0:7]=="else if"):
            line_type[c]=6
        else:
            line_type[c]=7





    #8 - for
    if(line[0:3]=="for"):
        line_type[c]=8

    



    
    #9 - while
    if(line[0:5]=="while"):
        line_type[c]=9



    
    #10 - arithmetic statement


    
    #11 - do while
    if(line[0:2]=="do"):
        line_type[c]=11


    #12 - switch case
    if(line[0:6]=="switch"):
        line_type[c]=12

    #13 - comment
    if(line[0:2]=="//"):
        line_type[c]=13

    #14 - multi comment
    if(line[0:2]=="/*"):
        line_type[c]=14
#__________________________________________________________

for i in range(0,len(code_lines)):
    ff.write('\n')
    if code_lines[i][0]=='{':
        tab_count+=1
        line_type[i] = -2
    if code_lines[i][0]=='}':
        tab_count-=1
        line_type[i] = -2
    if line_type[i] == -1:
        if code_lines[i][-1:]==';':
            code_lines[i]=code_lines[i][:-1]
        for xd in range(0,tab_count):
            ff.write('    ')
        ff.write(code_lines[i])
    elif line_type[i] == 0:
        for xd in range(0,tab_count):
            ff.write('    ')
        ff.write("#"+code_lines[i])

    elif line_type[i] == 1:
        Tx_Function(code_lines[i])
        
    elif line_type[i] == 2:
        Tx_Variables(code_lines[i])
        
    elif line_type[i] == 3:
        Tx_Scanf(code_lines[i])
        
    elif line_type[i] == 4:
        Tx_Printf(code_lines[i])
        
    elif line_type[i] == 5:
        Tx_If(code_lines[i])
        
    elif line_type[i] == 6:
        Tx_Else_If(code_lines[i])
        
    elif line_type[i] == 7:
        Tx_Else(code_lines[i])
        
    elif line_type[i] == 8:
        Tx_For(code_lines[i])
        
    elif line_type[i] == 9:
        Tx_While(code_lines[i])

    elif line_type[i] == 11:
        ff.write("#do"+code_lines[i])
    elif line_type[i] == 12:
        ff.write("#switch"+code_lines[i])
    elif line_type[i] == 13:
        Tx_Single_Comment(code_lines[i])
    elif line_type[i] == 14:
        Tx_Multi_Comment(code_lines[i])
        temp=i+1
        for k in range(temp,len(code_lines)):
            if '*/' in code_lines[k]:
                line= re.sub('\*/', "'''", code_lines[k])
                line_type[k] = -2
                for xd in range(0,tab_count):
                    ff.write('    ')
                ff.write(line)
                break
            for xd in range(0,tab_count):
                ff.write('    ')
            ff.write(code_lines[k])
            line_type[k] = -2
            

ff.write('main()')

f.close()
ff.close()


f= open("D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\output.txt")
ff= open('D:\\OnlineCompilerUsingCloudComputing\\Flaskh\\application\\Compiler\\pythonoutput.py','w')

for line in f:
    if line.isspace()==False:
        ff.write(line)
        print(line)
f.close()
ff.close()


