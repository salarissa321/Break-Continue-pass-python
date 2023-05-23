


#--------------------------------------------
#----------- Break , Continue , Pass ------
#-------------------------------------------


myNumbers = [1,2,3,5,16,10,18,12,15]

# Continue

for number in myNumbers :
    if number == 3 :
        continue
    print(number) # 1,2,3,5,16,10,18,12,15
    print(number) # 1,2,5,16,10,18,12,15

print("-" *50 ) # --------------------------------------------------

# Break

for number in myNumbers :
    if number == 10 :
        break
    print(number) # 1,2,3,5,16,10,18,12,15
    print(number) # 1,2,3,5,16


print("-" *50 ) # --------------------------------------------------


# Pass

for number in myNumbers :
    if number == 10 :
        pass
    print(number) # 1,2,3,5,16,10,18,12,15
    print(number) # 1,2,3,5,16,10,18,12,15





