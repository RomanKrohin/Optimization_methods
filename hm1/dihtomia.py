def f(x):
    return (1/7)*(x**7)-(x**3)+(1/2)*(x**2)-x


def dihtomia(a, b, eps):
    iterator = 0
    while (((b-a)/2)>eps):
        x1 = (float(b+a)-10**(-10))/2
        x2 = (float(b+a)+10**(-10))/2
        if (f(x1)<=f(x2)):
            b = x2
        else:
            a = x1
        print(f"Итерация - {iterator} | x = {(a+b)/2} | y = {f((a+b)/2)}")
        iterator+=1
        
    
if __name__ == "__main__":
    dihtomia(1, 1.5, 0.05)