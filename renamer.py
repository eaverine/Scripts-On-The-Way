import os
import shutil

for filename in os.listdir('C:/Users/User/Downloads'):
    
    if filename.startswith('Page'):
        
        val = filename[:9]
        newname = filename.replace(val,'')
        
        if '.pdf' in newname:
            newname = newname.replace('.pdf','')

        newname = newname + val + '.pdf'
        print(newname)
        
        shutil.move('C:/Users/User/Downloads/{}'.format(filename),'C:/Users/User/Downloads/{}'.format(newname))


