import nltk
from nltk.corpus import stopwords
import string
import re
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def filter_text(text):
    # Lowercasing
    text = text.lower()
    # Removing punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Removing stop words
    words = [word for word in text.split() if word not in stop_words]
    # Removing special characters
    filtered_text = [re.sub(r'\W+', '', word) for word in words]
    return ' '.join(filtered_text)
file_path = input("Enter file path: ")
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()
    filtered_result = filter_text(file_content)
print("Filtered Text:", filtered_result)

# OUTPUT EXAMPLE
# Enter file path: Textfile.txt
# Filtered Text: hello world another sample text numbers 123 symbols
