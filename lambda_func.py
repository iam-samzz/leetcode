hello = lambda x: x*x

print(hello(2))


#in sorting
l = [12,6,0,2,1,3,2,1]

l.sort(key=lambda x: x, reverse= True)
print(l)

l = [[1,2],[1,3],[9,3],[2,5],[100,1],[1,-1]]
l.sort(key = lambda x : (x[0],x[1]),reverse=True)
print(l)