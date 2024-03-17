def f(x):
    return (1/7)*(x**7)-(x**3)+(1/2)*(x**2)-x

def f_prime(x):
    return (x**6)-3*(x**2)+x-1

def f_2prime(x):
    return 6*(x**5)-6 * (x)+1

def newton_method(x, eps):
    iterator = 0
    while (True):
        
        if (abs(f_prime(x)) < eps):
            break
        x_n = x - f_prime(x) / f_2prime(x)
        x = x_n
        iterator+=1
        print(f"Итерация - {iterator} | x = {x} | y = {f(x)}")
        
        

if __name__ == "__main__":
    newton_method(0, 0.05)