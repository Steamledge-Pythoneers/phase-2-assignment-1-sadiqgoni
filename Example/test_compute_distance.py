from compute_distance import distance_to_destination

def test_distance_to_destination_4():
    assert(distance_to_destination(22, 26) == 14)

def test_distance_to_destination_0():
    assert(distance_to_destination(253, 253) == 0)

def test_distance_to_destination_0_negative():
    assert(distance_to_destination(83, 64) == 0)
    
def test_distance_to_destination_1():
    assert(distance_to_destination(9, 10) == 1)

def test_distance_to_destination_100():
    assert(distance_to_destination(100, 200) == 100)
