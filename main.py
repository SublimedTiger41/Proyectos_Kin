import pandas as pd

def creardf():
    df_mamalon = {"Amor_de_mi_vida":["Maria Fernananda Camarena Gonzales"],
                  "Segundo_amor_de_mi_vida":["PCERDA"]}
    return pd.DataFrame(df_mamalon)


if __name__ == "__main__":
    df = creardf()
    print(df)
    #print("Hola mundo")
    #print("La mafer es hermosa")
