""" Example to test the simple add function"""


from hypothesis import given
import hypothesis.strategies as st
from src import util
from termfrequency import simpleadd


table = "monkeytype_call_traces"
dbFilename = "example/tests/monkeytype.sqlite3"

# TODO:
# read_type
# create_st
# use * to pass in the given decorator
# specify how many parameters needed in the test case like below

type_add_output = util.get_output_type(
    function="add",
    module="termfrequency.simpleadd",
)
list_type = util.read_type(type_add_output)
func_st = util.create_st(list_type)


@given(*func_st)
def test_add(a, b):
    """ use tool to test add function """
    assert simpleadd.add(a, b) == a + b
