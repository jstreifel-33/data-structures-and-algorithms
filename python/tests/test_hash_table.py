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
