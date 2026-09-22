from app import add, greet

def test_add():
    assert add(2, 2) == 4

def test_greet():
    assert greet("Anna") == "Hej, Anna!"
    