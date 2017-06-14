# kartarc
## a Wacky Wheels datafile packer & unpacker

A simple set of python scripts to pack and unpack files to the datafile format used by Wacky Wheels. I wrote the unpacker in a fit of nostalgia to get at the MIDI files, and after reverse engineering the format, decided to go ahead and write the packer as well.

## Usage
Place *unpack.py* and *WACKY.DAT* in the same folder and run
'''
python unpack.py
'''

If you don't own Wacky Wheels and wish to test the script out for some reason, you can use *TEST.DAT* in the repo. Just edit *unpack.py* to use it instead of *WACKY.DAT*

---

Licensed under the *Do What The Fuck You Want To Public License*, see LICENSE
