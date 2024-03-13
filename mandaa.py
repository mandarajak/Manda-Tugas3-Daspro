data_dictionary = {
    'manda': '81205',
    'rafika': '11010',
    'acha': '17030',
    'nabila': '27453',
    'wahdania': '23765',
    'titin': '87654',
    'diva': '76542',
    'nayla': '12865',
    'ela': '67542',
    'serly': '76543'
}

def login(username, password):
    if username in data_dictionary and data_dictionary[username] == password:
        return f"Selamat datang, {username}!"
    else:
        return "Data yang dimasukkan salah."

username = input("Masukkan username: ")
password = input("Masukkan password: ")

result = login(username, password)
print(result)
