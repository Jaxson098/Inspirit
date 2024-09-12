def write_dict_to_files(input_dict):
    for key, value in input_dict.items():
        filename = f"{key}.txt"
        
        with open(f"/home/jaxson/Inspirit/rawText/trump/{key}.txt", 'w') as file:
            for item in value:
                file.write(f"{item}\n")

# Example usage
my_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "colors": ["red", "yellow", "pink"],
    "numbers": [1, 2, 3, 4, 5]
}

write_dict_to_files(my_dict)
