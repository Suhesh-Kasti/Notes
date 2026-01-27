def main():
    time=str(input("What time is it? "))
    answer=convert(time)
    if 8 >  answer >= 7:
        print("breakfast")
    elif 13 > answer >= 12:
        print("lunch")
    elif 19 > answer >= 18:
        print("dinner")

def convert(time):
    hour=float(time.split(":")[0])
    minute=float(time.split(":")[-1])
    final = hour+(minute/60)
    return final

if __name__ == "__main__":
    main()