from script_parser import read_script, extract_dialogues
from character_gender import identify_gender

from collections import Counter

def get_female_characters(dialogues):
    characters = [speaker for speaker, _ in dialogues]
    counts = Counter(characters)

    # Filter out characters speaking less than 2 times
    frequent_characters = [name for name, count in counts.items() if count >= 2]

    female_characters = []

    for name in frequent_characters:
        gender = identify_gender(name)
        if gender == 'female':
            female_characters.append(name)

    return female_characters


def check_bechdel_test(dialogues, female_characters):
    conversation_found = False

    for i in range(len(dialogues) - 1):
        speaker1, line1 = dialogues[i]
        speaker2, line2 = dialogues[i + 1]

        # Check if both are named female characters and speaking consecutively
        if speaker1 in female_characters and speaker2 in female_characters and speaker1 != speaker2:
            # Check if they’re talking about something other than a man (simple check)
            if not any(word.lower() in line2.lower() for word in ['he', 'him', 'his']):
                conversation_found = True
                print(f"\n🎬 Sample Passing Dialogue:\n{speaker1}: {line1}\n{speaker2}: {line2}")
                break

    return conversation_found

# Example usage
if __name__ == "__main__":
    file_path = r"C:\Users\abhi0\Pythonbechdel_test_project\data\script.txt"
    script_lines = read_script(file_path)
    dialogues = extract_dialogues(script_lines)

    female_characters = get_female_characters(dialogues)
    print(f"🎭 Female Characters Detected: {female_characters}")

    result = check_bechdel_test(dialogues, female_characters)

    if result:
        print("\n✅ This movie PASSES the Bechdel Test.")
    else:
        print("\n❌ This movie FAILS the Bechdel Test.")

