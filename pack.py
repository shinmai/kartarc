import binascii
import os

#TODO argument handling
with open("TEST.DAT", "wb") as datfile:
	files = os.listdir('in') #TODO parametrize indir and/or infilelist
	num_files = len(files) # get number of files for filelist header
	datfile.write(num_files.to_bytes(2, byteorder='little')) # write filelist header

	datas = b''
	offset = (num_files*22) # initial offset, just after filelist
	for filename in files:
		with open('in/'+filename, "rb") as infile:
			data = infile.read() # read file contents ...
			datas+=data # ... and add to bytes to be written after filelist
			datfile.write(filename.encode()) # write filename ...
			datfile.write(binascii.unhexlify('00' * (14-len(filename)))) # ... with padding ...
			datfile.write(len(data).to_bytes(4, byteorder='little')) # ... & length ...
			datfile.write(offset.to_bytes(4, byteorder='little')) # ... & offset
			offset+=len(data) # increment offset for next file
	datfile.write(datas) # append data after filelist
	# TODO write data immediately to avoid loading whole file catalogue to memory