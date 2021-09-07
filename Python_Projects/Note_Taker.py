from datetime import date
import os
question = input("Option A: create a new file or option B: continue with another file [a/b]").lower()
if question == 'a':
    date = str(date.today())
    file_name = input("what would you like the file name of this note to be?:") + ".txt"
    subject = input("welcome to your new note, what is the subject of this note?:")
    body = input("write your note here:")
    with open(file_name, 'w') as f:
        f.write(f"date: ")
        f.write(date)
        f.write(os.linesep)
        f.write("subject: ")
        f.write(subject)
        f.write(os.linesep)
        f.write(body)
        f.write(os.linesep)
        f.write('----------------------------------------------------------------------------------------------------------------------------')
        f.write(os.linesep)

elif question == 'b':
    file_name = input("what is the previous file name for the note? (please do not provide file type):") + ".txt"
    date = str(date.today())
    subject = input("welcome to your note entry. what is the subject of this note?:")
    body = input("write your note here:")
    with open(file_name, 'a') as f:
        f.write(f"date: ")
        f.write(date)
        f.write(os.linesep)
        f.write("Subject: ")
        f.write(subject)
        f.write(os.linesep)
        f.write(body)
        f.write(os.linesep)
        f.write('----------------------------------------------------------------------------------------------------------------------------')
        f.write(os.linesep)









