from api.library import *

def main ():
    S_MIN = 1000000
    SUB_ALIM = 120000
    SUB_TRANS = 80000
    BONO = 50000
    nombre = input("Digite nombre del empleado ==> ")
    salario = int(input("Digite el salario mensual del empleado ==> "))
    diaslaborados = int(input("Digite la cantidad de dias laborados por el empleado ==> "))
    s_pagar = calcularsueldo(salario, diaslaborados)

    if salario < (S_MIN * 2):
        s_pagar = s_pagar + SUB_ALIM + SUB_TRANS
    else:
        s_pagar = s_pagar + BONO
    
    print(f"El sueldo del empleado: {nombre} es: {s_pagar:.0f}")



if __name__ == "__main__":
    main()