import collections

FuncList = collections.namedtuple("FuncList", ['head', 'tail'])

def item_count(funclist):
    pass


def convert_to_funclist(reglist):
    pass


def convert_to_reglist(funclist):
    pass


def find_first(funclist, value):
    """ @return the index of the first instance of the value in the list, or -1 if not found """ 
    pass


def find_last(funclist, value):
    """ @return the index of the last instance of the value in the list, or -1 if not found """ 
    pass


def check_if_sorted(funclist):
    """ @return True is the list is in sorted order, False otherwise """
    pass


def split(funclist, first_list_item_count):
    """ @return two lists, the first containing the specified count of items,
        the second containing the leftover items from the original (the rest).
        Either or both lists can be None if there aren't enough items
        if firstItemCount < 0, first list will be None
        if firtItemCount > item_count, second list will be None
    """
    pass


def merge(sortedList1, sortedList2):
    """ @return one, sorted list that contains all items from the two sorted lists given """
    pass


def merge_sort(funclist):
    """ hint: should not need to be complex, use item_count, split, and merge functions """
    pass
