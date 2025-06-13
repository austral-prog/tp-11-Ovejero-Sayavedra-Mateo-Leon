def read_file_to_dict(filename):
    dict = {}
    with open(filename, 'r') as file:
        content = file.read()
        for l in content.split(';'):
            products = l.split(':')
            try:
                if (products != [] and len(products) >=2):
                    name_product = products[0]
                    value_product = float(products[1])
                    
                    if (name_product not in dict):
                        dict[name_product] = []
                    dict[name_product].append(value_product)
                        
            except Exception:
                pass
    return dict
read_file_to_dict('datos.csv')

def process_dict(datos):
    for producto, valores in datos.items():
        total = sum(valores)
        promedio = total / len(valores)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

datos = read_file_to_dict('datos.csv')
print(process_dict(datos))
