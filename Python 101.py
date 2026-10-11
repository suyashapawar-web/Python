def  print2ndlargest(a, a_size):
    
    
    largest = second_largest = -1233445434
    for i in range(a_size):
        
        
        if (a[i] > second_largest):

            second_largest = largest
            largest = a[i]

        elif (a[i] > second_largest and a[i] != largest):
            second_largest = a[i]

    print(second_largest)

a = [1,2,3,4,5,6,7,8,9]
a_size = len(a)
print2ndlargest(a, a_size)