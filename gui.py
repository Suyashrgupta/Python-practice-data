picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]]

ans = r""
for i in picture:
    for j in i:
        if(j):
            ans+="*"
        else:
            ans+=" "
    ans+="\n"
print(ans)