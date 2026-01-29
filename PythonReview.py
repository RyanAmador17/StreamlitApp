# Start here
print("This is the first programming app for CIS 3590")

message = "Welcome to FIU"

print(len(message))
print(message[0])
print(type(message))
print(type(3))
print(type("3"))
print(3*3)
print(3*"3")
print(len("Joshua")==4)

a = 10
b = 5

print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division

print(10/2)

print(a//b) # floor division
print(a**b) # a to the power of b
print(a%b) # modulo

pokemon = ["Bulbasaur","Charmander","Squirtle"]

print(pokemon[0])
print(pokemon[-1]) # starts at the end of the list
pokemon.append("Pikachu")
print(pokemon)
pokemon.extend(["Eevee","Chikorita","Cyndaquil","Totodile"]) # adds several values
print(pokemon)
pokemon.insert(len(pokemon),"Treecko")
print(pokemon)
pokemon[2] = "Torchic"
print(pokemon)
print(pokemon[3:5]) # accessing Pokémon is positions 3 and 4
print(pokemon[5:]) # prints Pokémon from 5 to the end
print(pokemon[:3]) # prints Pokémon from the beginning to 2
print(pokemon[:]) # prints the entire list but creates a copy
pokemon.remove("Eevee")
print(pokemon)
print(pokemon.index("Pikachu"))

x = pokemon.pop(6)

print(pokemon)
print(x)
print(len(pokemon))
print(type(pokemon))
pokemon.sort()
print(pokemon)
pokemon.sort(reverse=True)
print(pokemon)

for i in pokemon:
    print(i.title())
    #print("FIU")
print("FIU")

water_data = {
    "temperature":[78, 89, 92],
    "pH":[6.5, 6.7, 6.3],
    "oxygen":[7.2, 5.6, 3.5]
} # dictionary
print(water_data["oxygen"])
print(water_data.keys())
print(water_data.values())

import pandas as pd

df = pd.DataFrame(water_data) # converts a dictionary into a data frame
print(df)