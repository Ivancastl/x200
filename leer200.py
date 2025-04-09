import os

# Ruta base donde está el script
base_path = os.path.dirname(os.path.abspath(__file__))

# Carpeta que contiene los archivos .txt
directory_path = os.path.join(base_path, "data")

def buscar_y_mostrar_coincidencias(file_path, keyword):
    """Busca líneas que contengan la palabra clave y las muestra en la consola."""
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword.lower() in line.lower():
                print(line.strip())  # ✅ Ya no muestra la ruta
                count += 1
    return count

def main():
    keyword = input("Introduce la palabra clave para buscar: ")

    total_coincidencias = 0

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            print(f"\nBuscando en {filename}...")

            coincidencias = buscar_y_mostrar_coincidencias(file_path, keyword)
            print(f"Coincidencias en {filename}: {coincidencias}")

            total_coincidencias += coincidencias

    print(f"\nTotal de coincidencias encontradas: {total_coincidencias}")

if __name__ == "__main__":
    main()
