file_object = open("c:/test/test.txt","a")
for x in range (0, 11):
    for y in range (0, 11):
        mult = str(x) + " x " + str(y) + " = " + str(x * y)
        print (mult)
        file_object.write (mult)
        file_object.write ('\n')
    print ("-----------------------------------")
file_object.close()