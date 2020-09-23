Before you begin, make sure to run this command in your terminal to install pytest:
```
pip install -U pytest
```
Then, ensure you are in Example/ folder and run pytest; to run pytest, just enter:
```
pytest
```

Right now, not all of the tests pass. It should give an output like this:
```
test_compute_distance.py F....                                           [100%]
```
this means test_compute_distance.py file has five(5) test cases denoted by:
```
F....
```

the first test failed, denoted by an 'F':
```
F
```

while the rest four tests passed, denoted by four '.':
```
....
```

study and understand the code in compute_distance.py

study and understand the code in test_compute_distance.py

Fix the test_compute_distance.py functions to pass all its tests! Once all your tests pass, Navigate to Exercise folder for your exercise!