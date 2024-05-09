
from collections import Counter

def count_character_frequency(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        character_frequency = Counter(data)
        return character_frequency

# Example usage
file_path = './regulamento.txt'
frequency = count_character_frequency(file_path)
print(frequency)
sorted_frequency = frequency.most_common()[::-1]
print(sorted_frequency)


