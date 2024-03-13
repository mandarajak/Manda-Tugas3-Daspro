def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)
    return merged_dict


jadwalDasproIf2 = {
    "Senin": "logika matematika",
    "Selasa": "Dasar Pemrograman",
    "Rabu": "matematika diskrit",
}

jadwalDasproIf3 = {
    "Kamis": "Algoritma dan Struktur Data",
    "Jumat": "Dasar Pemrograman",
    "Sabtu": "Pemrograman Web",
}


result_dict = merge_dicts(jadwalDasproIf2, jadwalDasproIf3)


print("Hasil Penggabungan:")
print(result_dict)
