# Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες. Αρχικά απεικονίστε κάθε χαρακτήρα σε δυαδικό 
# μήκους 7. Υπολογίστε ποια είναι η μεγαλύτερη ακολουθία από συνεχόμενα 0 και από συνεχόμενα 1.

from os import chdir
chdir('.')

with open('tale.txt', 'r') as f:
    text = f.read()

chars = list(text)
binary = ''
for char in chars:
    binary += bin(ord(char))[2:]

maxZeroCount = len(max(binary.split('1')))
maxOneCount = len(max(binary.split('0')))
print(maxZeroCount)
print(maxOneCount)
    