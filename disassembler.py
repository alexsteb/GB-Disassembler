fileName = input("Enter GB ROM filename: ")
lineNums = input("Show line numbers? (y/n) ")
showBytes = input("Show bytes? (y/n) ")
lcStyle = input("RGBDS style Assembly? (y/n) ")
jumps = input("Show absolute labels? (y/n) ")
starth = input("Enter first address (hex): ")
endh = input("Enter last address (hex): ")
membank = input("Memory bank number: ")


start = int(starth, 16)
end = int(endh, 16)+1




f = open(fileName, "rb")
hexStringList = []
hexList = []
length = end - start
try:
	if start > 0: 
		f.read(start)
	byte = f.read(1)
	while length > -50 and byte != "" and len(byte) != 0:
		hexStringList.append("%02X" % ord( byte ))
		hexList.append(ord(byte))
		byte = f.read(1)
		length -= 1
finally:
	f.close()


ops = []
addresses = []
byteLists = []
skip = 0

_byteList = []

fo = open("bank"+membank+".asm","w+")

for ite in range(0,len(hexList) - (-length)):
	
	b = hexList[ite]

	if len(_byteList) > 0 and skip == 0:
		byteLists.append(_byteList)
		_byteList = []

	_byteList.append(b)

	if skip > 0:
		skip -= 1
		continue




	addresses.append(ite + start)


	if ite+start >= 0x104 and ite+start <= 0x113:
		text = "db "
		while ite+start <= 0x113:
			text += ("%02X" % hexList[ite]) + ", "
			skip += 1
			ite += 1
		skip -= 1
		ops.append(text)
		continue
	if ite+start >= 0x114 and ite+start <= 0x123:
		text = "db "
		while ite+start <= 0x123:
			text += ("%02X" % hexList[ite]) + ", "
			skip += 1
			ite += 1
		skip -= 1
		ops.append(text)
		continue
	if ite+start >= 0x124 and ite+start <= 0x133:
		text = "db "
		while ite+start <= 0x133:
			text += ("%02X" % hexList[ite]) + ", "
			skip += 1
			ite += 1
		skip -= 1
		ops.append(text)
		continue
	if ite+start >= 0x134 and ite+start <= 0x142:
		text = "db \""
		while ite+start <= 0x142:
			text += (chr(hexList[ite]))
			skip += 1
			ite += 1
		skip -= 1
		text += "\""
		ops.append(text)
		continue



	n = ""
	n2 = ""
	if ite < len(hexList)-1: n = ("%02X" % hexList[ite + 1])
	if ite < len(hexList)-2: n2 = ("%02X" % hexList[ite + 2])
	nn = "0x" + n2 + n
	n = "0x" + n
	me = "0x" + ("%02X" % hexList[ite])

	if ite+start == 0x143: 
		ops.append("db "+me+"		;DMG - classic gameboy")
		continue
	if ite+start == 0x144:
		ops.append("db "+me+", 0x"+n+"		;new license")
		skip += 1
		continue
	if ite+start == 0x146: 
		ops.append("db "+me+"		;SGB flag: not SGB compatible")
		continue
	if ite+start == 0x147: 
		ops.append("db "+me+"		;cart type: ROM")
		continue
	if ite+start == 0x148: 
		ops.append("db "+me+"		;ROM size: 32 kb")
		continue
	if ite+start == 0x149: 
		ops.append("db "+me+"		;RAM size: 0 b")
		continue
	if ite+start == 0x14a: 
		ops.append("db "+me+"		;destination code: Japanese")
		continue
	if ite+start == 0x14b: 
		ops.append("db "+me+"		;old license: not SGB compatible")
		continue
	if ite+start == 0x14c: 
		ops.append("db "+me+"		;mask ROM version number")
		continue
	if ite+start == 0x14d: 
		ops.append("db "+me+"		;header check (OK)")
		continue
	if ite+start == 0x14e: 
		skip += 1
		ops.append("db "+me+", "+n+"		;global check (OK)")
		continue



	if b == 0x00: ops.append("NOP")
	if b == 0x01: 
		ops.append("LD BC, "+nn)
		skip += 2
	if b == 0x02: ops.append("LD (BC), A")
	if b == 0x03: ops.append("INC BC")
	if b == 0x04: ops.append("INC B")
	if b == 0x05: ops.append("DEC B")
	if b == 0x06: 
		ops.append("LD B, "+n)
		skip += 1
	if b == 0x07: ops.append("RLC A")
	if b == 0x08: 
		ops.append("LD ("+nn+"), SP")
		skip += 2
	if b == 0x09: ops.append("ADD HL, BC")
	if b == 0x0a: ops.append("LD A, (BC)")
	if b == 0x0b: ops.append("DEC BC")
	if b == 0x0c: ops.append("INC C")
	if b == 0x0d: ops.append("DEC C")
	if b == 0x0e: 
		ops.append("LD C, "+n)
		skip += 1
	if b == 0x0f: ops.append("RRC A")

	if b == 0x10: ops.append("STOP")
	if b == 0x11: 
		ops.append("LD DE, "+nn)
		skip += 2
	if b == 0x12: ops.append("LD (DE), A")
	if b == 0x13: ops.append("INC DE")
	if b == 0x14: ops.append("INC D")
	if b == 0x15: ops.append("DEC D")
	if b == 0x16: 
		ops.append("LD D, "+n)
		skip += 1
	if b == 0x17: ops.append("RL A")
	if b == 0x18: 
		ops.append("JR "+n)
		skip += 1
	if b == 0x19: ops.append("ADD HL, DE")
	if b == 0x1a: ops.append("LD A, (DE)")
	if b == 0x1b: ops.append("DEC DE")
	if b == 0x1c: ops.append("INC E")
	if b == 0x1d: ops.append("DEC E")
	if b == 0x1e: 
		ops.append("LD E, "+n)
		skip += 1
	if b == 0x1f: ops.append("RR A")

	if b == 0x20: 
		ops.append("JR NZ, "+n)
		skip += 1
	if b == 0x21: 
		ops.append("LD HL, "+nn)
		skip += 2
	if b == 0x22: ops.append("LDI (HL), A")
	if b == 0x23: ops.append("INC HL")
	if b == 0x24: ops.append("INC H")
	if b == 0x25: ops.append("DEC H")
	if b == 0x26: 
		ops.append("LD H, "+n)
		skip += 1
	if b == 0x27: ops.append("DAA")
	if b == 0x28: 
		ops.append("JR Z, "+n)
		skip += 1
	if b == 0x29: ops.append("ADD HL, HL")
	if b == 0x2a: ops.append("LDI A, (HL)")
	if b == 0x2b: ops.append("DEC HL")
	if b == 0x2c: ops.append("INC L")
	if b == 0x2d: ops.append("DEC L")
	if b == 0x2e: 
		ops.append("LD L, "+n)
		skip += 1
	if b == 0x2f: ops.append("CPL")

	if b == 0x30: 
		ops.append("JR NC, "+n)
		skip += 1
	if b == 0x31: 
		ops.append("LD SP, "+nn)
		skip += 2
	if b == 0x32: ops.append("LDD (HL), A")
	if b == 0x33: ops.append("INC SP")
	if b == 0x34: ops.append("INC (HL)")
	if b == 0x35: ops.append("DEC (HL)")
	if b == 0x36: 
		ops.append("LD (HL), "+n)
		skip += 1
	if b == 0x37: ops.append("SCF")
	if b == 0x38: 
		ops.append("JR C, "+n)
		skip += 1
	if b == 0x39: ops.append("ADD HL, SP")
	if b == 0x3a: ops.append("LDD A, (HL)")
	if b == 0x3b: ops.append("DEC SP")
	if b == 0x3c: ops.append("INC A")
	if b == 0x3d: ops.append("DEC A")
	if b == 0x3e: 
		ops.append("LD A, "+n)
		skip += 1
	if b == 0x3f: ops.append("CCF")

	if b == 0x40: ops.append("LD B, B")
	if b == 0x41: ops.append("LD B, C")
	if b == 0x42: ops.append("LD B, D")
	if b == 0x43: ops.append("LD B, E")
	if b == 0x44: ops.append("LD B, H")
	if b == 0x45: ops.append("LD B, L")
	if b == 0x46: ops.append("LD B, (HL)")
	if b == 0x47: ops.append("LD B, A")
	if b == 0x48: ops.append("LD C, B")
	if b == 0x49: ops.append("LD C, C")
	if b == 0x4a: ops.append("LD C, D")
	if b == 0x4b: ops.append("LD C, E")
	if b == 0x4c: ops.append("LD C, H")
	if b == 0x4d: ops.append("LD C, L")
	if b == 0x4e: ops.append("LD C, (HL)")
	if b == 0x4f: ops.append("LD C, A")

	if b == 0x50: ops.append("LD D, B")
	if b == 0x51: ops.append("LD D, C")
	if b == 0x52: ops.append("LD D, D")
	if b == 0x53: ops.append("LD D, E")
	if b == 0x54: ops.append("LD D, H")
	if b == 0x55: ops.append("LD D, L")
	if b == 0x56: ops.append("LD D, (HL)")
	if b == 0x57: ops.append("LD D, A")
	if b == 0x58: ops.append("LD E, B")
	if b == 0x59: ops.append("LD E, C")
	if b == 0x5a: ops.append("LD E, D")
	if b == 0x5b: ops.append("LD E, E")
	if b == 0x5c: ops.append("LD E, H")
	if b == 0x5d: ops.append("LD E, L")
	if b == 0x5e: ops.append("LD E, (HL)")
	if b == 0x5f: ops.append("LD E, A")

	if b == 0x60: ops.append("LD H, B")
	if b == 0x61: ops.append("LD H, C")
	if b == 0x62: ops.append("LD H, D")
	if b == 0x63: ops.append("LD H, E")
	if b == 0x64: ops.append("LD H, H")
	if b == 0x65: ops.append("LD H, L")
	if b == 0x66: ops.append("LD H, (HL)")
	if b == 0x67: ops.append("LD H, A")
	if b == 0x68: ops.append("LD L, B")
	if b == 0x69: ops.append("LD L, C")
	if b == 0x6a: ops.append("LD L, D")
	if b == 0x6b: ops.append("LD L, E")
	if b == 0x6c: ops.append("LD L, H")
	if b == 0x6d: ops.append("LD L, L")
	if b == 0x6e: ops.append("LD L, (HL)")
	if b == 0x6f: ops.append("LD L, A")

	if b == 0x70: ops.append("LD (HL), B")
	if b == 0x71: ops.append("LD (HL), C")
	if b == 0x72: ops.append("LD (HL), D")
	if b == 0x73: ops.append("LD (HL), E")
	if b == 0x74: ops.append("LD (HL), H")
	if b == 0x75: ops.append("LD (HL), L")
	if b == 0x76: ops.append("HALT")
	if b == 0x77: ops.append("LD (HL), A")
	if b == 0x78: ops.append("LD A, B")
	if b == 0x79: ops.append("LD A, C")
	if b == 0x7a: ops.append("LD A, D")
	if b == 0x7b: ops.append("LD A, E")
	if b == 0x7c: ops.append("LD A, H")
	if b == 0x7d: ops.append("LD A, L")
	if b == 0x7e: ops.append("LD A, (HL)")
	if b == 0x7f: ops.append("LD A, A")

	if b == 0x80: ops.append("ADD A, B")
	if b == 0x81: ops.append("ADD A, C")
	if b == 0x82: ops.append("ADD A, D")
	if b == 0x83: ops.append("ADD A, E")
	if b == 0x84: ops.append("ADD A, H")
	if b == 0x85: ops.append("ADD A, L")
	if b == 0x86: ops.append("ADD A, (HL)")
	if b == 0x87: ops.append("ADD A, A")
	if b == 0x88: ops.append("ADC A, B")
	if b == 0x89: ops.append("ADC A, C")
	if b == 0x8a: ops.append("ADC A, D")
	if b == 0x8b: ops.append("ADC A, E")
	if b == 0x8c: ops.append("ADC A, H")
	if b == 0x8d: ops.append("ADC A, L")
	if b == 0x8e: ops.append("ADC A, (HL)")
	if b == 0x8f: ops.append("ADC A, A")

	if b == 0x90: ops.append("SUB A, B")
	if b == 0x91: ops.append("SUB A, C")
	if b == 0x92: ops.append("SUB A, D")
	if b == 0x93: ops.append("SUB A, E")
	if b == 0x94: ops.append("SUB A, H")
	if b == 0x95: ops.append("SUB A, L")
	if b == 0x96: ops.append("SUB A, (HL)")
	if b == 0x97: ops.append("SUB A, A")
	if b == 0x98: ops.append("SBC A, B")
	if b == 0x99: ops.append("SBC A, C")
	if b == 0x9a: ops.append("SBC A, D")
	if b == 0x9b: ops.append("SBC A, E")
	if b == 0x9c: ops.append("SBC A, H")
	if b == 0x9d: ops.append("SBC A, L")
	if b == 0x9e: ops.append("SBC A, (HL)")
	if b == 0x9f: ops.append("SBC A, A")

	if b == 0xa0: ops.append("AND B")
	if b == 0xa1: ops.append("AND C")
	if b == 0xa2: ops.append("AND D")
	if b == 0xa3: ops.append("AND E")
	if b == 0xa4: ops.append("AND H")
	if b == 0xa5: ops.append("AND L")
	if b == 0xa6: ops.append("AND (HL)")
	if b == 0xa7: ops.append("AND A")
	if b == 0xa8: ops.append("XOR B")
	if b == 0xa9: ops.append("XOR C")
	if b == 0xaa: ops.append("XOR D")
	if b == 0xab: ops.append("XOR E")
	if b == 0xac: ops.append("XOR H")
	if b == 0xad: ops.append("XOR L")
	if b == 0xae: ops.append("XOR (HL)")
	if b == 0xaf: ops.append("XOR A")

	if b == 0xb0: ops.append("OR B")
	if b == 0xb1: ops.append("OR C")
	if b == 0xb2: ops.append("OR D")
	if b == 0xb3: ops.append("OR E")
	if b == 0xb4: ops.append("OR H")
	if b == 0xb5: ops.append("OR L")
	if b == 0xb6: ops.append("OR (HL)")
	if b == 0xb7: ops.append("OR A")
	if b == 0xb8: ops.append("CP B")
	if b == 0xb9: ops.append("CP C")
	if b == 0xba: ops.append("CP D")
	if b == 0xbb: ops.append("CP E")
	if b == 0xbc: ops.append("CP H")
	if b == 0xbd: ops.append("CP L")
	if b == 0xbe: ops.append("CP (HL)")
	if b == 0xbf: ops.append("CP A")

	if b == 0xc0: ops.append("RET NZ")
	if b == 0xc1: ops.append("POP BC")
	if b == 0xc2: 
		ops.append("JP NZ, "+nn)
		skip += 2

	if b == 0xc3: 
		ops.append("JP "+nn)
		skip += 2

	if b == 0xc4: 
		ops.append("CALL NZ, "+nn)
		skip += 2
	if b == 0xc5: ops.append("PUSH BC")
	if b == 0xc6: 
		ops.append("ADD A, "+n)
		skip += 1
	if b == 0xc7: ops.append("RST 0")
	if b == 0xc8: ops.append("RET Z")
	if b == 0xc9: ops.append("RET")
	if b == 0xca: 
		ops.append("JP Z, "+nn)
		skip += 2
	if b == 0xcb:
		skip += 1
		v = hexList[ite + 1]
		text = ""
		if v >= 0x00 and v <= 0x07: text += "RLC "
		if v >= 0x08 and v <= 0x0f: text += "RRC "
		if v >= 0x10 and v <= 0x17: text += "RL "
		if v >= 0x18 and v <= 0x1f: text += "RR "
		if v >= 0x20 and v <= 0x27: text += "SLA "
		if v >= 0x28 and v <= 0x2f: text += "SRA "
		if v >= 0x30 and v <= 0x37: text += "SWAP "
		if v >= 0x38 and v <= 0x3f: text += "SRL "
		if v >= 0x40 and v <= 0x47: text += "BIT 0, "
		if v >= 0x48 and v <= 0x4f: text += "BIT 1, "
		if v >= 0x50 and v <= 0x57: text += "BIT 2, "
		if v >= 0x58 and v <= 0x5f: text += "BIT 3, "
		if v >= 0x60 and v <= 0x67: text += "BIT 4, "
		if v >= 0x68 and v <= 0x6f: text += "BIT 5, "
		if v >= 0x70 and v <= 0x77: text += "BIT 6, "
		if v >= 0x78 and v <= 0x7f: text += "BIT 7, "
		if v >= 0x80 and v <= 0x87: text += "RES 0, "
		if v >= 0x88 and v <= 0x8f: text += "RES 1, "
		if v >= 0x90 and v <= 0x97: text += "RES 2, "
		if v >= 0x98 and v <= 0x9f: text += "RES 3, "
		if v >= 0xA0 and v <= 0xA7: text += "RES 4, "
		if v >= 0xA8 and v <= 0xAf: text += "RES 5, "
		if v >= 0xB0 and v <= 0xB7: text += "RES 6, "
		if v >= 0xB8 and v <= 0xBf: text += "RES 7, "
		if v >= 0xC0 and v <= 0xC7: text += "SET 0, "
		if v >= 0xC8 and v <= 0xCf: text += "SET 1, "
		if v >= 0xD0 and v <= 0xD7: text += "SET 2, "
		if v >= 0xD8 and v <= 0xDf: text += "SET 3, "
		if v >= 0xE0 and v <= 0xE7: text += "SET 4, "
		if v >= 0xE8 and v <= 0xEf: text += "SET 5, "
		if v >= 0xF0 and v <= 0xF7: text += "SET 6, "
		if v >= 0xF8 and v <= 0xFf: text += "SET 7, "

		n = (v % 16)
		if n == 0 or n == 8: text += "B"
		if n == 1 or n == 9: text += "C"
		if n == 2 or n == 10: text += "D"
		if n == 3 or n == 11: text += "E"
		if n == 4 or n == 12: text += "H"
		if n == 5 or n == 13: text += "L"
		if n == 6 or n == 14: text += "(HL)"
		if n == 7 or n == 15: text += "A"
		ops.append(text)

	if b == 0xcc: 
		ops.append("CALL Z, "+nn)
		skip += 2
	if b == 0xcd: 
		ops.append("CALL "+nn)
		skip += 2
	if b == 0xce: 
		ops.append("ADC A, "+n)
		skip += 1
	if b == 0xcf: ops.append("RST 8")

	if b == 0xd0: ops.append("RET NC")
	if b == 0xd1: ops.append("POP DE")
	if b == 0xd2: 
		ops.append("JP NC, "+nn)
		skip += 2
	if b == 0xd3: ops.append("<ERROR>")
	if b == 0xd4: 
		ops.append("CALL NC, "+nn)
		skip += 2
	if b == 0xd5: ops.append("PUSH DE")
	if b == 0xd6: 
		ops.append("SUB A, "+n)
		skip += 1
	if b == 0xd7: ops.append("RST 10")
	if b == 0xd8: ops.append("RET C")
	if b == 0xd9: ops.append("RETI")
	if b == 0xda: 
		ops.append("JP C, "+nn)
		skip += 2
	if b == 0xdb: ops.append("<ERROR>")
	if b == 0xdc: 
		ops.append("CALL C, "+nn)
		skip += 2
	if b == 0xdd: ops.append("<ERROR>")
	if b == 0xde: 
		ops.append("SBC A, "+n)
		skip += 1
	if b == 0xdf: ops.append("RST 18")

	if b == 0xe0: 
		ops.append("LDH (0xFF00 + "+n+"), A")
		skip += 1
	if b == 0xe1: ops.append("POP HL")
	if b == 0xe2: ops.append("LDH (C), A")
	if b == 0xe3: ops.append("<ERROR>")
	if b == 0xe4: ops.append("<ERROR>")
	if b == 0xe5: ops.append("PUSH HL")
	if b == 0xe6: 
		ops.append("AND "+n)
		skip += 1
	if b == 0xe7: ops.append("RST 20")
	if b == 0xe8: ops.append("ADD SP, d")
	if b == 0xe9: ops.append("JP (HL)")
	if b == 0xea: 
		ops.append("LD ("+nn+"), A")
		skip += 2
	if b == 0xeb: ops.append("<ERROR>")
	if b == 0xec: ops.append("<ERROR>")
	if b == 0xed: ops.append("<ERROR>")
	if b == 0xee: 
		ops.append("XOR "+n)
		skip += 1
	if b == 0xef: ops.append("RST 28")

	if b == 0xf0: 
		ops.append("LDH A, (0xFF00 + "+n+")")
		skip += 1
	if b == 0xf1: ops.append("POP AF")
	if b == 0xf2: ops.append("<ERROR>")
	if b == 0xf3: ops.append("DI")
	if b == 0xf4: ops.append("<ERROR>")
	if b == 0xf5: ops.append("PUSH AF")
	if b == 0xf6: 
		ops.append("OR "+n)
		skip += 1
	if b == 0xf7: ops.append("RST 30")
	if b == 0xf8: ops.append("LDHL SP, d")
	if b == 0xf9: ops.append("LD SP, HL")
	if b == 0xfa: 
		ops.append("LD A, ("+nn+")")
		skip += 2
	if b == 0xfb: ops.append("EI")
	if b == 0xfc: ops.append("<ERROR>")
	if b == 0xfd: ops.append("<ERROR>")
	if b == 0xfe: 
		ops.append("CP "+n)
		skip += 1
	if b == 0xff: ops.append("RST 38")

