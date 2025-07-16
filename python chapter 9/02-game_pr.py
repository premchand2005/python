def game():
    return 8581
score = game()
with open('hiscore.txt','r') as f:
    hiscorestr = f.read()
    
if hiscorestr == ' ':
    with open('hiscore .txt','w') as f: 
        f.write(str(score))
        
elif int(hiscorestr)<score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))           