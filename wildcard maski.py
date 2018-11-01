while True:
    sub = "";smaski = input("Sláðu inn subnetmaska(með punktum): ");subnetmaski = smaski.split(".");
    for x in subnetmaski:
        if 0 <= eval(x) <= 255:run = False
        else:run = True;break
        sub += str(abs(eval(x)-255))+"."
    if run == False:break;print("reyndu aftur")
print(sub[:-1])
    
    
