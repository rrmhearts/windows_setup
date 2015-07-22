from __future__ import with_statement
import string, shutil
#https://vimeo.com/channels/bloomlibrary/117927599

with open("C:\\Users\\rogersk\\Documents\\newKey.sikuli\\BloomSCNumbers.txt","r") as file:
    for line in iter(file):   
        letter = line[0] 
        l_options = int(line[2:-1])
    
        app_prefix = ""
        os_prefix = ""
        ap = app_prefix
        op = os_prefix
        oap = op+ap
    
        click(oap+"title_bar.png")
        
        import java.awt.Robot as jR
        
        r = jR() # makes a new robot
        #wait(2)
        key = ord(letter)   
        capital = key <97 
        if not capital:
            key = key-32
        
        #for loop in range(1):
        #for letter in string.ascii_uppercase:
        
        for options in range(1,l_options+1):
            if capital:
                r.keyPress(16)
            wait(.25)
            r.keyPress(key)
            r.keyPress(key)
            wait(.5)
            for moves in range(options): 
                type(Key.RIGHT)     
                wait(.25)
            r.keyRelease(key)
            wait(.25)
            if capital:
                r.keyRelease(16)
            wait(.25)

        #screenshot words
        image = capture(Region(269,156,445,62))
        shutil.copy(image, letter+".png")

        #delete word
        for options in range(1,l_options+1):
           type(Key.BACKSPACE)
        wait(1)
        #type special words
        
        #for each word
         #type words
         #check word
         #iferror
          #capture actual word   
         #else success
         #delete word