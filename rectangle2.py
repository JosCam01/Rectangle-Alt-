alt=int(input("Disme altura:"))
amp=int(input("Disme ample:"))

for f in range(alt):

    for c in range(amp):
        if f==0 or c==0 or f==alt-1 or c==amp-1:
            print('* ', end='')
        else:
            print("  ", end="")
    print()
