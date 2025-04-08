uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]


def hitung_kembalian(uang, total):
    total_kembalian = uang-total
    
    kembalian = {}
    # 2000 : 1
    
    # print(total_kembalian)
        # print(total_kembalian)
    for x in uang_pecahan:  
        # 500%500
        # 0
        cek_kembalian = total_kembalian % x
        if cek_kembalian != total_kembalian:
            # print(cek_kembalian)
            # cek_kembalian = total_kembalian % x
            if cek_kembalian == 0:
                # print(x, 1)
                
                kembalian[x] = total_kembalian//x
                return kembalian
            else:
                # print(x, x//cek_kembalian)
                # 2500 : 2000 = 1
                kembalian[x] = total_kembalian//x
                # print(total_kembalian)
                total_kembalian=cek_kembalian

print(hitung_kembalian(10000, 7500 ))
print(hitung_kembalian(5000, 1100 ))
print(hitung_kembalian(178000, 90500))