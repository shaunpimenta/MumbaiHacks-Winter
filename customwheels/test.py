import re

def find_part_match(input_text, part_names):
    """
    Find the first match for part names in the input text.

    Parameters:
    - input_text (str): The input text to search.
    - part_names (list): List of part names to search for.

    Returns:
    - str or None: The first matched part name or None if no match is found.
    """
    # Create a regular expression pattern using part names
    pattern = r'\b(?:' + '|'.join(part_names) + r')\b'

    # Search for the first match
    match = re.search(pattern, input_text, flags=re.IGNORECASE)

    # Return the matched part name or None
    return match.group(0) if match else None

# Example usage:
input_text = "I have a tire and a spoiler on my car."
# part_names = ["tire", "spoiler", "bonnet"]

# result = find_part_match(input_text, part_names)
# print(result)
if "tire" in input_text:
    print("yes")
else:
    print("no")



                    else if (mesh.material && mesh.material.name === '{{responseReply.wheel_details.mat_name}}') {
