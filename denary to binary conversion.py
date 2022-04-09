# Denary to Binary converter

binary_conversion_list = [128, 64, 32, 16, 8, 4, 2, 1]
binary_configuration = []

denary_number = int(input("Enter any denary number less than or equal to 255"))
if denary_number > 255:
    print("Exceeds Parameters")
    while denary_number > 255:
        denary_number = int(input("Give another denary value"))

def convertToBinary():
    running_total = denary_number
    binary_configuration = []
    bases_left = 8
    showProcess = 0
    
    answer1 = input("Would you like to show each stage of the process? (Yes/No)")
    if answer1 == "Yes" or "yes":
        showProcess = True
    else:
        showProcess = False
    
    for base in binary_conversion_list:
        if base > running_total: #if the specific binary base (eg 1, 2, 4..) is bigger that what's left of the running total, put 0. This will happen
            bases_left += -1 #records how many bases we have left to do for the 8-bit binary number
            binary_configuration.append("0")
            if showProcess == True:
                print(binary_configuration) 
        elif base <= running_total and running_total > 0: #ensures conditions are right for calculation
            bases_left += -1 #ditto
            binary_output = base // running_total # really only checks that base goes into running total atleast once
            running_total = running_total - (base % running_total) #calculates what's left of the running total
            if binary_output == 1: #this would mean that the base is wholly divisible by the running total
                binary_configuration.append("1") # line 28-33: since this condition is true, this makes the rest of the loop redundant as we know any remaining values will be 0. 
                if showProcess == True:
                    print(binary_configuration)
                for auto in range (bases_left): #using our bases_left variable we can just add the amount of 0s left we need to complete the 8-bit binary number
                    binary_configuration.append("0")
                    if showProcess == True:
                        print(binary_configuration) 
                break #the rest of the code is redundant
            else:
                binary_configuration.append("1")
                if showProcess == True:
                    print(binary_configuration)
            
    print("You're 8-bit binary number is ", str (binary_configuration))
                
                
            
convertToBinary()

    
        
                    