if len(_byteList) > 0:
	byteLists.append(_byteList)	

#Change JR labels
for ite,op in enumerate(ops):
	if op[0:2] == "JR":
		val = byteLists[ite][-1]
		#fo.write (val)
		if val > 127:
			signedVal = -256+val + 2
		else: 
			signedVal = val + 2
		_new = (("%04X" % (addresses[ite] + signedVal)))
		#fo.write (_new)
		#fo.write (op[-2:])
		ops[ite] =ops[ite].replace(op[-2:],_new)

#Add labels
jmpLabels = set()
jrLabels = set()
callLabels = set()
if jumps == "y":
	for ite,op in enumerate(ops):
		if op[0:2] == "JP" and op != "JP (HL)":
			jmpLabels.add(op[-4:])

		if op[0:2] == "JR":
			jrLabels.add(op[-4:])

		if op[0:4] == "CALL":
			callLabels.add(op[-4:])

#fo.write (jmpLabels)

for ite,op in enumerate(ops):
	hexAddressBig = ("%04X" % addresses[ite])

	if lcStyle == "y":
		hexAddress = hexAddressBig.lower()

	
	if hexAddressBig in callLabels:
		fo.write ("\n")
		fo.write ("\n")
		fo.write ("func_"+hexAddress+"::\n")
	

	if (hexAddressBig in jmpLabels or hexAddressBig in jrLabels) and not hexAddressBig in callLabels:
		fo.write ("\n")
		fo.write (".l_"+hexAddress+":\n")


	if op[0:2] == "JP" and op[-4:] in jmpLabels and not op[-4:] in callLabels:
		op = op.replace(op[-6:], ".l_"+op[-4:])

	if op[0:2] == "JR" and op[-4:] in jrLabels and not op[-4:] in callLabels:
		op = op.replace(op[-6:], ".l_"+op[-4:])
	
	if op[0:4] == "CALL" and op[-4:] in callLabels:
		op = op.replace(op[-6:], "func_"+op[-4:])

	if lcStyle == "y":
		op = op.replace("(","[")
		op = op.replace(")","]")
		op = op.replace("0x","$")
		if addresses[ite] != 0x134: op = op.lower()
		
	output = ""
	if lineNums == "y":
		output += hexAddress
	
	bytesText = ""
	if showBytes == "y":
		output += " "
		count = 0
		for byte in byteLists[ite]:
			count += 1
			if count == 5:
				bytesText = bytesText[0:-1] + "+  "
				break

			bytesText += ("%02X" % byte) + " "
		bytesText = bytesText[0:-1]
		while len(bytesText) < 13:
			bytesText += " "
	else:
		bytesText = "\t"
	
	output += bytesText + op

	
	fo.write (output+"\n")

fo.close()		
#fo.write (byteLists)

exit(1)
