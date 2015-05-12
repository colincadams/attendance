# attendance

Attendance is a python script used to take attendance by entering id's of members, usually via a card reader.

The script is normally run simply as an executable, assuming you have Python 3 installed at `/usr/bin/python3`. If this is not the case, you can change the header of the file to the location of your python executable, or you can simply run the executable with python, as `python3 attendance`.

To end the script, type `quit` or `exit`. This will cause the output to be written and the script to terminate.

## Supporting Files

### Configuration File

The configuration file must be a .csv with the columns first name, last name, id. The member csv is provided (config.csv).

### Output File

You must supply the name that the output file will be saved under. The columns of this file are first name, last name, attended (true/false).

## Notes

In the current implementation, the output isn't written until the end. This means that if the script crashes, all input and records are lost. We will explore having the input stored in a temporary file, so that it can be restored, or the session can be resumed in the future.


