def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for i in range(steps + 1):
        gradient_derv = 2*a*x0 + b
        x0 = x0 - lr*gradient_derv

    return x0
    
    pass