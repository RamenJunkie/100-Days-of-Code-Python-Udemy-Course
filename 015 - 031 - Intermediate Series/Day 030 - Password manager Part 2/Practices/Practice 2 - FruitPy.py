
fruits = ["Apple", "Pear", "Orange"]

### Original Code
# TODO: Catch the exception and make sure the code runs without crashing.
#def make_pie(index):
#    fruit = fruits[index]
#    print(fruit + " pie")

## Fixed Code
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        fruit = "Fruit"
    else:
        pass
    finally:
        print(fruit + " pie")


make_pie(4)