import pickle

lista_nombres=["Lily", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del (fichero_binario)