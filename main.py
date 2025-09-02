from stats import get_character_count, get_word_count, sort_character_dict
import sys

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  print("============ BOOKBOT ============")  
  file_path = sys.argv[1]
  
  print(f"Analyzing book found at {file_path}...")
  file_content = get_book_text(file_path)
  
  print("----------- Word Count ----------")
  num_words = get_word_count(file_content)
  print(f"Found {num_words} total words")
  
  print("--------- Character Count -------")
  char_count_dict = get_character_count(file_content)
  char_count_list = sort_character_dict(char_count_dict)
  
  for data in char_count_list:
    char = data['char']
    num = data['num']

    print(f"{char}: {num}")
    
  print("============= END ===============")

main()
