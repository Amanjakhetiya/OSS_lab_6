from scipy.sparse import random,hstack,vstack,tril,triu,issparse

S1 = random(3,4,density=0.75)
S2 = random(3,4,density=0.25)

print(S1.A,end='\n\n')

print(S2.A,end='\n\n')

# horizonatal stack
print(hstack([S1,S2]).toarray(),end='\n\n')

# vertical stack
print(vstack([S1,S2]).toarray(),end='\n\n')

# lower triangular portion
print(tril(S1).toarray(),end='\n\n')

# upper triangular portion
print(triu(S1).toarray(),end='\n\n')

# sparse matrix check
print(issparse(S1)," ",issparse(S2))
