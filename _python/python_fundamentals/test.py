from timeit import repeat


def beCheerful(name='', repeat=3):
    print(f"Good Morning {name}\n" * repeat)

beCheerful()
beCheerful("Chris")
beCheerful("Misty")
beCheerful(repeat=6)
beCheerful("Jiraiya", 5)
beCheerful(repeat=2, name="Freyja")

