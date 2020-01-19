#Ida
ida = int(input("IDA en segundos: "))
ida_h = ida // 3600
resto_ida = ida % 3600
ida_m = resto_ida // 60
ida_s = resto_ida % 60
print("IDA:",ida_h,"(h)",ida_m,"(m)",ida_s,"(s)") 
#Uni
uni = int(input("UNI en segundos: "))
uni_h = uni // 3600
resto_uni = ida % 3600
uni_m = resto_uni // 60
uni_s = resto_uni % 60
print("UNI:",uni_h,"(h)",uni_m,"(m)",uni_s,"(s)") 
#Vuelta
vuelta = int(input("VUELTA en segundos: "))
vuelta_h = vuelta // 3600
resto_vuelta = vuelta % 360
vuelta_m = resto_vuelta // 60
vuelta_s = resto_vuelta % 60
print("VUELTA:",vuelta_h,"(h)",vuelta_m,"(m)",vuelta_s,"(s)") 