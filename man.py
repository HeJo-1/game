import random

def adam_asmaca():
    print("=== Adam Asmaca Oyunu ===")
    print("Kelimeyi tahmin etmeye çalışın! Harfleri tek tek deneyebilirsiniz.")

    kelimeler = [
        "bilgisayar", "kitap", "kalem", "defter", "araba",
        "telefon", "televizyon", "uçak", "tren", "okul"
    ]

    secilen_kelime = random.choice(kelimeler)
    gorunen_kelime = ["_" for _ in secilen_kelime]
    tahmin_hakki = 7
    kullanilan_harfler = []

    while tahmin_hakki > 0:
        print("\nKalan Tahmin Hakkı:", tahmin_hakki)
        print("Kelime:", " ".join(gorunen_kelime))
        print("Kullanılan Harfler:", ", ".join(kullanilan_harfler))

        tahmin = input("Bir harf tahmin edin: ").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen sadece bir harf girin!")
            continue

        if tahmin in kullanilan_harfler:
            print("Bu harfi zaten kullandınız!")
            continue

        kullanilan_harfler.append(tahmin)

        if tahmin in secilen_kelime:
            print(f"Doğru! '{tahmin}' harfi kelimede var.")
            for i, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    gorunen_kelime[i] = tahmin

            if "_" not in gorunen_kelime:
                print("\nTebrikler! Kelimeyi doğru tahmin ettiniz:", secilen_kelime)
                break
        else:
            print(f"Yanlış! '{tahmin}' harfi kelimede yok.")
            tahmin_hakki -= 1

    if tahmin_hakki == 0:
        print(f"\nÜzgünüm, kaybettiniz. Doğru kelime: {secilen_kelime}")

if __name__ == "__main__":
    adam_asmaca()
