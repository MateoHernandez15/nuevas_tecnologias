#UH-001/create_register 

user=[]

def user_register(): 
    id = int(input("Agregue su documento"))
    user.append(id)
    name = int(input("Ingrese su nombre"))
    user.append(name)
    last_name = ("Agregue su apellido")
    user.append(last_name)
    email = input("Agregue su email")
    user.append(email)
    password = input("Cree un password de 8 caracteres entre numeros y letras")
    user.append(password)
    print("Usuario creado exitosamente")
    print(user)