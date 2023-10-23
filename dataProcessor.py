import json

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    
import json

def add_attribute_to_json_file(file_path, attribute_name, attribute_value):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Adicione o novo atributo em cada objeto do array
        for item in data:
            item[attribute_name] = attribute_value

        # Abra o arquivo JSON no mesmo caminho (modo escrita) e escreva os dados atualizados
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

