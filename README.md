# pyhexdump

Python library for printing data as hexdump.

## Example usage

~~~
> from pyhexdump import hexdump

# simulate hexdump at other offset than 0x00
> data = list(list(range(0,0xf2))*2)[:-16]
> hexdump(data, start_addr=4, addr_len=2)

      00 01 02 03  04 05 06 07  08 09 0a 0b  0c 0d 0e 0f
      -- -- -- --  -- -- -- --  -- -- -- --  -- -- -- --
0000:              00 01 02 03  04 05 06 07  08 09 0a 0b  |    ............|
0010: 0c 0d 0e 0f  10 11 12 13  14 15 16 17  18 19 1a 1b  |................|
0020: 1c 1d 1e 1f  20 21 22 23  24 25 26 27  28 29 2a 2b  |.... !"#$%&'()*+|
0030: 2c 2d 2e 2f  30 31 32 33  34 35 36 37  38 39 3a 3b  |,-./0123456789:;|
0040: 3c 3d 3e 3f  40 41 42 43  44 45 46 47  48 49 4a 4b  |<=>?@ABCDEFGHIJK|
0050: 4c 4d 4e 4f  50 51 52 53  54 55 56 57  58 59 5a 5b  |LMNOPQRSTUVWXYZ[|
0060: 5c 5d 5e 5f  60 61 62 63  64 65 66 67  68 69 6a 6b  |\]^_`abcdefghijk|
0070: 6c 6d 6e 6f  70 71 72 73  74 75 76 77  78 79 7a 7b  |lmnopqrstuvwxyz{|
0080: 7c 7d 7e 7f  80 81 82 83  84 85 86 87  88 89 8a 8b  ||}~.............|
0090: 8c 8d 8e 8f  90 91 92 93  94 95 96 97  98 99 9a 9b  |................|
00a0: 9c 9d 9e 9f  a0 a1 a2 a3  a4 a5 a6 a7  a8 a9 aa ab  |................|
00b0: ac ad ae af  b0 b1 b2 b3  b4 b5 b6 b7  b8 b9 ba bb  |................|
00c0: bc bd be bf  c0 c1 c2 c3  c4 c5 c6 c7  c8 c9 ca cb  |................|
00d0: cc cd ce cf  d0 d1 d2 d3  d4 d5 d6 d7  d8 d9 da db  |................|
00e0: dc dd de df  e0 e1 e2 e3  e4 e5 e6 e7  e8 e9 ea eb  |................|
00f0: ec ed ee ef  f0 f1 00 01  02 03 04 05  06 07 08 09  |................|

      00 01 02 03  04 05 06 07  08 09 0a 0b  0c 0d 0e 0f
      -- -- -- --  -- -- -- --  -- -- -- --  -- -- -- --
0100: 0a 0b 0c 0d  0e 0f 10 11  12 13 14 15  16 17 18 19  |................|
0110: 1a 1b 1c 1d  1e 1f 20 21  22 23 24 25  26 27 28 29  |...... !"#$%&'()|
0120: 2a 2b 2c 2d  2e 2f 30 31  32 33 34 35  36 37 38 39  |*+,-./0123456789|
0130: 3a 3b 3c 3d  3e 3f 40 41  42 43 44 45  46 47 48 49  |:;<=>?@ABCDEFGHI|
0140: 4a 4b 4c 4d  4e 4f 50 51  52 53 54 55  56 57 58 59  |JKLMNOPQRSTUVWXY|
0150: 5a 5b 5c 5d  5e 5f 60 61  62 63 64 65  66 67 68 69  |Z[\]^_`abcdefghi|
0160: 6a 6b 6c 6d  6e 6f 70 71  72 73 74 75  76 77 78 79  |jklmnopqrstuvwxy|
0170: 7a 7b 7c 7d  7e 7f 80 81  82 83 84 85  86 87 88 89  |z{|}~...........|
0180: 8a 8b 8c 8d  8e 8f 90 91  92 93 94 95  96 97 98 99  |................|
0190: 9a 9b 9c 9d  9e 9f a0 a1  a2 a3 a4 a5  a6 a7 a8 a9  |................|
01a0: aa ab ac ad  ae af b0 b1  b2 b3 b4 b5  b6 b7 b8 b9  |................|
01b0: ba bb bc bd  be bf c0 c1  c2 c3 c4 c5  c6 c7 c8 c9  |................|
01c0: ca cb cc cd  ce cf d0 d1  d2 d3 d4 d5  d6 d7 d8 d9  |................|
01d0: da db dc dd  de df e0 e1                            |........        |
~~~

## License

Copyright (c) 2024 Michael Niewöhner

This is open source software, licensed under GPLv2. See LICENSE file for details.
