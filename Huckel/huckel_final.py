import huckel_main
import visualization
a = input("is the system a open chain or monocyclic(y/n):").strip().lower()
if not(a == "y") and not(a == "n"):
    print("invalid input,enter either(y/n):")
if a == "y":
    x = int(input("enter the number of atoms:"))
    y = input("open chain or monocyclic(o/c)").strip().lower()
    eval,evec = huckel_main.fun(x,y)
    b = input("visualize the orbitals(y/n):").strip().lower()
    if not(b=="y") and not(b=="n"):
        print("invalid input,enter either(y/n):")
    if b == "y":
        visualization.p_o(x,y)
    elif b == "n":
        print(eval)
        print(evec)
elif a== "n":
    n = int(input("enter the order of the adjacency matrix"))
    print("input the adjacency matrix")
    m = [] 
    for i in range(n): 
        row = input(f"Row {i+1}: ").split() 
        m.append(row)
    eval,evec = huckel_main.fun_n(m)
    print(eval)
    print(evec)