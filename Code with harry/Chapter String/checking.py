# print("Enter the Name of Source File: ")
# sFile = input()
# print("Enter the Name of Target File: ")
# tFile = input()

# fileHandle = open(sFile, "r")
# texts = fileHandle.readlines()
# fileHandle.close()

# fileHandle = open(tFile, "w")
# for s in texts:
#     fileHandle.write(s)
# fileHandle.close()

# print("\nFile Copied Successfully!")

sfile = input()
tfile = input()

with open(sfile, "r") as shandle:
    with open(tfile, "w") as thandle:
        for line in shandle:
            thandle.write(line)