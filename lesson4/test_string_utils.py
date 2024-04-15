import pytest

from string_utils import StringUtils

stringUtils = StringUtils()

# Checking: the CAPITAL LETTER
# Positive checks
@pytest.mark.parametrize('string_, res_', [("moskow", "Moskow"), ("a", "A"),
                        ("Cool", "Cool"), ("москва", "Москва"),
                        pytest.param(123, 123, marks=pytest.mark.xfail(strict=True)),
                        pytest.param([], [], marks=pytest.mark.xfail(strict=True)),
                        pytest.param(None, None, marks=pytest.mark.xfail(strict=True))])
def test_capitalize_poz(string_, res_):
    res = stringUtils.capitilize(string_)
    assert res == res_

# Negative checks
@pytest.mark.parametrize('string_, res_', [("--ool", "--ool"), ("!!!", "!!!")])
def test_capitalize_neg(string_, res_):
    res = stringUtils.capitilize(string_)
    assert res == res_

# Checking: A SPACE AT THE BEGINNING OF A WORD
# Positive checks    
@pytest.mark.parametrize('string_, res_', [("Street", "Street"),
                        (" Street", "Street"), ("    Street", "Street"),
                        (" 123", "123"), (" ", ""), ("", ""),
                        pytest.param((  123), (123), marks=pytest.mark.xfail(strict=True)),
                        pytest.param([  ], [], marks=pytest.mark.xfail(strict=True)),
                        pytest.param((  None), (None), marks=pytest.mark.xfail(strict=True))]) 
def test_trim_poz(string_, res_):
    res = stringUtils.trim(string_)
    assert res == res_

# Negative checks    
@pytest.mark.parametrize('string_, res_', [("   --ool", "--ool"), ("   !!!", "!!!")]) 
def test_trim_neg(string_, res_):
    res = stringUtils.trim(string_)
    assert res == res_
       
# Checking: the DELIMITER
# Positive checks default DELIMITER       
@pytest.mark.parametrize('string_, res_', [("s,t,o,r,y", ["s","t","o","r","y"]),
                        ("м,а,й", ["м","а","й"]), ("st,or,y", ["st","or","y"]),
                        pytest.param((), [], marks=pytest.mark.xfail(strict=True)),
                        pytest.param(None, [None], marks=pytest.mark.xfail(strict=True))])
def test_default_list_pos(string_, res_):
    res = stringUtils.to_list(string_)
    assert res == res_

# Negative checks default DELIMITER    
@pytest.mark.parametrize('string_, res_', [("-,-,o,?,l", ["-","-","o","?","l"]),
                        ("!,!,!", ["!","!","!"])])      
def test_default_list_neg(string_, res_):
    res = stringUtils.to_list(string_)
    assert res == res_

# Positive checks DELIMITER  
@pytest.mark.parametrize('string_, del_, res_', [("г:о:д", ":", ["г","о","д"]),
                        ("y-e-s", "-", ["y","e","s"]),
                        pytest.param(None, ":", [None], marks=pytest.mark.xfail(strict=True))])                                       
def test_delimiter_list_pos(string_, del_, res_):
    res = stringUtils.to_list(string_, del_)
    assert res == res_         

# Negative checks DELIMITER    
@pytest.mark.parametrize('string_, del_, res_', [("N:*:*:e", ":", ["N","*","*","e"]),
                        ("!-!-!", "-", ["!","!","!"])])
def test_delimiter_list_neg(string_, del_, res_):
    res = stringUtils.to_list(string_, del_)
    assert res == res_

# Checking: THE DESIRED SYMBOL
# Positive checks        
@pytest.mark.parametrize('string_, symbol_, res_', [("City", "C", True), ("Moskow", "w", True),
                        ("Street", "K", False), ("_Street", "_", True), ("Street", "f", False),
                        pytest.param("Street", "f", True, marks=pytest.mark.xfail(strict=True)),
                        pytest.param("Москва", "с", False, marks=pytest.mark.xfail(strict=True)),
                        pytest.param(468, 8, True, marks=pytest.mark.xfail(strict=True))])                       
def test_contains_poz(string_, symbol_, res_):
        res = stringUtils.contains(string_, symbol_)
        assert res == res_ 

# Negative checks       
@pytest.mark.parametrize('string_, symbol_, res_', [("A$b8f", "f", True),
                        ("k6-s", "с", False)]) 
def test_contains_neg(string_, symbol_, res_):
        res = stringUtils.contains(string_, symbol_)             
        assert res == res_                   
            
# Checking: DELETING A SYMBOL
# Positive checks
@pytest.mark.parametrize('string_, symbol_, res_', [("City", "C", "ity"),
                        ( "Moskow", "w", "Mosko"), ("Москва", "к", "Мосва"),
                        ("_Street", "_", "Street"), ("Street", "tr", "Seet"),
                        pytest.param("  ", " ", " ", marks=pytest.mark.xfail(strict=True)),
                        pytest.param(None, None, None, marks=pytest.mark.xfail(strict=True)),
                        pytest.param(24682, 6, 2482, marks=pytest.mark.xfail(strict=True))])
