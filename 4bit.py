from hamming import calculate_parity_bits, detect_and_correct_error
import random

data = '1011'
hamming_code = calculate_parity_bits(data)
print(f'4 Bit - Hamming Kodu: {hamming_code}')

# Hata testi için hata oluşturma
error_pos = random.randint(0, len(hamming_code) - 1)
error_hamming_code = list(hamming_code)
error_hamming_code[error_pos] = '1' if error_hamming_code[error_pos] == '0' else '0'
error_hamming_code = ''.join(error_hamming_code)
print(f'4 Bit - Hata İçeren Hamming Kodu: {error_hamming_code} (Hata Pozisyonu: {error_pos + 1})')

corrected_code, detected_error_pos = detect_and_correct_error(error_hamming_code)
print(f'4 Bit - Düzeltilmiş Hamming Kodu: {corrected_code}')
if detected_error_pos:
    print(f'Hata tespit edildi ve {detected_error_pos}. pozisyonda düzeltildi.')
else:
    print('Hata tespit edilmedi.')
