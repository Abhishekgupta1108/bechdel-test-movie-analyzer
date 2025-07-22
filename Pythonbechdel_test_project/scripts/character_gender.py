import gender_guesser.detector as gender


def identify_gender(name):
    d = gender.Detector(case_sensitive=False)
    first_name = name.split()[0]  # Use first name for gender detection
    result = d.get_gender(first_name)

    if result in ['female', 'mostly_female']:
        return 'female'
    elif result in ['male', 'mostly_male']:
        return 'male'
    else:
        return 'unknown'


# Example usage:
if __name__ == "__main__":
    print(identify_gender("SARAH CONNOR"))
    print(identify_gender("JOHN DOE"))
