def translate(phrase):
     translation = ""
     for letter in phrase:
         if letter in "AEIOUaeiou":
             translation = translation + "wow"
         else:
             translation = translation + letter

     return translation

print(translate(input("Enter a string:")))

