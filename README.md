#osxrsyncbackup
Gordon Inggs
September 2014
Scripting for backing up certain key file types to another local directory location. Intended to be used with a redudant local drive, or a cloud storage service such as Dropbox or Google Drive.

##configuration
Both files need to be specialised to the system being used

##setup
* backup.py:
    * needs to have executable permissions set (`chmod +x backup.py`)

* com.gordongordon.osx.backup.plist:
    1.  Needs to be copied to ~/Library/LaunchAgents (`cp com.gordongordon.osx.backup.plist ~/Library/LaunchAgents`)
    2.  Needs to be loaded into launchd (`launchctl load ~/Library/LaunchAgents/com.gordongordon.osx.backup.plist`)
    3.  Needs to be started (`launchctl start com.gordongordon.osx.backup`)
    
##ToDo
* a better configuration system