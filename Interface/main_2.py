import session as ss
import model_system as ms
import par_hamiltonian as ph
import ob_fr as of

ss.init()
global model_ch
model_ch = 0

def home():
    print(f"Model                 : {ss.ses['mod']['name']}")
    print(f"System                : {ss.ses['sys']['status']}")
    print(f"Parameters            : {ss.ses['par']['status']}")
    print(f"Basis                 : {ss.ses['bas']['status']}")
    print(f"Hamiltonian           : {ss.ses['ham']['status']}")
    print(f"eigenpairs            : {ss.ses["ep"]["status"]} ")
    print()
    print("-"*63)
    print()
    print("1. Model")
    print("2. System")
    print("3. Parameters")
    print("4. Hamiltonian and Eigenpair")
    print("5. Observables")
    print("6. Finite Field Response")
    print("7. Exit")

    return int(input("Choice : "))

while True:
    ch = home()
    match ch:
        case 1:
            ms.model()
        case 2:
            ms.sys()
        case 3:
            ph.parameters()
        case 4:
            ph.hamiltonian()
        case 5:
            of.observables()
        case 6:
            of.finite_field()
        case 7:
            break   

