import  re
cadena="aprender expresiones regulares"
textoBuscar="aprender"
textoEncontrado=re.search(textoBuscar, cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

cadena2="Expresiones regulares en python"
textoBuscar2="python"
print(len(re.findall(textoBuscar2, cadena2)))

#-----------------
codigo1="lfjslfjñlsajdfkjsk71df"
codigo2="lksahgoirthnolgbmdlñfgñv.gn"
codigo3="kjslñijonlgdfgrggv"

if re.search("71", codigo1):
    print("Se ha encontrado el nombre")
else:
    print("no se ha encontrado el nombre")
