def cek_palindrom(kata):
    kata = kata.lower()
    reversed = kata[::-1]
    if kata == reversed:
        return print("eureeka!")
    return print("suka blyat")

list_kata = ["Angsa", "KataK", "kasur empuk", "Aku Suka Kamu", "Ibu Ratna Antar Ubi."]

for x in list_kata:
    cek_palindrom(x)
    