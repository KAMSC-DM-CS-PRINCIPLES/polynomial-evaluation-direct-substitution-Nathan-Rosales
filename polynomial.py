
def evaluate_polynomial(degree, x, constant_term, *coefficients):
    # TODO: Implement polynomial evaluation using direct substitution method
    # TODO: Print step-by-step evaluation (S0, S1, S2, etc.)
    # TODO: Return final polynomial result

    #if(len(coefficients)!=degree):
     #   raise ValueError("needs " + str(degree) + " coefficient(s)")

    S = constant_term
    k = 1

    a = 0
    while k<=degree:
        num = coefficients[a]
        S += num*(x**k)
        a += 1
        k += 1
    
    return(S)
    

if __name__ == "__main__":
    # TODO: Add main program loop
    # TODO: Get user input for degree, x, constant term, and coefficients
    # TODO: Call evaluate_polynomial function
    # TODO: Ask user if they want to run again

    answer = "y"

    while(answer=="y"):
        degree = int(input("Degree of the polynomial: "))
        x = int(input("Value of x: "))
        constant_term = int(input("Value of constant term: "))

        coefficients = ()

        for i in range(1, degree+1):
            coefficients += (int(input(f"Coefficient of the x^{i} term: ")),)
        
        print("")
        print("P(x) = " + str(evaluate_polynomial(degree, x, constant_term, coefficients)))
        print("")
        answer = input("Do you want to evaluate another polynomial? (y/n): ")
        print("")