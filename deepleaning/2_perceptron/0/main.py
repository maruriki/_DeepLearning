#全加算回路
import g

def halfaddr(x1,x2):
    c=g.AND(x1,x2)
    oout=g.OR(x1,x2)
    nout=g.NOT(c)
    s=g.AND(oout,nout)
    return c,s

if __name__=="__main__":
    x0=int(input("x1="))
    x1=int(input("x2="))
    pc=int(input("x3="))
    c0,s0=halfaddr(x0,x1)
    c1,s1=halfaddr(s0,pc)
    c=g.OR(c0,c1)
    print(c,s1)
                 