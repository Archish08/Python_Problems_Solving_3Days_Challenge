input_story = input("Enter the story:\n")
words=input_story.split()
articles=['a','an','the']
result = [word
          for word in words
          if word.lower() not in articles]
print(' '.join(result))