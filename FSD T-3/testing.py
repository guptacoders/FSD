# wapp to reverse the content of 


def reverser():
    countv = 0
    with open("testingio.txt","r") as fobj:
        with open("testingio1.txt","w") as fobj1:
            with open("testingio2.txt","w+") as fobj2:
                content = fobj.read().reverse()
                fobj1.write(content)
                fobj2.write(content.upper())
                fobj2.seek(0)
                for i in fobj2.read():
                    if i in "AEIOU":
                        countv+=1
    print(countv)
                    
reverser()
            