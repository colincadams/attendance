# attendance

Attendance is a python script used to take attendance by entering id's of members, usually via a card reader.

## Execution
The script can be run with Python 2 or 3, as `python attendance`.

To end the script, type `quit` or `exit`. This will cause the output to be written and the script to terminate.

## Supporting Files

### Configuration File

The configuration file must be a .csv with the columns first name, last name, id. A sample configuration csv is provided (example/config.csv).

### Output File

You must supply the name that the output file will be saved under. The columns of this file are first name, last name, attended (true/false). A sample output is provided (example/attendance.csv).

## Future Development

* In the current implementation the output file isn't written until the end. This means that if the script crashes all input and records are lost. We will explore having the input stored in a temporary file so that it can be restored or the session can be resumed in the future.

* Create a simple GUI (likely PyQt) and PyInstaller executables to make it easier to use for those unfamiliar with CLIs.
