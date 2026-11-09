
g={}

while True:
    try:
        item = input()

        if item in g:
            g[item]+=1
        else:
            g[item]=1
        
    except EOFError:
        for item in sorted(g):
           print( g[item],item.upper())
        break
