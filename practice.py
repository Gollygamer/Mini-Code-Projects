#functions
import time


print("let's play a game of mad libs")



word_types = ["adjective", "adjective", "type of bird", "room in a house", "verb (past tense)", "verb", "relative's name", "noun", "a liquid", "verb (ending in -ing)",
              "part of the body (plural)", "plural noun", "verb (ending in -ing)","noun"]

for word in word_types:
    print("give me a " + word)
    answer = input()
    index = word_types.index(word)
    word_types[index] = answer
    
print("OKAY! give me a second whilst I load your response")
time.sleep(3)

print(f"""
It was a {word_types[0]}, cold November day. I woke up to the {word_types[1]} smell of {word_types[2]} roasting in the {word_types[3]} downstairs. I {word_types[4]} the stairs to see if i could help {word_types[5]} the dinner. 
My mom said \"See if {word_types[6]} needs a fresh {word_types[7]}.\" So i carried a tray of glasses full of {word_types[8]} into the {word_types[9]} room. When I got there, I couldn't believe my {word_types[10]}! There were {word_types[11]} 
{word_types[12]} on the {word_types[13]}!
""")
    
   

