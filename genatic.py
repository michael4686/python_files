import random
items=[[1, 2],[2, 4],[3, 4],[4, 5],[5, 7],[6, 9]]
print("Available items:\n", items)
mw = 10
s = 10
mp = 0.2
cp=0.875
g = 10
print("\nGenetic algorithm parameters:")
print("Max weight:", mw)
print("Population:", s)
print("Mutation probability:", mp)
print("Generations:", g, "\n")
print("Performing genetic evolution:")
 
def generate_p(s):
    genes=[0,1]
    p=[]
    for i in range(s):
        c=[]
        for j in range(len(items)):
            c.append(random.choice(genes))
        p.append(c)    
    print("Generated a random population of size", s)
    return p

def calculate_f(c):
    w=0
    t=0
    for i in range(len(c)):
        if c[i]==1:
            w+=items[i][0]
            t+=items[i][1]
    if w>mw:
        return 0
    else:
        return t

def selectc(p):
    f=[]
    for c in p:
        f.append(calculate_f(c))
    for x,y in enumerate(f):
        f[x]=float(y)/sum(f)
    parent1=random.choices(p, weights=f, k=1)[0] 
    parent2=random.choices(p, weights=f, k=1)[0] 
    print("Selected two chromosomes for crossover")
    return parent1, parent2               
    
def crossover(c1,c2):
    point=random.randint(0,len(items)-1)
    ch1=c1[:point]+c2[point:]
    ch2=c2[:point]+c1[point:]
    print("Performed crossover between two chromosomes")
    return ch1, ch2

def mutate(c):
   point = random.randint(0, len(items)-1)
   if c[point]==1:
        c[point]=0
   else:
        c[point]=1   
   print("Performed mutation on a chromosome")
   return c

def get_b(p):
    f=0
    for c in p:
        x=calculate_f(c)
        if x>=f:
            f=x
            ch=c
            
    return ch  
             
p=generate_p(s)
print(p)
for c in p:
    print(calculate_f(c))

ch1=[]
ch2=[]
best = get_b(p)
print(best)
for i in range(g):
    if random.randint(0,1)< cp:   
        ch1,ch2=selectc(p) 
        ch1,ch2=crossover(ch1,ch2)
    if random.uniform(0, 1) < mp:
        ch1 = mutate(ch1)
    if random.uniform(0, 1) < mp:
        ch2 = mutate(ch2)
    p = [ch1, ch2] + p[2:]
print (p)
total_weight = 0
total_value = 0
for i in range(len(best)):
    if best[i] == 1:
        total_weight += items[i][0]
        total_value += items[i][1]
print("\nThe best solution:")
print("Weight:", total_weight)
print("Value:", total_value)

    

             