#misol linki https://www.codewars.com/kata/5b011461de4c7f8d78000052/train/python


def bear_fur(colors):
    offspring_colors = {
        ('black', 'black'): 'black',
        ('brown', 'brown'): 'brown',
        ('white', 'white'): 'white',
        ('black', 'brown'): 'dark brown',
        ('brown', 'black'): 'dark brown',
        ('black', 'white'): 'grey',
        ('white', 'black'): 'grey',
        ('brown', 'white'): 'light brown',
        ('white', 'brown'): 'light brown'
    }

    if tuple(colors) in offspring_colors:
        return offspring_colors[tuple(colors)]
    else:
        return 'unknown'


print(bear_fur(['black', 'black']))
print(bear_fur(['brown', 'brown']))
print(bear_fur(['white', 'white']))
print(bear_fur(['black', 'brown']))
print(bear_fur(['black', 'white']))
print(bear_fur(['brown', 'white']))
print(bear_fur(['yellow', 'magenta']))
