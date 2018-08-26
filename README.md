# GB Disassembler
Tested on Windows and Mac. Runs on Python 2.7.

Simply run the file and choose your preferences.

Preferences include:
- show line numbers / hex rom addresses. ex.: 0001, 0003, 01ff
- show Bytes of current line. ex.: 01 30 00   LD BC, 0x0030
- show absolute labels. ex.: .l_0080 for jump destinations and func_046c:: for call destinations
- use RGBDS style assembly or not:
   - RGBDS style: ld bc, $1e6f
   - old style: LD BC, 0x1E6F
- first address and last address (in hex) - the range of data to print. 0000 to 7fff is memory bank 0, from then on all further memory banks are saved in (hex) 4000 increments. I.e. bank 1 lies between 8000 and bfff.
- memory bank number. This value is appended to the file name for you to distinguish them later.

Files are saved as bank + bank number + .asm

Note that any banks other than the first will not include any jump or function labels, due to the nature of bank switching. (The program would need to understand the exact paths the game's execution could take. Impossible.)
   
Enjoy!
