import os

def read_script(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        return f.readlines()

def extract_dialogues(script_lines):
    dialogues = []
    current_speaker = None

    for line in script_lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Skip scene headings or non-character lines
        if any(keyword in line for keyword in ['INT.', 'EXT.', 'DAY', 'NIGHT']):
            continue
        if any(char.isdigit() for char in line):  # Skip lines containing numbers (scene numbers, dates)
            continue
        if len(line) > 30:  # Likely not a character name if line is too long
            continue

        # Detect character name (usually uppercase and short)
        if line.isupper() and 1 <= len(line.split()) <= 4:
            current_speaker = line
        elif current_speaker and line:
            dialogues.append((current_speaker, line))

    return dialogues


# Example usage
if __name__ == "__main__":
    file_path = r"C:\Users\abhi0\Pythonbechdel_test_project\data\script.txt"   # Replace with your script file name
    script_lines = read_script(file_path)
    dialogues = extract_dialogues(script_lines)

    print(f"Total dialogues detected: {len(dialogues)}")
    print(dialogues[:10])  # Show first 10 dialogues as sample
