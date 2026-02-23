
# List of encoded numbers 
data = [35,44,47,36,33,13,44,36,63,62,61,44,46,40,96,36,35,57,40,33,33,36,42,40,35,46,40,99,46,34,32]

# XOR key (from squawk 7700 -> trim zeros -> 77)
key = 77

# Empty string where it decodes message letter by letter
decoded = ""

# Loop through each encoded number
for n in data:

    # XOR the encoded number with the key to get decoded ASCII number
    x = n ^ key

    # Print step-by-step decoding:
    # original_number ^ key = decoded_number -> decoded_character (aka just a formula that tem used  for each number to decode)
    print(f"{n} ^ {key} = {x} -> {chr(x)}")

    # Convert decoded number to charachter and finish the loop
    decoded += chr(x)

# After loop finishes, print the fully decoded message
print("EMAIL:", decoded)

