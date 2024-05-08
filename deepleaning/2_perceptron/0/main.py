#半加算回路
import g

def halfaddr(x1,x2):
    c=g.AND(x1,x2)
    oout=g.OR(x1,x2)
    nout=g.NOT(c)
    s=g.AND(oout,nout)
    return c,s

if __name__=="__main__":
    x1=input("x1=")
    x2=input("x2=")
    ha=halfaddr(x1,x2)
    print(ha)