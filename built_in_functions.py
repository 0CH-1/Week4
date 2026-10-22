print("Program Started! ")

print("Please enter a standard character: ")
character =input()

if len(character)==1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("A single character was expected.")
print("Program Ended!")

#New code
print("Program Started!")

print("Please enter an ASCII code: ")
code=int(input())

if code>=32 and code<=126:
    print(f"The character presented by the ASCII code {code} is {chr(code)}")
else:
    print("The character cannot be displayed.")

print("Program Ended!")