def main():
        string=input("Give an emoticon: ")
        convert(string)
        
        
def convert(comein):
    comein=comein.replace(":)", "\U0001F642")
    comein=comein.replace(":(", "\U0001F641")
    print(comein)
    
if __name__=="__main__":
    main()

