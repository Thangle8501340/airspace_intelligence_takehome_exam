# Problem
How do we hire:
We look at the interview process not as a screening or test, but rather as an opportunity to simulate what it would look like working together. We build the interview process around you.
In case you’re interested in taking a shortcut through our application process - try a little puzzle on for size. Below you’ll find an array of bytes. Once decoded, it will reveal the hiring manager’s e-mail. Send an e-mail with the subject “Squawk!” and we’ll get in touch right away! Send in your code as well!
[35,44,47,36,33,13,44,36,63,62,61,44,46,40,96,36,35,57,40,33,33,36,42,40,35,46,40,99,46,34,32]

Each character in the hiring manager’s email was translated into the byte array above by first converting each character into its Unicode integer representation, and then XOR’ing each integer with a secret key.
In order to find the key - you’ll have to do some aviation research into squawk codes. Specifically - the key will be the squawk code used to signal a generic emergency, with any leading or trailing 0’s trimmed out. Happy decoding!


# Research
SQUAWK CODE - aircraft codes

77-> key
The general, universal emergency squawk code is 7700. Setting a transponder to 7700 immediately alerts Air Traffic Control (ATC) to a distress situation, causing the aircraft to stand out on radar screens, enabling priority handling and assistance. 

Wayman Flight School +3
Key Emergency Codes:
7700: General Emergency (e.g., engine failure, medical, depressurization).



TIME START: 6:30PM
In case you’re interested in taking a shortcut through our application process - try a little puzzle on for size. Below you’ll find an array of bytes. Once decoded, it will reveal the hiring manager’s e-mail. Send an e-mail with the subject “Squawk!” and we’ll get in touch right away! Send in your code as well!

[35,44,47,36,33,13,44,36,63,62,61,44,46,40,96,36,35,57,40,33,33,36,42,40,35,46,40,99,46,34,32]
Each character in the hiring manager’s email was translated into the byte array above by first converting each character into its Unicode integer representation, and then XOR’ing each integer with a secret key.
In order to find the key - you’ll have to do some aviation research into squawk codes. Specifically - the key will be the squawk code used to signal a generic emergency, with any leading or trailing 0’s trimmed out. Happy decoding!


squawk codes:

[Squawk codes are four-digit, octal (0-7) numbers entered into an aircraft transponder to identify it on Air Traffic Control (ATC) radar. They allow for 
 (4,096) unique combinations]

 An array of bytes:
 [35,44,47,36,33,13,44,36,63,62,61,44,46,40,96,36,35,57,40,33,33,36,42,40,35,46,40,99,46,34,32]


What to do:
Each character in the hiring manager’s email was translated into the byte array above by first converting each character into its Unicode integer representation, and then XOR’ing each integer with a secret key.

Step 1:
- EACH CHARACTER -> UNICODE INTEGER REPRESENTATION 
- THEN XOR’ing each integer with a secret key.

UNICODE INTEGER REPRESENTATION
While we usually see them in hex (like U+0041), they are fundamentally just base-10 integers.
Character	Unicode Code Point (Hex)	Integer Representation (Decimal)
A	U+0041	65
a	U+0061	97
1	U+0031	49
!	U+0021	33

# Coding
EXAMPLES:
USING AI TO GET EXAMPLES
iwillstealthemoon@gmail.com
[36, 58, 36, 33, 33, 62, 57, 40, 44, 33, 57, 37, 40, 32, 34, 34, 35, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32]
spaceiscool@gmail.com
[62, 61, 44, 46, 40, 36, 62, 46, 34, 34, 33, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32]
airspaceintelligent@gmail.com
[44, 36, 63, 62, 61, 44, 46, 40, 36, 35, 57, 40, 33, 33, 36, 42, 40, 35, 57, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32]


STEP BY STEP process
iwillstealthemoon@gmail.com
[36, 58, 36, 33, 33, 62, 57, 40, 44, 33, 57, 37, 40, 32, 34, 34, 35, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32]

--- How that byte array is built (secret key = 77) ---

