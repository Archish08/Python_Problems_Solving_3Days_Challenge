N=int(input("Enter the Change Amount"))
# int()
# print(type(N))
c100=N//100
N = N%100
c50=N//50
N = N%50
c20=N//20
N = N%20
c10=N//10
N = N%10
c5=N//5
N = N%5
c2=N//2
N = N%2
c1=N
totalNotes=c100+c50+c20+c10+c5+c2+c1
print(totalNotes)
