#dictionary with value as squares between 1 and 20:
def fun():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print(d)
fun()