For each character you do:  (1) get Unicode number  (2) XOR with 77  →  that’s one byte.
```
  #   char   Step 1: ord(char)   Step 2: ord XOR 77   →  byte in array
 ---  -----  -----------------  ------------------   -----------------
  0   'i'    ord('i') = 105      105 XOR 77 = 36     →  byte[0]  = 36
  1   'w'    ord('w') = 119      119 XOR 77 = 58     →  byte[1]  = 58
  2   'i'    ord('i') = 105      105 XOR 77 = 36     →  byte[2]  = 36
  3   'l'    ord('l') = 108      108 XOR 77 = 33     →  byte[3]  = 33
  4   'l'    ord('l') = 108      108 XOR 77 = 33     →  byte[4]  = 33
  5   's'    ord('s') = 115      115 XOR 77 = 62     →  byte[5]  = 62
  6   't'    ord('t') = 116      116 XOR 77 = 57     →  byte[6]  = 57
  7   'e'    ord('e') = 101      101 XOR 77 = 40     →  byte[7]  = 40
  8   'a'    ord('a') =  97       97 XOR 77 = 44     →  byte[8]  = 44
  9   'l'    ord('l') = 108      108 XOR 77 = 33     →  byte[9]  = 33
 10   't'    ord('t') = 116      116 XOR 77 = 57     →  byte[10] = 57
 11   'h'    ord('h') = 104      104 XOR 77 = 37     →  byte[11] = 37
 12   'e'    ord('e') = 101      101 XOR 77 = 40     →  byte[12] = 40
 13   'm'    ord('m') = 109      109 XOR 77 = 32     →  byte[13] = 32
 14   'o'    ord('o') = 111      111 XOR 77 = 34     →  byte[14] = 34
 15   'o'    ord('o') = 111      111 XOR 77 = 34     →  byte[15] = 34
 16   'n'    ord('n') = 110      110 XOR 77 = 35     →  byte[16] = 35
 17   '@'    ord('@') =  64       64 XOR 77 = 13     →  byte[17] = 13
 18   'g'    ord('g') = 103      103 XOR 77 = 42     →  byte[18] = 42
 19   'm'    ord('m') = 109      109 XOR 77 = 32     →  byte[19] = 32
 20   'a'    ord('a') =  97       97 XOR 77 = 44     →  byte[20] = 44
 21   'i'    ord('i') = 105      105 XOR 77 = 36     →  byte[21] = 36
 22   'l'    ord('l') = 108      108 XOR 77 = 33     →  byte[22] = 33
 23   '.'    ord('.') =  46       46 XOR 77 = 99     →  byte[23] = 99
 24   'c'    ord('c') =  99       99 XOR 77 = 46     →  byte[24] = 46
 25   'o'    ord('o') = 111      111 XOR 77 = 34     →  byte[25] = 34
 26   'm'    ord('m') = 109      109 XOR 77 = 32     →  byte[26] = 32

So:  character → Unicode number → XOR 77  gives the byte at that position.
Put all bytes in order: [36, 58, 36, 33, 33, 62, 57, 40, 44, 33, 57, 37, 40, 32, 34, 34, 35, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32].
```
GOAL -> the characters


STEP 
EMAIL
EMAIL

[36, 58, 36, 33, 33, 62, 57, 40, 44, 33, 57, 37, 40, 32, 34, 34, 35, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32]


XOR 


[123, 58, 3123136, 33, 3323213 62, 57, 40, 44, 33, 57, 37, 40, 32, 34, 34, 35, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32]

[35,44,47,36,33,13,44,36,63,62,61,44,46,40,96,36,35,57,40,33,33,36,42,40,35,46,40,99,46 (END GOAL)]





# Credit:
Tems ---- Coder Helper
Damon -- Decoder/Cryptographer Guy/ Consulting
Tems (MY FRIEND IN NORTHEASTER SENIOR YEAR - MAJOR - BIOINFORMATICS - BIOTECH --- email -- t.miyatov@gmail.com) --- with the help of my DECODER FRIEND (DAMON - EMAIL --- jelliot1231@gmail.com) --- THANG (CODER: thangle246@gmail.com) 

yayyyyyyy -- sending email at 8:22 pm but it was finished at 7:30pm and i was re-reading my email for an hour 
