from stats import count_words , num_appear ,sorted_stats ,sort_on ,report_stats
import sys

path1="/home/kijanaballer/site/bookbot/books/frankenstein.txt"
def get_book_text(book_id):
    with open(book_id) as file:
        return file.read()

    
def main():
    
    try:
        path=sys.argv[1]
        report_stats(count_words(get_book_text(path)), sorted_stats(num_appear(get_book_text(path))))
        sys.exit(0)
    except IndexError  :
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)
 

main()
