#!/usr/bin/env python3


class MyString:
    
    def __init__(self, value=None):
        if value is not None and not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    value = property(get_value, set_value)

    def is_sentence(self):
        if self._value and self._value.endswith("."):
            return True
        return False

    def is_question(self):
        if self._value and self._value.endswith("?"):
            return True
        return False

    def is_exclamation(self):
        if self._value and self._value.endswith("!"):
            return True
        return False

    def count_sentences(self):
        if not self._value:
            return 0
        
        sentence_endings = (".", "?", "!")
        sentence_count = 0

        
        inside_word = False
        ending_character_encountered = False

        for char in self._value:
            if char.isalpha() or char.isdigit() or char in ("'", "-"):
                inside_word = True
                ending_character_encountered = False
            elif char in sentence_endings and inside_word:
                sentence_count += 1
                ending_character_encountered = True
                inside_word = False
            elif char in sentence_endings and not ending_character_encountered:
                sentence_count += 1
                ending_character_encountered = True
        
        return sentence_count








    


        
    





    
  # def __init__(self):
  #   self._value = None

  # def get_value(self):
  #   return self._value
    
  # def set_value(self, value):
  #   if (type(value) != str):
  #     print("The value must be a string.")
  #   else:
  #     self._value = value


  # value = property(get_value, set_value)






    # def __init__(self, value=None):
    #     self.value = value

    # def is_sentence(self):
    #     return self.value.endswith(".") if self.value else False

    # def is_question(self):
    #     return self.value.endswith("?") if self.value else False

    # def is_exclamation(self):
    #     return self.value.endswith("!") if self.value else False

        
    













  


# class MyString:
    
#     def __init__(self, value=None):
#         if value is not None and not isinstance(value, str):
#             print("The value must be a string.")
#         else:
#             self._value = value

#     def get_value(self):
#         return self._value
    
#     def set_value(self, value):
#         if not isinstance(value, str):
#             print("The value must be a string.")
#         else:
#             self._value = value

#     value = property(get_value, set_value)

#     def is_sentence(self):
#         if self._value and self._value.endswith("."):
#             return True
#         return False

#     def is_question(self):
#         if self._value and self._value.endswith("?"):
#             return True
#         return False

#     def is_exclamation(self):
#         if self._value and self._value.endswith("!"):
#             return True
#         return False

#     def count_sentences(self):
#         if not self._value:
#             return 0
        
#         sentences = self._value.split(".")
#         sentences = [s for s in sentences if s.strip()]
#         return len(sentences)

