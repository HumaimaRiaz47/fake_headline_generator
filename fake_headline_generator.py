#import random module
import random

subjects = [
    "Angry grandma",
    "Confused cat",
    "Sleep-deprived student",
    "Overworked AI",
    "Local chicken",
    "Flat Earth society",
    "Time-traveling tourist",
    "Professional napper",
    "Talking fridge",
    "Emoji influencer",
    "Unemployed superhero",
    "Dancing politician",
    "Alien from Mars",
    "Ghost of Shakespeare",
    "Karate-trained toddler",
    "Billionaire hamster",
    "Zombie barista",
    "Drama queen goat",
    "Flat tire conspiracy theorist",
    "Accidental magician"
]

actions = [
    "declares war on",
    "accidentally invents",
    "gets arrested for eating",
    "organizes protest against",
    "confuses scientists with",
    "launches TikTok challenge about",
    "claims ownership of",
    "mistakenly marries",
    "starts a cult based on",
    "steals secret recipe for",
    "warns people about",
    "breaks world record for juggling",
    "accidentally teleports into",
    "refuses to pay tax on",
    "writes love letter to",
    "turns into",
    "buys 500 tons of",
    "gets lost inside",
    "runs for president of",
    "replaces currency with"
]

places_objects = [
    "giant rubber duck",
    "haunted WiFi router",
    "quantum banana",
    "government cafeteria",
    "moonwalk dance floor",
    "interdimensional sandwich",
    "public toilet time machine",
    "talking pineapple",
    "haunted Zoom call",
    "mysterious sock dimension",
    "giant pizza slice",
    "parallel universe Starbucks",
    "haunted washing machine",
    "karaoke volcano",
    "spaghetti-powered rocket",
    "flying scooter",
    "underground donut society",
    "haunted TikTok filter",
    "cheese-flavored vaccine",
    "exploding alarm clock"
]

#headline generation

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_object = random.choice(places_objects)

    headline = f'BREAKING NEWS: {subject} {action} {place_object} '
    print('\n' + headline)

    user_input = input('\nDo you want another headline? yes/no').strip().lower()
    if user_input == 'no':
        break

print('\nThanks for using FAKE HEADLINE GENERATOR!!')
