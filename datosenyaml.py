import yaml


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

info_personal = {
    "nombre": nombre,
    "apellido": apellido
}

info_personal_yaml = yaml.dump(info_personal)

print("Información en formato YAML:")
print(info_personal_yaml)
