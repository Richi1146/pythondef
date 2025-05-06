from datetime import date

# # 1. 💰 Calculadora de tip
# def calculate_tip(mount, porcent):
#     tip = mount*porcent
#     return (tip)
# total = calculate_tip (10000, 0.15)
# print(total)

# # 2. 📏 Conversor de unidades  
# def test_meters_to_kilometers(meters):
#     kilometers = meters/1000
#     return kilometers
# metros = test_meters_to_kilometers(5000)
# print(metros)

# # 3. ✉️ Generador de email empresarial 
# def create_email(nombre, apellido, dominio):
#     email = nombre+apellido+"@"+dominio
#     return email
# email1 = create_email("ricardo","carmona","gmail.com")
# print(email1)

# # 4. 🧾 Precio con impuestos  
# def final_price(precio_base, iva=0.21):
#     total_iva = precio_base*iva
#     total = total_iva + precio_base
#     return total
# totalPrice = final_price(10000)
# print(totalPrice)

# 5. 🔐 Simulador de login  

# def validate_login(usuario, contraseña):
#     register_user = "ricardo"
#     register_password = "12345"
#     if usuario == register_user and contraseña == register_password:
#         return print("usuario valido")
#     else:
#         print("usuario no valido")
# validate_user = validate_login("ricardo","12346")


# 6. 🧑‍💻 Generador de nombre de usuario  
# def generate_username(nombre, nacimiento):
#     num1 = nacimiento % 100
#     name_yy = f"{nombre}{num1}"
#     return name_yy
# name_and_yy = generate_username("ricardo",1997)
# print(name_and_yy)

# 7. ✨ Formateador de nombres  
# def format_name(nombre_completo):
#     name_complete = nombre_completo.title()
#     return name_complete
# name2 = format_name("ricardo carmona")
# print(name2)

# # 8. 🎂 Calculadora de edad  
# def calculate_age(año_nacimiento):
#     date_actual = 2025
#     actual_age = date_actual - año_nacimiento
#     return actual_age
# age = calculate_age(2002)
# print(age)

# 9. 📞 Validación de número telefónico  
# def validate_phone(numero):
#     digitos = 0
#     for i in numero:
#         digitos =+ 1
#     print(digitos)



# 10. 🧠 Notas de estudiantes  

def student_average(nombre, *notas):
    

