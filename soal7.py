def deskripsi(kalimat):
    kalimat_deskripsi = ""
    for x in kalimat:
        if not x.isalpha():
            # print(x)
            kalimat_deskripsi += x
        else:
            x = ord(x)
            # print(chr(x-5))
            kalimat_deskripsi += chr(x-5)
            
    return print(kalimat_deskripsi)

kata = [
# "f",
"xfqfr bfmdz",
"gjxtp lzj rfz ifkyfw jxi snm",
"gwt, gjxtp qz rfz rfpfs in bfwlty lfp?",
"fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz",
"dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"
]

for x in kata:
    deskripsi(x)