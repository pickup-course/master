import sys

def get_coef(prompt, zero=True):
    while True:
        c = input(prompt)
        try:
            res = float(c)
            if zero or res != 0:
                return res
            else:
                raise
        except:
            print("Invalid input!")
    
def get_coefs():
    A = get_coef("Enter coefficient A (non-zero): ", zero=False)
    B = get_coef("Enter coefficient B: ")
    C = get_coef("Enter coefficient C: ")
    return A, B, C

def calc_roots(A, B, C):
    D = B**2 - 4*A*C
    print("D = ", D)
    
    if D < 0:
        return []
    elif D == 0:
        x = -B / (2 * A)
        return [x**0.5, -x**0.5] if x > 0 else ([0] if x == 0 else [])
    else:
        x1 = (-B + D**0.5) / (2 * A)
        x2 = (-B - D**0.5) / (2 * A)
        
        roots = []
        if x1 >= 0:
            roots.extend([x1**0.5, -x1**0.5] if x1 > 0 else [0])
        if x2 >= 0:
            roots.extend([x2**0.5, -x2**0.5] if x2 > 0 else [0])
        
        return roots

def main():
    if len(sys.argv) == 4:
        try:
            A = float(sys.argv[1])
            if A == 0:
                raise
            B = float(sys.argv[2])
            C = float(sys.argv[3])
        except:
            A, B, C = get_coefs()
    else:
        A, B, C = get_coefs()

    res = calc_roots(A, B, C)
    
    if res:
        print("Real solutions of the equation:")
        for root in res:
            print(root)
    else:
        print("No real solutions")

if __name__ == "__main__":
    main()
