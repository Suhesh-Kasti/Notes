def main():
    answer=str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))

    if answer.lower()=="42" or answer.lower()=="forty-two" or answer.lower()=="forty two": 
        print("Yes")
    else:
        print("No")
    
if __name__=="__main__":
    main()