import random

def guess_number():
    # Rastgele bir sayı seçme
    number = random.randint(1, 100)
    attempts = 0

    print("1 ile 100 arasında bir sayıyı tahmin et!")

    while True:
        guess = input("Tahmininizi girin: ")

        # Girilen değeri kontrol etme
        try:
            guess = int(guess)
        except ValueError:
            print("Lütfen bir sayı girin.")
            continue

        # Tahmin kontrolü
        if guess < number:
            print("Daha büyük bir sayı girin.")
        elif guess > number:
            print("Daha küçük bir sayı girin.")
        else:
            print(f"Tebrikler! {number} sayısını buldunuz!")
            break

        attempts += 1

    print(f"{attempts} denemede buldunuz.")

if __name__ == "__main__":
    guess_number()