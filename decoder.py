INPUT = [35,44,47,36,33,13,44,36,63,62,61,44,46,40,96,36,35,57,40,33,33,36,42,40,35,46,40,99,46,34,32]
print(f"testing input: {INPUT}")


character = chr(35)

print(f"testing character - test subject 35: {character}")


first_number = 35
key = 77
print(f"key----{key}")


first_test = 35 ^ 77
print(f"testing first test - test subject 35 ^ 77 : {first_test}")

first_test_result =35 ^ 77


print(f"first test result- {first_test_result}")

second_test = 44 ^ 77

print(f"print second test: test subject 44 ^ 77: {second_test}")

character = ""
print(f"character to start: {character}")
for number in INPUT:
    character+=chr(number ^ 77)
    print(f"number is: {number} - number xor: {number ^ 77} -- answer is: {chr(number ^ 77)} -- character = {character}")
print(character)


def thang_function(input_list_of_number:list[int]) -> str:# unit_test
    result = ""
    for number in input_list_of_number:
        result+=chr(number ^ 77)
    return result

expected = ["iwillstealthemoon@gmail.com","spaceiscool@gmail.com","airspaceintelligent@gmail.com"]
input = [[36, 58, 36, 33, 33, 62, 57, 40, 44, 33, 57, 37, 40, 32, 34, 34, 35, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32],[62, 61, 44, 46, 40, 36, 62, 46, 34, 34, 33, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32],[44, 36, 63, 62, 61, 44, 46, 40, 36, 35, 57, 40, 33, 33, 36, 42, 40, 35, 57, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32]
]
unit_test_dict= {
    "expected": ["iwillstealthemoon@gmail.com","spaceiscool@gmail.com","airspaceintelligent@gmail.com"],
    "input" :[[36, 58, 36, 33, 33, 62, 57, 40, 44, 33, 57, 37, 40, 32, 34, 34, 35, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32],[62, 61, 44, 46, 40, 36, 62, 46, 34, 34, 33, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32],[44, 36, 63, 62, 61, 44, 46, 40, 36, 35, 57, 40, 33, 33, 36, 42, 40, 35, 57, 13, 42, 32, 44, 36, 33, 99, 46, 34, 32]],
}

print(f"unit test -- expected : {unit_test_dict["expected"]}")
print(f"unit test -- input : {unit_test_dict["input"]}")

test_1 = unit_test_dict["expected"]
print(f"test---{len(unit_test_dict["expected"])}")
for test_number in range(len(unit_test_dict["expected"])):
    print(f"---------------------BEGIN TEST {test_number}-----------------------------")
    thang_result = thang_function(unit_test_dict["input"][test_number])
    if thang_result == unit_test_dict["expected"][test_number]:
        print(f"input: {unit_test_dict["input"][test_number]}-- expected: {unit_test_dict["expected"][test_number]} --- thang result: {thang_result} -- test passes")
    print("--------------------------END TEST -------------------------")
thang_function( [35,44,47,36,33,13,44,36,63,62,61,44,46,40,96,36,35,57,40,33,33,36,42,40,35,46,40,99,46,34,32])

