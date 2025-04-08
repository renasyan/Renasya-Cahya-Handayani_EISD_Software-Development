uang_pecahan = [100000, 50000, 20000,  10000, 5000, 2000, 1000, 500, 200, 100]


def hitung_kembalian(uang, total):
    total_kembalian = uang-total
    kembalian ={
        
    }
    while total_kembalian != 0:
        # print(total_kembalian)
        while total_kembalian !=0:
            for x in uang_pecahan:  
                cek_kembalian = total_kembalian % x
                if cek_kembalian != total_kembalian:
                    total_kembalian = total_kembalian % x
                    if cek_kembalian == 0:
                        # print(x, 1)
                        kembalian[x] = 1
                    else:
                        # print(x, x//cek_kembalian)
                        kembalian[x] = x//cek_kembalian
                        
    return kembalian

print(hitung_kembalian(10000, 7500 ))
print(hitung_kembalian(5000, 1100 ))
print(hitung_kembalian(178000, 90500))