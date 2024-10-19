# Chinese Astrology Program: Determine the Chinese zodiac animal based on birth year

# Function to determine the Chinese zodiac animal based on birth year
def determine_chinese_zodiac(year):
    # List of Chinese zodiac animals and their associated years in a repeating 12-year cycle
    zodiac_animals = [
        ("Rat", "People born in the Year of the Rat are clever, quick-witted, and resourceful. They are ambitious and adaptable in nature.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/rat.htm"),
        ("Ox", "Oxen are known for their diligence, dependability, and strength. They value hard work and are reliable and calm.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/ox.htm"),
        ("Tiger", "People born in the Year of the Tiger are brave, competitive, and confident. They are natural leaders who are unafraid of challenges.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/tiger.htm"),
        ("Rabbit", "Rabbits are gentle, quiet, and elegant. They are compassionate and thoughtful, preferring peaceful lives.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/rabbit.htm"),
        ("Dragon", "Dragons are energetic, fearless, and ambitious. They are natural-born leaders with confidence and charisma.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/dragon.htm"),
        ("Snake", "Snakes are intelligent, wise, and graceful. They are intuitive and often make careful, well-thought-out decisions.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/snake.htm"),
        ("Horse", "People born in the Year of the Horse are active, energetic, and free-spirited. They enjoy being social and exploring new opportunities.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/horse.htm"),
        ("Goat", "Goats are calm, gentle, and empathetic. They prefer a peaceful life surrounded by nature and beauty.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/sheep.htm"),
        ("Monkey", "Monkeys are witty, intelligent, and playful. They are highly adaptable and quick learners, often bringing humor to any situation.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/monkey.htm"),
        ("Rooster", "Roosters are observant, hardworking, and courageous. They are detail-oriented and thrive in leadership roles.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/rooster.htm"),
        ("Dog", "People born in the Year of the Dog are loyal, honest, and protective. They value justice and have a strong sense of duty.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/dog.htm"),
        ("Pig", "Pigs are kind-hearted, generous, and sincere. They enjoy helping others and value harmony and enjoyment in life.", "https://www.chinahighlights.com/travelguide/chinese-zodiac/pig.htm")
    ]
    
    # The Chinese zodiac repeats every 12 years, so we use modulo arithmetic to find the user's zodiac animal
    zodiac_index = (year - 1900) % 12
    animal, summary, link = zodiac_animals[zodiac_index]
    
    return animal, summary, link

# Main function to run the program
def main():
    # Prompt the user for their birth year
    print("Welcome to the Chinese Astrology Program!")
    try:
        year = int(input("Enter your birth year (e.g., 1995): "))
        
        # Call the function to determine the zodiac animal, summary, and link
        zodiac_animal, summary, link = determine_chinese_zodiac(year)
        
        # Output the user's Chinese zodiac animal, summary, and link
        print(f"Your Chinese Zodiac animal is: {zodiac_animal}")
        print(f"Summary: {summary}")
        print(f"Learn more about your sign here: {link}")
    
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Please enter a valid numerical year.")

# Run the program
if __name__ == "__main__":
    main()