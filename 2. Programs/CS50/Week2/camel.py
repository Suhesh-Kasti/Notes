def main():
    camel=input("camelCase: ")
    
    for each in camel:
        if each.isupper():
            camel = camel.replace(each, "_"+each)
    print(camel.lower())
    
if __name__=="__main__":
    main()