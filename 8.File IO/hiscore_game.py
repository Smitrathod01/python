def game():
    return 78

score=game()

with open("highscore.txt","r") as f:
    hiscore=f.read()

if score>int(hiscore): #we nare assuming that hiscore txt never blank otherwie write that in elif and copy paste code for write. 
    with open("highscore.txt","w") as f:
        f.write(str(score)) #because write fun is used for strings.