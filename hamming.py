def hata_denetim_bitleri_hesapla(veri_bitleri):
    n = len(veri_bitleri)
    r = 0
    while (2 ** r) < (n + r + 1):
        r += 1

    hamming_kodu = ['0'] * (n + r)
    j = 0
    k = 0
    for i in range(1, len(hamming_kodu) + 1):
        if i == 2 ** j:
            j += 1
        else:
            hamming_kodu[i - 1] = veri_bitleri[k]
            k += 1

    for i in range(r):
        kontrol_pozisyonu = 2 ** i
        for j in range(1, len(hamming_kodu) + 1):
            if j & kontrol_pozisyonu == kontrol_pozisyonu and hamming_kodu[j - 1] == '1':
                hamming_kodu[kontrol_pozisyonu - 1] = str(1 - int(hamming_kodu[kontrol_pozisyonu - 1]))
    
    return ''.join(hamming_kodu)

def hata_tespit_ve_düzelt(hamming_kodu):
    n = len(hamming_kodu)
    r = 0
    while (2 ** r) < n:
        r += 1

    hata_pozisyonu = 0
    for i in range(r):
        kontrol_pozisyonu = 2 ** i
        parite = 0
        for j in range(1, n + 1):
            if j & kontrol_pozisyonu == kontrol_pozisyonu and hamming_kodu[j - 1] == '1':
                parite ^= 1
        hata_pozisyonu += parite * kontrol_pozisyonu

    if hata_pozisyonu != 0:
        duzeltilmis_kod = list(hamming_kodu)
        duzeltilmis_kod[hata_pozisyonu - 1] = str(1 - int(duzeltilmis_kod[hata_pozisyonu - 1]))
        return ''.join(duzeltilmis_kod), hata_pozisyonu
    return hamming_kodu, None

if __name__ == "__main__":
    veri = '1011'  # Örnek veri bitleri
    hamming_kodu = hata_denetim_bitleri_hesapla(veri)
    print(f'Hamming Kodu: {hamming_kodu}')  # Beklenen: 1011011

    duzeltilmis_kod, tespit_edilen_hata_pozisyonu = hata_tespit_ve_düzelt(hamming_kodu)
    print(f'Düzeltilmiş Hamming Kodu: {duzeltilmis_kod}')
    if tespit_edilen_hata_pozisyonu:
        print(f'Hata tespit edildi ve {tespit_edilen_hata_pozisyonu}. pozisyonda düzeltildi.')
    else:
        print('Hata tespit edilmedi.')
