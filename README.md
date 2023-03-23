# Some helpful information.

### Link to download the Selenium (in terminal) <br>
we need install this in  folder with our code files

        pip install selenium

----------
### LINK to Download a selenium Driver for CHROME Browsers<br>
(choose your version browser. last number - not a important)

        https://chromedriver.storage.googleapis.com/index.html
-----------

### If have a problem like <br>
"Error: “chromedriver” cannot be opened because the developer cannot be verified." <br>
(I tried this on MacOS - was be ok.)

        Open terminal
            1.Navigate to path where your chromedriver file is located
            2.Execute any one of the below commands
            3.Command1: xattr -d com.apple.quarantine <name-of-executable>
            
            Example
            
            /usr/local/Caskroom/chromedriver 
            $ xattr -d com.apple.quarantine chromedriver 
            (or)
            
            Command2: spctl --add --label 'Approved' <name-of-executable>
            
            Source: https://docwhat.org/upgrading-to-catalina
            
            Note: This will work only with the file(s) where the above command is executed. 
            If a new chromedriver is downloaded then the command has to be executed 
            again on the newly downloaded file

### User Agents Lists <br>
        https://deviceatlas.com/blog/list-of-user-agent-strings
        
### Fake User Agent Lib for Python
        pip install fake-useragent
    
website

        https://pypi.org/project/fake-useragent/
