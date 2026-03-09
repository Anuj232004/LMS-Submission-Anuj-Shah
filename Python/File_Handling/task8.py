with open ("paragraph.txt","w") as file:
    file.write("Beneath a sky streaked with neon whispers, a lone cat tiptoed across the cobblestones, carrying secrets in its shadow. Somewhere in the distance, a tuba groaned like a tired giant, and a lamppost flickered, debating whether to illuminate truth or illusion. Meanwhile, a forgotten book hummed quietly on a windowsill, dreaming of readers who might never arrive.")

with open("paragraph.txt", "r") as file:
    content = file.read().lower()
 
words = content.split()
 
print("Total number of words:", len(words))
 
search_word = input("Enter a word to search: ").lower()
 
print("Occurrences:", words.count(search_word))


    