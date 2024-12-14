import random

def labirent_oyunu():
    print("=== Labirent Oyunu ===")
    print("Amacınız 15. bölüme ulaşmak! Her bölümde farklı bir seçim yapmanız gerekiyor.")

    bolumler = {
        1: "Başlangıç noktası. İleri gitmek için 'ileri' yazın.",
        2: "Bir yol ayrımındasınız. Sağ veya sol seçebilirsiniz.",
        3: "Bir köprü var. Geçmek için 'geç' yazın.",
        4: "Bir mağara buldunuz. İçeri girmek için 'gir' yazın.",
        5: "Bir nehir var. Yüzmek için 'yüz' yazın.",
        6: "Ormanda ilerliyorsunuz. İleri gitmek için 'ileri' yazın.",
        7: "Bir dağa geldiniz. Tırmanmak için 'tırman' yazın.",
        8: "Bir kapı buldunuz. Açmak için 'aç' yazın.",
        9: "Bir bilmeceli kapı var. 'cevap' yazarak ilerleyebilirsiniz.",
        10: "Bir yaratık karşınıza çıktı. Kaçmak için 'kaç' yazın.",
        11: "Bir köy buldunuz. Devam etmek için 'devam' yazın.",
        12: "Bir bataklık var. Geçmek için 'atla' yazın.",
        13: "Bir kule var. Tırmanmak için 'tırman' yazın.",
        14: "Son kapıya ulaştınız. Açmak için 'aç' yazın.",
        15: "Tebrikler! Labirenti başarıyla tamamladınız!"
    }

    mevcut_bolum = 1

    while mevcut_bolum <= 15:
        print(f"\nBölüm {mevcut_bolum}: {bolumler[mevcut_bolum]}")
        if mevcut_bolum == 15:
            break

        secim = input("Ne yapmak istersiniz? ").lower()

        dogru_cevaplar = {
            1: "ileri", 2: ["sağ", "sol"], 3: "geç", 4: "gir",
            5: "yüz", 6: "ileri", 7: "tırman", 8: "aç",
            9: "cevap", 10: "kaç", 11: "devam", 12: "atla",
            13: "tırman", 14: "aç"
        }

        if isinstance(dogru_cevaplar[mevcut_bolum], list):
            if secim in dogru_cevaplar[mevcut_bolum]:
                mevcut_bolum += 1
            else:
                print("Yanlış seçim! Bölüme yeniden başlayın.")
        else:
            if secim == dogru_cevaplar[mevcut_bolum]:
                mevcut_bolum += 1
            else:
                print("Yanlış seçim! Bölüme yeniden başlayın.")

    print("Oyunu bitirdiniz! Harika bir iş çıkardınız.")

if __name__ == "__main__":
    labirent_oyunu()
