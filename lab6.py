import lab6pt2.py
from pathlib import Path

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

def is_int(val):
    if type(val) == float:
        return False
    else:
        try:
            int(val)
            return True
        except ValueError:
            return False

def save_note(note: str):
    createpath()
    f.write(note + '\n')
    f.close()

def read_notes():
    p = Path(NOTES_PATH) / NOTES_FILE

    # check if storage file exists, if not return.
    if not p.exists():
        return

    print("Here are your notes: \n")
    printfile()

def remove_note() -> str:
    checkerror()
    
    print("Here are your notes: \n")
    # open and write user note to file
    f = p.open()
    id = 1
    lines = []

    # print each note with an id and store each line in a list
    for line in f:
        lines.append(line)
        print(f"{id}: {line}")
        id = id+1
    f.close()

    remove_id = input("Enter the number of the note you would like to remove: ")
    if not is_int(remove_id):
        print ("Not a valid number, cancelling operation.")
        return ""

    f = p.open('w')
    id = 1
    removed_note = ""

    for line in lines:
        if id == int(remove_id):
            removed_note = line
        else:
            f.write(line)
        id = id+1
    f.close()

    return removed_note

def run():
    note = input("Please enter a note (enter :d to delete a note or :q to exit):  ")
    if note == ":d":
        try:
            note = remove_note()
            if note is None:
                assert False, "FileNotFoundError should have been raised"
            
            print(f"The following note has been removed: \n\n {note}")
        except FileNotFoundError:
            print("The PyNote.txt file no longer exists")
    elif note == ":q":
        return
    else:    
        save_note(note)
    run()


if __name__ == "__main__":
    assert is_int(5) == True
    assert is_int("five") == False

    print("Welcome to PyNote! \n")
    read_notes()

    run()
    
###################################################################################
def createpath():
    p = Path(NOTES_PATH) / NOTES_FILE
    # check if storage file exists, if not create it.
    if not p.exists():
        p.touch(exist_ok=True)
    # open and write user note to file
    f = p.open('a')
    
def printfile():
    f = p.open()
    for line in f:
        print(line)
    f.close()

def checkerror():
    p = Path(NOTES_PATH) / NOTES_FILE
    # check if storage file exists, if not return.
    if not p.exists():
        raise FileNotFoundError("Notes file has been deleted unexpectedly")
###################################################################################
