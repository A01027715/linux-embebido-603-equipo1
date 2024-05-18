import os

def find_available_Serial_ports() -> list[str]:
    dev_files = os.listdir('/dev/')
    # Filtrar y retornar aquellos que comienzan con 'ttyA'
    return [file for file in dev_files if file.startswith('ttyA')]

# Llamada a la función para probarla
print(find_available_Serial_ports())


