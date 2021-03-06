# And now for lists!

print("""Lists are ordered collections, defined using square brackets. []
        Within a list, elements are separated by commas.
        Elements may be accessed using their index (position), which begins at 0, not 1, as show below.
        list_name[index] i.e. planets[0]
        If you're not sure how many elements exist in a list you can use -1 to return the last item,
        -2 to return the second to last item, and so on.

        """)

local_solar_sys = ['mercuy', 'venus', 'earth', 'mars','jupiter', 'saturn', 'uranus', 'neptune']
inner_planets = ['Mercury', 'Venus', 'Earth', 'Mars']
gas_giants = ['Jupiter', 'Saturn']
ice_giants = ['Uranus', 'Neptune']
drawf_planets = ['Pluto']

print("Here's a list: ")
print(inner_planets)
print("This is index 0: ")
print(inner_planets[0])
print("This is index -1: ")
print(inner_planets[-1])

print("You can also modify elements in a list like so: list[index] = 'new_item'")

rosie_toys = ['string', 'turtle', 'fuzzy_ball']

print("\nHere's our list.")
print(rosie_toys)

rosie_toys[1] = 'crumpled_paper'

print("\nHere we've changed 'turtle' to 'crumpled_paper' at  index 1: ")
print(rosie_toys)

print("\nTurns out Rosie really like her turtle toy, so let's add it back in using the insert() method like so: \tlist.insert(index, 'element').")

rosie_toys.insert(2, 'turtle')

print(rosie_toys)

print("""\nWe can use also the append() method to add to the end of the list without affecting any other elements.
       \t list.append('new_element')""")

rosie_toys.append('feathers')

print("Here's our appended list: ", rosie_toys)

print("""\nWhat if little Rosie gets tired of one of her toys and we want to remove it from the list?
        That's as simple as the del() statement:
        del list[index]""")

del rosie_toys[-2]

print(rosie_toys)

print("\nCool, now we want to use an item after removing it, and for that we turn to the pop() method: list.pop().")

print("Here we'll use pop() and assign the popped value to a new variable, 'rosie_fav'.")

rosie_fav = rosie_toys.pop()

print(rosie_fav)

print("\nGreat, it automatically popped the last element. We can specify a specific element by adding its index inside the parenthesis.")

rosie_fav = rosie_toys.pop(0)

print("rosie_fav = ", rosie_fav)
print("rosie_toys = ", rosie_toys)

print("""\nAren't lists fun?
        We want to remove an item from our list, but we don't know its index.
        As luck would have it, we can remove it knowing just the value via the remove() method.
        \t\t\tlist.remove('item')
        The remove() method only deletes the first occurance of an item. Let's add a second turtle to demonstrate this.
        """)

rosie_toys.insert(0, 'turtle')

print("rosie_toys = ", rosie_toys)

print("Now let's try the remove method: ")
rosie_toys.remove('turtle')

print("rosie_toys = ", rosie_toys)

# ORGANIZING LISTS

print("\n\n\n In this section, we'll work on organizing lists using the sort() method, sorted() function, reverse() method and len() function.")
print("\nLet's kick things off with sorted(), which will temporarily change a list's order to be alphabetical.")
print("""sorted() is a little different in that it is a function, not a method.
        Rather than applying it to a list object with the dot notation, we'll feed the list as an argument to the function, like so:
        \t\t\tsorted(list_name)""")

print("First we'll print our list `local_solar_sys`: ", local_solar_sys)

print("\nNow we'll print it sorted: ", sorted(local_solar_sys))

print("\nNow let's print the list our to see if the change was permenant: ", local_solar_sys)

print("\nLet's try using the sort() and reverse() methods now.\n")

print("First reverse(), which is permenant.\n")

local_solar_sys.reverse()

print(local_solar_sys)

print("\nIf you want to sort in reverse alphabetical order, just pass the argument `reverse=True` to the sort() method.\n")

local_solar_sys.sort(reverse=True)

print(local_solar_sys)

# Why does this return None instead of the same as the above? print(local_solar_sys.reverse())

print("\nTo find the length of the list, simple use the len() function like so: ")

print("\n\t\tlen(local_solar_sys) = ", len(local_solar_sys))

print("Python counts item in a list starting at one, unlike it's index.")
