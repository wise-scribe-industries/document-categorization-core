import logging
from cate_keys import cate_keys
from read_doc_txt import read_doc_txt

# Configure logging>
logging.basicConfig(level=logging.ERROR)


def get_cate_by_key(doc_text):
    # Initialize dictionary with categories from cate_keys and 0 as values
    cate_scores = {cate: 0 for cate in cate_keys}

    # Iterate through each category and its keys
    for cate, keys in cate_keys.items():
        for key in keys:
            # If the key is found in the document text, increment the score for that category
            if key.lower() in doc_text.lower():
                cate_scores[cate] += 1

    # Return the category with the maximum score
    return max(cate_scores, key=cate_scores.get)


if __name__ == "__main__":
    # Example usage
    demo_legal_path = "./demo_files/Legal.docx"
    content = read_doc_txt(demo_legal_path)
    result = get_cate_by_key(content)
    print("This Demo result of get_cate_by_key function for legal documents :")
    print("This is a " + result + " document.")

    demo_will_path = "./demo_files/Demo_Wills.txt"
    content = read_doc_txt(demo_will_path)
    result = get_cate_by_key(content)
    print("This is a " + result + " document.")
