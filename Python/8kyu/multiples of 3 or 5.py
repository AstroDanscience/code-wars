'''
f we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

'''

#My solution

def solution(number):
    
    if number<0:    #Return 0 for all negative numbers   
        return 0 
    
    mult=[] #Create empty array for save multiples
    for i in range(number): 
        if i%5==0 or i%3==0:    #If the residue of the division between 3 or 5 is cero, then the number is a multiple
            mult.append(i)  #Add multiple to list
    return sum(mult)    #Return sumatory of multiples

