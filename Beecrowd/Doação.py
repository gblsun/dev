def main():
    total_vic_coins = 0.0
    conversion_rate = 2.50

    while True:
        donation = float(input())
        if donation == -1.0:
            break
        total_vic_coins += donation

    total_reais = total_vic_coins * conversion_rate

    print(f"{total_vic_coins:.2f}")
    print(f"{total_reais:.2f}")
    
    if __name__ == "__main__":
    main()

