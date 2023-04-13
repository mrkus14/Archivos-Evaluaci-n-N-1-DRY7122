import json

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

info_personal = {
    "nombre": nombre,
    "apellido": apellido
}

info_personal_json = json.dumps(info_personal)

print("Información en formato JSON:")
print(info_personal_json)
