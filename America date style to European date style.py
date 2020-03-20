#Renaming files with American-Style Date to European-Style dates
import shutil, os, re
datePattern = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-                 # one or two digits for the day
((19|20)\d\d)                   # four digits for the year
(.*?)$                          # all text after the date 
""", re.VERBOSE)

#Loop over the file in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    #Form the european-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPath
    
    #Getting the full absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #Renaming the files.
    print('Renaming "%s" to "%s"...' %(amerFilename,euroFilename))
    shutil.move(amerFilename, euroFilename)
    
