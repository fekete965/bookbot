def get_word_count(text):
  words = text.split()
  
  return len(words)

def get_character_count(text):
  char_count_dict = {}
  
  for char in text:
    lower_char = char.lower()
    
    if lower_char.isspace():
      continue
    elif lower_char in char_count_dict:
      char_count_dict[lower_char] += 1
    else:
      char_count_dict[lower_char] = 1
      
  char_count_dict
      
  return char_count_dict

def sort_character_dict(char_dict):
  char_data = []
  
  for key in char_dict:
    data = {
      "char": key,
      "num": char_dict[key],
    }
    
    char_data.append(data)
    
  def sort_on(item):
    return item["num"]

  char_data.sort(reverse=True, key=sort_on)
  
  return char_data
