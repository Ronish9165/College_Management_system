from rough import *
def test_login():
    db = show_login_result('ankit','9841252055')
    assert db == 'Pass'

def test_log():
    db = show_login_result('ankit','9841252055')
    assert db == 'Pass'

def test_logann():
    db = show_login_result('ankit','9841252055')
    assert db == 'Pass'

def test_gann():
    db = show_login_result('ankitdd','984125205gfhgh5')
    assert db == 'Pass'

def test_aagann():
    db = show_login_result('ankitdd','984125205gfhgh5')
    assert db == 'Pass'