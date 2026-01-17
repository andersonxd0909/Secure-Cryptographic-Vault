#pip install Faker
#Email Temporal 10 min mail

# --- GENERADOR DE IDENTIDADES ---
from faker import Faker

# Configuramos datos en español
fake = Faker('es_ES')

def generar():
    print("-" * 25)
    print(f"Nombre:    {fake.name()}")
    print(f"Email:     {fake.email()}")
    print(f"Dirección: {fake.address().replace('', '')}")
    print(f"Clave:     {fake.password(length=12)}")

# Pedir cantidad al usuario
try:
    # Usamos int(input()) para que el número funcione en el bucle for
    pregunta = input("¿Cuántas identidades quieres generar?: ")
    cantidad = int(pregunta)
    
    for i in range(cantidad):
        print(f"\n[ PERFIL #{i+1} ]")
        generar()
        
except ValueError:
    print("\n[!] Error: Por favor, escribe un número (ejemplo: 5).")

print("\nProceso terminado.")