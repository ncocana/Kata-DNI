import pytest
from src.dni import Dni


@pytest.mark.test_checkDniValid
def test_checkDniValid():

    assert Dni("49481746Y").checkDniValid() == True
    assert Dni("43235117Q").checkDniValid() == True
    assert Dni("45301872Z").checkDniValid() == True
    assert Dni("46389099P").checkDniValid() == True
    assert Dni("43205465B").checkDniValid() == True
    assert Dni("49481746342Y").checkDniValid() == False
    assert Dni("T43211434").checkDniValid() == False
    assert Dni("45608961").checkDniValid() == False
    assert Dni("-45608961").checkDniValid() == False
    assert Dni("AAAI").checkDniValid() == False
    assert Dni("456089IO").checkDniValid() == False
    assert Dni("45185088I").checkDniValid() == False
    assert Dni("45185088Ñ").checkDniValid() == False
    assert Dni("45185088O").checkDniValid() == False
    assert Dni("45185088U").checkDniValid() == False
    assert Dni("45321O").checkDniValid() == False
    assert Dni("asdw0").checkDniValid() == False
    assert Dni("43205465b").checkDniValid() == False
    assert Dni("").checkDniValid() == False
