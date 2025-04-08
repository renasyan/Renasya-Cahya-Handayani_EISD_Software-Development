def cek_duplikat(data):
    for x in data:
        loop_data = data
        loop_data.remove(x)
        for y in data:
            if x == y:
                return True
                # print("duplicate numbers here!!!", x, y)
            # else:
            #     print("bro friendless")
    return False

data = [100, 1, 3, 2, 4, 6, 8, 5, 7, 99, 11, 13, 15, 10,  12, 14, 16, 18, 20, 17, 19]
print(cek_duplikat(data))