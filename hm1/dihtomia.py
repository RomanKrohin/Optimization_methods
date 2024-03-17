def f(x):
    return (1/7)*(x**7)-(x**3)+(1/2)*(x**2)-x


def dihtomia(left, right, eps):
    iterator = 0
    while (((right-left)/2)>eps):
        x1 = (float(right+left)-10**(-10))/2
        x2 = (float(right+left)+10**(-10))/2
        if (f(x1)<=f(x2)):
            right = x2
        else:
            left = x1
        print(f"Итерация - {iterator} | x = {(left+right)/2} | y = {f((left+right)/2)}")
        iterator+=1
        
    
if __name__ == "__main__":
    dihtomia(1, 1.5, 0.05)