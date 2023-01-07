import pytest
from src.assignmentTable import AssignmentTable

@pytest.fixture
def testTable():

    table = AssignmentTable()

    return table

@pytest.mark.test_getLenghtTable
def test_getLenghtTable(testTable):

    assert testTable.getLenghtTable() == 23

@pytest.mark.test_getPositionLetter
def test_getPositionLetter(testTable):

    assert testTable.getPositionLetter(21) == "K"
    assert testTable.getPositionLetter(0) == "T"
    assert testTable.getPositionLetter(13) == "J"
    assert testTable.getPositionLetter(5) == "M"
    assert testTable.getPositionLetter(22) == "E"
    assert testTable.getPositionLetter(19) == "L"
    assert testTable.getPositionLetter(23) == "This letter is not in use."
    assert testTable.getPositionLetter(50) == "This letter is not in use."

@pytest.mark.test_getLetter
def test_getLetter(testTable):

    assert testTable.calculateLetter(43235117) == "Q"
    assert testTable.calculateLetter(45301872) == "Z"
    assert testTable.calculateLetter(46389099) == "P"
    assert testTable.calculateLetter(43205465) == "B"
    assert testTable.calculateLetter(43211434) == "T"
    assert testTable.calculateLetter(41573239) == "A"

@pytest.mark.test_getTableContent
def test_getTableContent(testTable):

    assert "O" not in testTable.getTableContent()
    assert "I" not in testTable.getTableContent()
    assert "U" not in testTable.getTableContent()
    assert "Ñ" not in testTable.getTableContent()

    for letter in testTable.getTableContent():
        assert letter in testTable.getTableContent()
