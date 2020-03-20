#Backing-up a folder into a ZIP File
import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '-' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    #Creating the ZIP file.
    print('Creating %s...'%(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files is %s....'%(foldername))
        print('Adding files is %s....'%(subfolders))
        print('Adding files is %s....'%(filenames))
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '-'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done.')
backupToZip('C:\\Users\\master\\Documents\\200 level materials')

            
