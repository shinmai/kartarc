import os
import errno

with open("WACKY.DAT", "rb") as datfile:
    num_files = int.from_bytes(datfile.read(2), byteorder='little') # First two bytes is number of file entries
    currfile=0
    filelist = []

    # make sure output directory exists
    try:
        os.makedirs('out')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    while(currfile<num_files): # loop through file enries
        charpos = 0
        filename = ''
        letter = datfile.read(1)

        while(letter!=bytes([00]) and charpos < 14): # only read filenames until a zero byte
            filename += letter.decode()
            letter = datfile.read(1)
            charpos += 1

        datfile.read(13-charpos) # seek to end of filename part (8.3 + 2 = 14 bytes)
        # TODO two bytes after filename probably indicate something?

        length = int.from_bytes(datfile.read(4), byteorder='little') # length of file
        offset = int.from_bytes(datfile.read(4), byteorder='little')+2 # offset of file from the beginning of the file entries, hence +2
        filelist.append((filename, offset, length))
        currfile+=1

    for file in filelist: # file = tuple (filename, offset, length)
        with open("out/" + file[0], "wb") as outfile:
            datfile.seek(file[1]) # seek to offset
            databytes = datfile.read(file[2]) # read file contents
            outfile.write(databytes) # write to disk
        print("Wrote {2:#010x} bytes to file {0:>13} from offset {1:#010x}".format(file[0],file[1],file[2]))

    print("Wrote "+str(num_files)+" files.")
    print("Done.")