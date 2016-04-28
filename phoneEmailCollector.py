#! python3

import re, pyperclip

#create a regex for phone numbers
phoneRegEx = re.compile(r'''
(
((\d\d\d)    |    (\(\d\d\d\)))? #area code
(\s|-)          #first seperator
\d\d\d          #first 3 numbers
-               #second seperator
\d\d\d\d        #last 4 numbers
(((ext(\.)?\s)|x)     #extension word
(\d{2,5}))?    #extension number
)
''', re.VERBOSE)


#TODO: create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+      #username
@           #domain symbol
[a-zA-Z0-9_.+]+      #$hostname
''', re.VERBOSE)

#TODO: get the text off the clipboard
text = pyperclip.paste()

#TODO: extract email phone from the text

extractedPhone = phoneRegEx.findall(text)
extractedEmail = emailRegex.findall(text)
#
# print(extractedEmail)
# print(extractedPhone)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


#TODO: copy extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers)  + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print(results)