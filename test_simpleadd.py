""" Example to test the simple add function"""


from hypothesis import given
import hypothesis.strategies as st
import util
import simpleadd


# TODO:
# get_input_type
# read_type
# create_st
# use * to pass in the given decorator
# specify how many parameters needed in the test case like below

type_add_output = util.get_input_type(
    function="add",
    module="simpleadd",
)
list_type = util.read_type(type_add_output)
func_st = util.create_st(list_type)


@given(*func_st)
def test_add(a, b):
    """ use tool to test add function """
    assert simpleadd.add(a, b) == a + b
