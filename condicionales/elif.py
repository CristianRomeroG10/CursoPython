
ingeso_mensual = 820000
gasto_mensual = 81000

#Elif e if anidados

if ingeso_mensual > 10000: 
   print("estas bien economicamente en cualquier parte del mundo") 
   if ingeso_mensual - gasto_mensual < 0:
       print("estas en deficit")
   elif ingeso_mensual - gasto_mensual > 3000:
       print("ahora si estas bien")
   else:
       print("Ey pa, estas gastando una banda, hay que ver si te alcanza")
elif ingeso_mensual > 1000:
    print("Esta bien economicamente en latino america")
elif ingeso_mensual > 500:
    print("Esta bien economicamente en Argentina")
elif ingeso_mensual > 200:
    print("Esta bien economicamente en Venezuela")
else: 
    print("Eres pobre")