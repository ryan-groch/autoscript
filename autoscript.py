# This library needs to be installed
import pyautogui as pyag

"""
For show-code and compile commands:
Both of these can include multiple file names, e.g.
`show-code progname.cpp libraryname.h libraryname.cpp`
"""
SHOW_CODE_COMMAND = "show-code demo_lab.cpp"
COMPILE_COMMAND = "CPP demo_lab.cpp"

"""
Delays:

Adjust these as desired. If they are too short, then
the commands may be typed too quickly for the server
to process them. It is safer to have these be larger,
but that also makes the script take a longer time.

These must all be non-negative numeric values,
and COUNTDOWN must be a non-negative integer.

All of these are in seconds, not milliseconds.
"""
STD_DELAY = 0.25        # Seconds of pause between each command
COMPILE_DELAY = 10      # Pause after typing compile command
SHOW_CODE_DELAY = 7.5   # Pause after typing show-code command
COUNTDOWN = 5           # Countdown before starting script

"""
File names:

Leave these as empty strings if not relevant.
An empty string is just two empty quotes: ""
"""
INFO_FILE = "demo_lab.info"     
TPQ_FILE = "demo_lab.tpq"
DESIRED_PDF_NAME = "Last-First-DemoLab"

"""
Test Run Inputs:

This array handles the test runs of your program.
Type your inputs directly into the array.
Each string should be separated by a comma.
"""
TEST_RUN_INPUTS = [
    # I've added some bash comments to demonstrate
    # that you can label the test runs of your program,
    # if you choose to do so.

    # Run 1
    "# Run 1: Two positive integers", # types a bash comment
    "./demo_lab.out",
    "2",
    "3",

    # Run 2
    "# Run 2: Negative and positive integers",
    "./demo_lab.out",
    "-15",
    "4",

    # Run 3:
    "# Run 3: Two negative integers",
    "./demo_lab.out",
    "-5",
    "-3"
]

# No need to edit anything below. 
# All settings can be adjusted by editing the constants above.

def write_ln(line, delay=STD_DELAY):
    pyag.write(line)
    pyag.press("enter")
    pyag.sleep(delay)


def script_countdown():
    print("\nPlease put your cursor in your SSH terminal. "
          "\nTo interrupt this script, you may move your mouse "
          "to any corner of your screen."
          "\n\nStarting script in:")

    for i in range(COUNTDOWN):
        for j in range(4):
            print(COUNTDOWN - i if j == 0 else ".", 
                       end="\n" if j == 3 else " ",
                                        flush=True)
            pyag.sleep(0.25)
    
    print("\nStarting script...\n")


def script_setup():
    write_ln("script")
    write_ln("pwd")
    
    if INFO_FILE.strip():
        write_ln(f"cat {INFO_FILE}") 

    if SHOW_CODE_COMMAND.strip():
        write_ln(SHOW_CODE_COMMAND, SHOW_CODE_DELAY) 

    if COMPILE_COMMAND.strip():
        write_ln(COMPILE_COMMAND, COMPILE_DELAY)


def script_test_runs():
    for line in TEST_RUN_INPUTS:
        write_ln(line)


def script_end():
    if TPQ_FILE.strip():
        write_ln(f"cat {TPQ_FILE}") 

    write_ln("exit")

    if DESIRED_PDF_NAME.strip():
        write_ln(f"script-print {DESIRED_PDF_NAME}")

    print("Script finished!\n")


def main():
    script_countdown()
    script_setup()
    script_test_runs()
    script_end()


if __name__ == "__main__":
    main()
