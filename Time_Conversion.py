#submitted succesfully 

time = str(input())
( digit , join_elements ) = time.split(":",1)



if "AM" in join_elements:
    if "12" in digit:
        digit = "00"
    else:
        digit=str(digit)





if "PM" in join_elements:
    if (int(digit) == 12):
        digit = "00"
    
    if ( int(digit) < 12 ):
        digit = int(digit) + 12
        digit = str(digit)


output_time = str(digit) + ":" + join_elements
print(output_time[0:8])
