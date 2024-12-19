# Criminal Profiling Tool

# Sample profiles database
profiles = {
    "robbery": {
        "age": "18-25",
        "gender": "male",
        "location": "urban",
        "common_traits": ["impulsive", "risk-seeking"]
    },
    "burglary": {
        "age": "25-40",
        "gender": "male",
        "location": "suburban",
        "common_traits": ["planning", "cautious"]
    },
    "assault": {
        "age": "18-35",
        "gender": "male",
        "location": "urban",
        "common_traits": ["aggressive", "sudden"]
    },
    "fraud": {
        "age": "30-50",
        "gender": "male/female",
        "location": "online",
        "common_traits": ["deceptive", "intelligent"]
    }
}


def get_crime_profile(crime_type):
    return profiles.get(crime_type.lower(), None)


def main():
    print("Welcome to the Criminal Profiling Tool!")
    print("Available crime types: robbery, burglary, assault, fraud")

    crime_type = input("Enter the type of crime: ")
    profile = get_crime_profile(crime_type)

    if profile:
        print(f"\nProfile for {crime_type.capitalize()}:")
        print(f"Age Range: {profile['age']}")
        print(f"Gender: {profile['gender']}")
        print(f"Common Location: {profile['location']}")
        print(f"Common Traits: {', '.join(profile['common_traits'])}")
    else:
        print("Sorry, no profile found for that crime type.")


if __name__ == "__main__":
    main()

