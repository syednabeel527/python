i = 1
while i <= 10:
    if i%3==0:
        i += 1   # no need for break
        continue  # replace continue when using break here 
    print(i)
    i += 1