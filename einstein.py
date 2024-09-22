def main():
    mass= int(input("Enter the mass: "))
    print(energy(mass))
def energy(mass):
    c=300000000
    E=mass*c*c
    return E
   
main()
