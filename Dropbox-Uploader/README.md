# Dropbox Uploader

Dropbox Uploader is a **BASH** script which can be used to upload, download, delete, list files (and more!) from **Dropbox**, an online file sharing, synchronization and backup service. 

It's written in BASH scripting language and only needs **cURL**.

You can take a look to the [My project page](https://github.com/zjzk99/EE-800-L).

## Features

* Cross platform
* Support for the official Dropbox API v2
* No password required or stored
* Simple step-by-step configuration wizard
* Simple and chunked file upload
* File and recursive directory download
* File and recursive directory upload
* Shell wildcard expansion (only for upload)
* Delete/Move/Rename/Copy/List/Share files
* Create share link
* Monitor for changes

## Usage

The syntax is quite simple:

```
./dropbox_uploader.sh [PARAMETERS] COMMAND...

[%%]: Optional param
<%%>: Required param
```

**Available commands:**

* **upload** &lt;LOCAL_FILE/DIR ...&gt; &lt;REMOTE_FILE/DIR&gt;  
Upload a local file or directory to a remote Dropbox folder.  
If the file is bigger than 150Mb the file is uploaded using small chunks (default 50Mb); 
in this case a . (dot) is printed for every chunk successfully uploaded and a * (star) if an error 
occurs (the upload is retried for a maximum of three times).
Only if the file is smaller than 150Mb, the standard upload API is used, and if the -p option is specified
the default curl progress bar is displayed during the upload process.  
The local file/dir parameter supports wildcards expansion.

* **download** &lt;REMOTE_FILE/DIR&gt; [LOCAL_FILE/DIR]  
Download file or directory from Dropbox to a local folder

* **delete** &lt;REMOTE_FILE/DIR&gt;  
Remove a remote file or directory from Dropbox

* **move** &lt;REMOTE_FILE/DIR&gt; &lt;REMOTE_FILE/DIR&gt;  
Move or rename a remote file or directory

* **copy** &lt;REMOTE_FILE/DIR&gt; &lt;REMOTE_FILE/DIR&gt;  
Copy a remote file or directory

* **mkdir** &lt;REMOTE_DIR&gt;  
Create a remote directory on Dropbox

* **list** [REMOTE_DIR]  
List the contents of the remote Dropbox folder

* **monitor** [REMOTE_DIR] [TIMEOUT]  
Monitor the remote Dropbox folder for changes. If timeout is specified, at the first change event the function will return.

* **share** &lt;REMOTE_FILE&gt;  
Get a public share link for the specified file or directory

* **saveurl** &lt;URL&gt; &lt;REMOTE_DIR&gt;  
Download a file from an URL to a Dropbox folder directly (the file is NOT downloaded locally)

* **search** &lt;QUERY&gt;
Search for a specific pattern on Dropbox and returns the list of matching files or directories

* **info**  
Print some info about your Dropbox account

* **space**
Print some info about the space usage on your Dropbox account

* **unlink**  
Unlink the script from your Dropbox account


**Optional parameters:**  
* **-f &lt;FILENAME&gt;**  
Load the configuration file from a specific file

* **-s**  
Skip already existing files when download/upload. Default: Overwrite

* **-d**  
Enable DEBUG mode

* **-q**  
Quiet mode. Don't show progress meter or messages

* **-h**  
Show file sizes in human readable format

* **-p**  
Show cURL progress meter

* **-k**  
Doesn't check for SSL certificates (insecure)

* **-x &lt;FILENAME&gt;**  
Ignores/excludes directories or files from syncing.
-x filename -x directoryname. 

**Examples:**
```bash
    ./dropbox_uploader.sh upload /etc/passwd /myfiles/passwd.old
    ./dropbox_uploader.sh upload *.zip /
    ./dropbox_uploader.sh -x .git upload ./project /
    ./dropbox_uploader.sh download /backup.zip
    ./dropbox_uploader.sh delete /backup.zip
    ./dropbox_uploader.sh mkdir /myDir/
    ./dropbox_uploader.sh upload "My File.txt" "My File 2.txt"
    ./dropbox_uploader.sh share "My File.txt"
    ./dropbox_uploader.sh list
```

## Running as cron job
Dropbox Uploader relies on a different configuration file for each system user. The default configuration file location is `$HOME/.dropbox_uploader`. This means that if you setup the script with your user and then you try to run a cron job as root, it won't work.
So, when running this script using cron, please keep in mind the following:
* Remember to setup the script with the user used to run the cron job
* Always specify the full script path when running it (e.g.  /path/to/dropbox_uploader.sh)
* Use always the -f option to specify the full configuration file path, because sometimes in the cron environment the home folder path is not detected correctly (e.g. -f /home/youruser/.dropbox_uploader)
* My advice is, for security reasons, to not share the same configuration file with different users
 
