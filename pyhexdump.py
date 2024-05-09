from itertools import islice, zip_longest

def hexdump(data, start_addr=0, addr_len=4):
    data = iter(data)
    fill = start_addr % 16
    yaddr = start_addr & ~0x0f

    indent = " " * (addr_len*2 + 2)
    header = "\n" + indent + "00 01 02 03  04 05 06 07  08 09 0a 0b  0c 0d 0e 0f\n" + \
                    indent + "-- -- -- --  -- -- -- --  -- -- -- --  -- -- -- --"

    while True:
        _data = list(islice(data, 16 - fill))
        if not _data:
            break

        # prefix with spaces when starting at addr > 0
        hex_data  = ["  "] * fill

        hex_data += list(map("{:02x}".format, _data))

        # fill up shorter last data chunk with spaces to align charater dump
        hex_data += ["  "] * (16 - len(_data) - fill)

        # format in chunks of 4 bytes
        chunks = zip_longest(*[iter(hex_data)]*4, fillvalue="  ")
        hex_data = '  '.join(' '.join(chunk) for chunk in chunks)

        str_data  = " " * fill
        str_data += "".join((chr(x) if 32 <= x < 127 else "." for x in _data))
        str_data += " " * (16 - len(_data) - fill)

        if yaddr & 0xff == 0x00 or yaddr == start_addr:
            print(header)

        print(f'{yaddr:0{addr_len*2}x}: {hex_data}  |{str_data}|')

        yaddr += 16
        fill = 0

