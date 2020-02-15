# find phone numbers and email address on the clipboard
# create phone regex

import pyperclip,re
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                # area code
(\s|-|\.)?                        # separator
(\d{3})                           # first 3 digits
(\s|-|\.)                         # separator
(\d{4})                           # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

# create email regex
import pyperclip,re
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+     # username
@                     # @ symbol
[a-zA-Z0-9.-]+        # domain name
(\.[a-zA-Z]{2,4})     # dot-something
)''',re.VERBOSE)

# find all the matches in the clipboard
import pyperclip,re
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# join the matches into string for the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
































                        
