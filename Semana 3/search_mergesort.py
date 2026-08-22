
# Code
def get_valid_number(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            return int(user_input)
        print("\n\tError: Por favor, ingrese solo dígitos (no letras, espacios ni símbolos).")

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def search_menu(code_list):
    while True:
        target_code = get_valid_number("\n\t\tIngrese el código del producto a buscar: ")

        if binary_search(code_list, target_code):
            print(f"\n\t\tEl código {target_code} ESTÁ registrado.")
        else:
            print(f"\n\t\tEl código {target_code} NO ESTÁ registrado.")

        choice = input("\n\t\t¿Buscar otro código? Ingrese (y) para sí o cualquier otra tecla para volver al menú principal: ").strip().lower()
        if choice != "y":
            break

def main_menu():
    code_list = []

    while True:
        print("\n\t\t--ORGANIZACIÓN Y BÚSQUEDA by FairSociety--")
        print("\n\t\t\t--- MENÚ PRINCIPAL ---")
        print("\n\t1. Registrar / Actualizar códigos de productos")
        print("\t2. Buscar un código en la lista almacenada")
        print("\t0. Salir")

        option = input("\n\t\tSeleccione una opción: ").strip()

        if option == "1":
            count = get_valid_number("\n\t\t¿Cuántos códigos desea ingresar?: ")
            new_codes = []
            
            for i in range(count):
                code = get_valid_number(f"\n\tIngrese el código #{i + 1}: ")
                new_codes.append(code)
            
            code_list = merge_sort(new_codes)
            print("\n\tCódigos ordenados:")
            print(code_list)

            while True:
                choice = input("\n\t¿Desea buscar un producto ahora? y = si, n = no (y/n): ").strip().lower()
                if choice == "y":
                    search_menu(code_list)
                    break
                else:
                    print("\n\tError: Por favor, ingrese (y) para sí o (n) para no.")

        elif option == "2":
            if not code_list:
                print("\n\tNo se encontraron códigos en memoria. Por favor, use la opción 1 primero para registrarlos.")
            else:
                search_menu(code_list)

        elif option == "0":
            print("\n\n\tSaliendo del programa...\n")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main_menu()