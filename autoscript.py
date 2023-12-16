# This library needs to be installed
import pyautogui as pyag

# Seconds of pause between each command
STD_DELAY = 0.1

# Delay after CPP command
# CPP can be a bit slow, so I set it to be a bit longer.
# If you find it to be too slow, feel free to shorten it.
CPP_DELAY = 10

# Delay after show-code command.
# Again, feel free to shorten this if it's too long.
SHOW_CODE_DELAY = 7.5

# Countdown before the script starts typing
COUNTDOWN = 5

# This array handles the test runs of your program.
# Type your inputs directly into the array.
# Each string should be separated by a comma.
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
    "# Run 2: Negative and positive integer",
    "./demo_lab.out",
    "-15",
    "4",

    # Run 3:
    "# Run 3: Two negative integers",
    "./demo_lab.out",
    "-5",
    "-3"
]


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
    
    # Change the three lines below to include 
    # the file names for your program

    write_ln("cat demo_lab.info") 

    # If you have multiple files, you can type
    # them all in the same show-code command, i.e.
    # show-code demo_lab.cpp library_name.h library_name.cpp
    write_ln("show-code demo_lab.cpp", SHOW_CODE_DELAY) 

    write_ln("CPP demo_lab.cpp", CPP_DELAY)


def script_body():
    for line in TEST_RUN_INPUTS:
        write_ln(line)


def script_end():
    # Change this line to include your tpq file
    # If you don't have a tpq, you can 
    # comment it out with a `#`
    write_ln("cat demo_lab.tpq") 

    write_ln("exit")

    # Change this line to include your desired PDF name
    write_ln("script-print Last-First-DemoLab")

    print("Script finished!\n")


def main():
    script_countdown()
    script_setup()
    script_body()
    script_end()


# Entry point of the script
if __name__ == "__main__":
    main()
