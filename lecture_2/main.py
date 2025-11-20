def generate_profile(age: int) -> str:
    """Determine age group depends on age"""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Unknown"


def main():
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")

    # calculate age
    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year

    # list to keep user hobbies
    hobbies = []

    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby.lower() == "stop":
            break
        hobbies.append(hobby)

    life_stage = generate_profile(current_age)

    # create user profile
    user_profile = {
        "name": user_name,
        "birth_year": birth_year,
        "age": current_age,
        "life_stage": life_stage,
        "hobbies": hobbies
    }

    # print profile summary
    print("\n" + "---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['life_stage']}")

    # print hobbies
    if not user_profile['hobbies']:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile['hobbies']:
            print(f"- {hobby}")

    print("---")


if __name__ == "__main__":
    main()
