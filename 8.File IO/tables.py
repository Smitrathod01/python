for i in range(2,20):
    with open(f"Tables/table of {i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={j*i} \n")
            if j!=10: #this is optional for not printing another 11th line in table folder
                print("\n")