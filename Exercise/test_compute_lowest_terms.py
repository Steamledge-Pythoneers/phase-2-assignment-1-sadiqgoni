from compute_lowest_terms import lowest_terms

def test_lowest_terms_rational():
	assert(lowest_terms("20/10") == "2/1")

def test_lowest_terms_irrational():
	assert(lowest_terms("16/28") == "4/7")

def test_lowest_terms_rational_negative():
	assert(lowest_terms("-50/25") == "-2/1")

def test_lowest_terms_irrational_negative_1():
	assert(lowest_terms("20/-60") == "-1/3")
    
def test_lowest_terms_irrational_negative_2():
	assert(lowest_terms("-300/165") == "-12/7")

def test_lowest_terms_positive():
	assert(lowest_terms("-12/-26") == "6/13")

def test_lowest_terms_ZeroDivisionError():
	assert(lowest_terms("90/0") == "Undefined")

def test_lowest_terms_0():
	assert(lowest_terms("0/12") == "0")
