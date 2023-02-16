from User import *


u1 = User('Juan')
u2 = User('maria') # No se crea... sigue siendo juan
u3 = User('Jose')# No se crea... sigue siendo juan
a1 = Admin() 
a2 = Admin() # No se crea

print("u1 == u2 ? :", str(u1 == u2))
print("u3 is u2 ? :", str(u3 is u2))
print("User == Admin? ", str(a1 == u1))
print("admin1 == admin2 ", str(a1 == a2))
print("u2.usrname == u1.usrname ? :", str(u2.username == u1.username))

print(u1.username)
print(u2.username)
print(u3.username)

