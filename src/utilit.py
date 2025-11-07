from checksum import modulo11_checksum

print("Проверка ISBN-10. Для выхода введите -1")
while True:
    isbn = input("Введите ISBN: ")
    if isbn == "-1":
        break
    if modulo11_checksum(isbn):
        print("correct")
    else:
        print("incorrect")