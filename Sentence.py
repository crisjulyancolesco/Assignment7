print("Wanna know how many words, vowels, and consonants are in your sentence?")
print("Let me count it for you!")

Sentence = input("Enter your sentence: ")
Word = 1
for I in range(len(Sentence)):
    if(Sentence[I] == ' ' ):
        Word = Word + 1

Vowels = 0
Consonants = 0
for I in range(len(Sentence)):
    if(Sentence[I] == 'a' or Sentence[I] == 'e' or Sentence[I] == 'i' or Sentence[I] == 'o' or Sentence[I] == 'u' or Sentence[I] == 'A' or Sentence[I] == 'E' or Sentence[I] == 'I' or Sentence[I] == 'O' or Sentence[I] == 'U'):
        Vowels = Vowels + 1
    else:
        Consonants = Consonants + 1
        if(Sentence[I] == '.' or Sentence[I] == ',' or Sentence[I] == ' ' or Sentence[I] == '?' or Sentence[I] == '!' or Sentence[I] == "'" or Sentence[I] == '-' or Sentence[I] == '"' or Sentence[I] == ';' or Sentence[I] == ':'):
            Consonants = Consonants - 1
        else:
            if(Sentence[I] >= '0' and Sentence[I] <= '9'):
                Consonants = Consonants - 1

print("Your sentence contains:")
print(f"Words: {Word}")
print(f"Vowels: {Vowels}")
print(f"Consonants: {Consonants}")