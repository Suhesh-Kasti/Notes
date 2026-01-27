def main():
    mass=float(input("Please input the mass: "))
    c2=pow(300000000,2)
    print(c2) 
    energy=mass*c2
    print(f"The energy is: {int(energy)}")
    
if __name__=="__main__":
    main()