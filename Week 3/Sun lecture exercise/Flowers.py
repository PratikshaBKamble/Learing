def flower():
    f = str(input("Please enter name of flower"))
    fl=f.capitalize()
    if (fl=="Rose"):
        print("Roses are red")
    elif(fl=="Lotus"):
        print("Lotus are pink")
    elif(fl=="Waterlily"):
        print("Waterlily are white")
    elif(fl=="Sunflower"):
        print("Sunflower is yelllow")
    else:
        print("Inavlid input")
flower()