def test_delete_symbol_poz(string_, symbol_, res_):
        res = stringUtils.delete_symbol(string_, symbol_)             
        assert res == res_

# Negative checks
@pytest.mark.parametrize('string_, symbol_, res_', [([], 1, [])])
def test_delete_symbol_neg(string_, symbol_, res_):
        res = stringUtils.delete_symbol(string_, symbol_)             
        assert res == res_
                
# Checking: THE SYMBOL AT THE BEGINNING OF THE LINE
# Positive checks       
@pytest.mark.parametrize('string_, symbol_, res_', [("City", "C", True),
                        ("Moskow", "M", True), ("Street", "K", False),
                        pytest.param("City", "y", True, marks=pytest.mark.xfail(strict=True)),
                        pytest.param("Москва", "М", False, marks=pytest.mark.xfail(strict=True)),
                        pytest.param(468, 8, True, marks=pytest.mark.xfail(strict=True))])
def test_starts_with_poz(string_, symbol_, res_):
        res = stringUtils.starts_with(string_, symbol_)
        assert res == res_

# Negative checks
@pytest.mark.parametrize('string_, symbol_, res_', [("_Street", "_", True)])
def test_starts_with_neg(string_, symbol_, res_):
        res = stringUtils.starts_with(string_, symbol_)              
        assert res == res_

# Checking: THE SYMBOL AT THE END OF THE LINE
# Positive checks       
@pytest.mark.parametrize('string_, symbol_, res_', [("City", "y", True),
                        ( "Москва", "а", True), ("Street", "K", False),
                        ("Street_", "_", True), ("Street", "f", False),
                        pytest.param("Street", "f", True, marks=pytest.mark.xfail(strict=True)),
                        pytest.param("Москва", "а", False, marks=pytest.mark.xfail(strict=True)),
                        pytest.param(468, 8, True, marks=pytest.mark.xfail(strict=True))])
def test_end_with_poz(string_, symbol_, res_):
        res = stringUtils.end_with(string_, symbol_)
        assert res == res_ 

# Negative checks
@pytest.mark.parametrize('string_, symbol_, res_', [("!-?", "?", True), (" ", "", True)]) 
def test_end_with_neg(string_, symbol_, res_):
        res = stringUtils.end_with(string_, symbol_)              
        assert res == res_ 

# Checking: AN EMPTY LINE
# Positive checks               
@pytest.mark.parametrize('string_, res_', [(" ", True), ("", True), ("Street", False),
                        pytest.param("123", True, marks=pytest.mark.xfail(strict=True)),
                        pytest.param(" ", False, marks=pytest.mark.xfail(strict=True)),
                        pytest.param(468, True, marks=pytest.mark.xfail(strict=True))]) 
def test_empty_poz(string_, res_):
        res = stringUtils.is_empty(string_)
        assert res == res_

# Negative checks 
@pytest.mark.parametrize('string_, res_', [("---", False), ("!?<>", False)])
def test_empty_neg(string_, res_):
        res = stringUtils.is_empty(string_)
        assert res == res_   

# Checking: A STRING WITH THE SPECIFIED JOINER
# Positive checks default JOINER            
@pytest.mark.parametrize('lst_, res_', [([1,2,3], "1,2,3"),
                        (["try","you"], "try,you"), (["t","r","y"], "t,r,y"),
                        pytest.param([], (), marks=pytest.mark.xfail(strict=True)),
                        pytest.param([None], None, marks=pytest.mark.xfail(strict=True))])
def test_default_list_string_poz(lst_, res_):
        res = stringUtils.list_to_string(lst_)
        assert res == res_  

# Negative checks default JOINER               
@pytest.mark.parametrize('lst_, res_', [(["<>","?!"], "<>,?!"), (["k","*","!"], "k,*,!")]) 
def test_default_list_string_neg(lst_, res_):
        res = stringUtils.list_to_string(lst_)             
        assert res == res_ 

# Positive checks JOINER             
@pytest.mark.parametrize('lst_, del_, res_', [(["try","you"], "-", "try-you"),
                        (["p","i","e"], ":", "p:i:e"),
                        pytest.param([], "",(), marks=pytest.mark.xfail(strict=True)),
                        pytest.param([None],":", None, marks=pytest.mark.xfail(strict=True))])
def test_joiner_list_string_poz(lst_, del_, res_):
        res = stringUtils.list_to_string(lst_, del_)             
        assert res == res_ 

# Negative checks JOINER              
@pytest.mark.parametrize('lst_, del_, res_', [(["<>","?!"], "-", "<>-?!"),
                        (["k","*","!"], ":", "k:*:!")])
def test_joiner_list_string_neg(lst_, del_, res_):
        res = stringUtils.list_to_string(lst_, del_)             
        assert res == res_                                          