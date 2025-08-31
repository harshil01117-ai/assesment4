try:
    f=open('sample.txt', 'r')
    rf=f.read()
    print(rf)
    f.close()
except FileNotFoundError:
    print("file 'sample.txt' not found")
