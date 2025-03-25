#validasi pasword
special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~)"
def is_valid_password (password):
    if len (password) < 8 :
        print("Password terlalu pendek! Minimal 8 karakter!!")
        return False
    if not any(c.islower() for c in password ):
        print("Password setidaknya terdiri atas 1 huruf kecil!!")
        return False
    if not any(c.isupper() for c in password ):
        print("Password setidaknya terdiri atas 1 huruf kapital!!")
        return False
    if not any(c.isdigit() for c in password ):
        print("Password setidaknya terdiri atas 1 angka!!")
        return False
    if not any(c in special_chars for c in password ) : 
        print("Password setidaknya terdiri atas 1 karakter khusus (!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~))")
        return False
    return True

while True:
    password = input("Masukkan password (terdiri dari huruf kapital, huruf kecil, angka, dan karakter khusus): ")
    if is_valid_password(password):
        print("Password yang anda masukkan sudah valid!")
        break
    else :
        print("Password yang anda masukkan tidak valid!, coba lagi")
    print()

    