f1="this.txt"
f2="thisi.txt"

with open(f1) as f:
    f3=f.read()

with open(f2) as f:
    f4=f.read()

if f3==f4:
    print("Identical")

else:
    print("Not")