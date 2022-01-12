from hash_table.hash_table import HashTable

def test_hash_table_add():
    ht = HashTable()
    ht.add("cat", "meow")

    hash = ht.hash("cat")

    assert ht.table[hash].head.value == ("cat", "meow")


def test_hash_table_get():
    ht = HashTable()
    ht.add("cat", "meow")

    assert ht.get("cat") == "meow"


def test_get_key_not_in_table():
    ht = HashTable()
    ht.add("cat", "meow")

    assert ht.get("dog") is None


def test_key_collision():
    ht = HashTable()

    ht.add("cat", "meow")
    ht.add("tac", "woem")

    #sanity check
    assert ht.hash("cat") == ht.hash("tac")

    #actual test
    assert ht.get("cat") == "meow"
    assert ht.get("tac") == "woem"


def test_retrieve_from_collision():
    ht = HashTable()

    ht.add("dingo", "dog thing")
    ht.add("doing", "things and stuff")
    ht.add("gindo", "made up word")

    assert ht.get("dingo") == "dog thing"
    assert ht.get("doing") == "things and stuff"
    assert ht.get("gindo") == "made up word"


def test_hash_ranges():
    ht = HashTable()

    #test a bunch of hashes
    assert 0 <= ht.hash("kittycat") <= 1023
    assert 0 <= ht.hash("Charles Darwin") <= 1023
    assert 0 <= ht.hash("Empire State Building") <= 1023
    assert 0 <= ht.hash("The Literal Entire City of Albuquerque") <= 1023
    assert 0 <= ht.hash("A really long string that I need for even more testing to make sure the number definitely rolls over instead of going out of range") <= 1023
