#Import from TextBlob
from textblob import TextBlob

#Ask user to input
text=input('Please enter your text here:')

#Display character count for inputted text
print("Character count is:", len(text))

#Ask user to input (choose Arabic or Spanish)
language=input('Spanish or Arabic?:')
Spanish='Spanish'
Arabic='Arabic'
textblob=TextBlob(text)

#Display translation and the new count with if statements
if language==Spanish:
    textblob=TextBlob(text)
    textblob.translate(to='es')
    print("Translation:", textblob.translate(to='es'))
    print("Character COUNT for new text:", len(textblob.translate(to='es')))
elif language==Arabic:
    textblob=TextBlob(text)
    textblob.translate(to='ar')
    print("Translation:", textblob.translate(to='ar'))
    print("Character COUNT for new text:", len(textblob.translate(to='ar')))
else:
    textblob=TextBlob(text)
    print("Please input Spanish or Arabic.")

#Display Sentimental level
print(TextBlob(text).sentiment)




