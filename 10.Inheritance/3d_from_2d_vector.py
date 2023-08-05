class C2d:
    def __init__(self,i,j) -> None:
        self.icap=i
        self.jcap=j

class C3d(C2d):
    def __init__(self,i,j,k) -> None:
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"


a=C2d(2,3)
b=C3d(1,3,4)
print(b)

    
        