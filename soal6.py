
list_menu= {
    "Ayam Goreng Krispi" :{   
        "Tipe" : "Makanan",
        "Harga" : 15000
    },
    "Ayam Puk Puk (Bukan di geprek)":{
        "Tipe" : "Makanan",
        "Harga" : 13000
    },
    "Ayam Bakar":{
        "Tipe" : "Makanan",
        "Harga" : 20000
    },
    "Es teh":{
        "Tipe" : "Minuman",
        "Harga" : 15000
    },
    "Es jeruk" :{
        "Tipe" : "Minuman",
        "Harga" : 7000
    },
}



pesanan_rehan = [
    {
        "Menu": "Ayam Bakar",
        "qty": 2
    },
    {
        "Menu": "Es teh",
        "qty": 1
    },
]

pesanan_roni = [
    {
        "Menu": "Ayam Puk Puk (Bukan di geprek)",
        "qty": 1
    },
    {
        "Menu": "Es teh",
        "qty": 3
    },
]

pesanan_faiz = [
    { 
        "Menu": "Ayam Goreng Krispi",
        "qty":1
    },
    {
        "Menu": "Ayam Puk Puk (Bukan di geprek)",
        "qty":1
    },
    {
        "Menu": "Ayam Bakar",
        "qty":1
    },
    {
        "Menu": "Es teh",
        "qty":1
    },
    {
        "Menu": "Es jeruk",
        "qty":1
    },
]

def hitung_belanja(data):
    total_belanjaan = 0
    # print(data)
    for x in data:
        # print(x["Menu"])
        # print(list_menu[x["Menu"]])
        get_menu = list_menu[x["Menu"]]
        if get_menu["Tipe"] == "Minuman":
            pajak = 0.03
        elif get_menu["Tipe"] == "Makanan":
            pajak = 0.05
            
        harga = get_menu["Harga"]*(1+pajak)
        # print(harga)
        total_belanjaan += harga
    
    total_belanjaan += total_belanjaan*15/100
    return total_belanjaan

print("Rehan Whangsap   : ", hitung_belanja(pesanan_rehan))
print("Amba roni        : ", hitung_belanja(pesanan_roni))
print("Faiz ngawi       : ", hitung_belanja(pesanan_faiz))