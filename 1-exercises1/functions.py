from datetime import date

# 1. 💰 Calculadora de tip
def calculate_tip(mount, porcent):
    tip = mount*(porcent/100)
    return (tip)
total = calculate_tip (100, 0.15)
print(total)

# 2. 📏 Conversor de unidades  
def meters_to_kilometers(meters):
    kilometers = meters/1000
    return kilometers
metros = meters_to_kilometers(1500)
print(metros)

# 3. ✉️ Generador de email empresarial 
def create_email(nombre, apellido, dominio):
    email = (nombre+"."+apellido+"@"+dominio).lower()
    return email
email1 = create_email("Lucia","Gomez","empresa.com")
print(email1)

# 4. 🧾 Precio con impuestos  
def final_price(precio_base, iva=0.21):
    total_iva = precio_base*iva
    total = total_iva + precio_base
    return total
totalPrice = final_price(100)
print(totalPrice)

# 5. 🔐 Simulador de login  

def validate_login(usuario, contraseña):
    register_user = "admin"
    register_password = "1234"
    if usuario == register_user and contraseña == register_password:
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Credenciales incorrectas") 
        return False
validate_user = validate_login("admin","1234")


# 6. 🧑‍💻 Generador de nombre de usuario  
def generate_username(nombre, nacimiento):
    num1 = nacimiento % 100
    name_yy = f"{nombre}{num1}"
    return name_yy.lower()
name_and_yy = generate_username("Lucas",1997)
print(name_and_yy)

# 7. ✨ Formateador de nombres  
def format_name(nombre_completo):
    name_complete = nombre_completo.title()
    return name_complete
name2 = format_name("juan perez")
print(name2)

# 8. 🎂 Calculadora de edad  
def calculate_age(año_nacimiento):
    date_actual = date.today().year
    return date_actual - año_nacimiento
age = calculate_age(2000)
print(age)

# 9. 📞 Validación de número telefónico  
def validate_phone(numero):
    digitos = 0
    string = str(numero)
    for i in string:
        if i.isdigit():
            digitos += 1
    if digitos == 10:
        return True
    else:
        return False
number = validate_phone("1234567890")
print(number)      

# 10. 🧠 Notas de estudiantes  

def student_average(nombre, nota1, nota2, nota3):
    print(f"{nombre}: Promedio = {((nota1+nota2+nota3)/3):.2f}")
    
i = student_average("Ana",8,9,7)
print(i)
    
