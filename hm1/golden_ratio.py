import math

def f(x):
    return (1/7)*(x**7)-(x**3)+(1/2)*(x**2)-x

def golden_ratio(a, b, eps):
    
    tau = (math.sqrt(5)-1)/2
    
    x1 = a + ((3 - math.sqrt(5))/2)*(b-a)
    x2 = a + ((math.sqrt(5) - 1)/2)*(b-a)
    f_x1 = f(x1)
    f_x2 = f(x2)
    eps_n = ((b-a)/2)
    iterator = 1
    while(((b-a)/2)>eps):
        if (f_x1<=f_x2):
            b = x2
            x2 = x1
            f_x2 = f_x1
            x1 = b - tau*(b-a)
            f_x1 = f(x1)
        else:
            a = x1
            x1 = x2
            f_x1 = f_x2
            x2 = a + tau*(b-a)
            f_x2 = f(x2)
        eps_n *= tau
        print(f"Итерация - {iterator} | x = {(a+b)/2} | y = {f((a+b)/2)}")
        iterator+=1

    print((a+b)/2, f((a+b)/2))

if __name__ == "__main__":
    golden_ratio(1.0, 1.5, 0.05)