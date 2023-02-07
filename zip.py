ls2=[[1,3],[5,7],[7,-1],[4,10],[2,5]]

ls2.sort(key=lambda x:x[1])
print(ls2)


ls2.sort(key=lambda x:x[0])
print(ls2)