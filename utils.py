from difflib import SequenceMatcher


def clean_text(text):
    return text.strip().lower()


def is_similar(new_text, existing_data, threshold=0.8):
    for data in existing_data:
        ratio = SequenceMatcher(None, new_text, data[1]).ratio()
        if ratio > threshold:
            return True
    return False