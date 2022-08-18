def evenodd():
    evenlist=[]
    oddlist=[]
    for item in x:
        if item%2==0:
            evenlist.append(item)   
        elif item%2!=0:
            oddlist.append(item)
    print(f"Even numbers: {evenlist}")
    print(f"Odd numbers: {oddlist}")
    


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evenodd()
