from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Dogcky")
    
    # Initial status
    print("Initial status:")
    my_pet.get_status()
    
    # Test eating
    print("\nAfter eating:")
    my_pet.eat()
    my_pet.get_status()
    
    # Test playing
    print("\nAfter playing:")
    my_pet.play()
    my_pet.get_status()
    
    # Test sleeping
    print("\nAfter sleeping:")
    my_pet.sleep()
    my_pet.get_status()
    
    # Test training tricks
    print("\nTraining tricks:")
    my_pet.train("Sit")
    my_pet.train("Roll over")
    my_pet.train("Play dead")
    my_pet.show_tricks()
    
    # Final status
    print("\nFinal status:")
    my_pet.get_status()

if __name__ == "__main__":
    main()