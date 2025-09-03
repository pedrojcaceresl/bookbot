from stats import get_num_words, frequency_counter, sort_dict, print_report
import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    
    args = sys.argv
    
    if (len(args) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_content = get_book_text(args[1])
    total_words = get_num_words(book_content)
    letters = frequency_counter(book_content)
    ordered_list = sort_dict(letters)
    
    print_report(total_words, ordered_list)
    
main()