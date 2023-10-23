import os
import unittest
from dataProcessor import read_json_file
from dataProcessor import add_attribute_to_json_file



class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
        
        self.assertIsNotNone(data)  # Arquivo JSON vazio.
        self.assertEqual(data[0]['name'], 'Jacob Lopez')
        self.assertEqual(data[1]['age'], 27)
        
        for obj in data:
            self.assertIsNotNone(obj['age'])  # Verifica se a idade não é nula
            self.assertIsInstance(obj['age'], int)  # Verifica se a idade é um número inteiro
            self.assertIsNotNone(obj['country'])  # Verifica se o pais não é nulo
            self.assertIsInstance(obj['country'], str)  # Verifica se o pais é uma string

    def test_add_attribute_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")
        
        add_attribute_to_json_file(file_path, 'attr', 'value')
        
        data = read_json_file(file_path)
        
        for obj in data:
            self.assertEqual(obj['attr'], 'value')


    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")
            

if __name__ == '__main__':
    unittest.main()