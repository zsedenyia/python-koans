from sentinel import ____


# === Typ och immutabilitet ===


def test_tuple_type_is_tuple():
    """Vad är typen av (1, 2, 3)?"""
    assert type((1, 2, 3)) == tuple


def test_tuples_raise_typeerror_on_item_assignment():
    """Tupler är immutabla — du kan inte ändra ett element på plats.
    Vilken exception kastar t[0] = 5 när t = (1, 2)?"""
    import pytest
    t = (1, 2)
    with pytest.raises(TypeError):
        t[0] = 5


def test_single_element_tuple_needs_trailing_comma():
    """Det är kommatecknet som skapar en tupel — inte parentesen.
    Vad är typen av (42,)?"""
    assert type((42,)) == tuple


def test_parentheses_without_comma_is_not_a_tuple():
    """(42) är bara ett parentesuttryck, inte en tupel. Vad är typen av (42)?"""
    assert type((42)) == int


# === Uppackning och swap ===


def test_unpacking_binds_names_positionally():
    """Tupeluppackning binder namnen till elementen positionellt från vänster.
    Vad är värdet av a efter a, b = (10, 20)?"""
    a, b = (10, 20)
    assert a == 10


def test_pythonic_swap_without_temporary_variable():
    """Python evaluerar hela höger sida innan tilldelning sker.
    Vad är värdet av a efter a, b = b, a när a=1 och b=2?"""
    a, b = 1, 2
    a, b = b, a
    assert a == 2


# === Konkatenering, längd och hashbarhet ===


def test_tuples_support_concatenation():
    """+ konkatenerar tupler till en ny tupel.
    Vad returnerar (1, 2) + (3, 4)?"""
    assert (1, 2) + (3, 4) == (1, 2, 3, 4)


def test_len_works_on_tuples():
    """len() fungerar på alla sekvenser. Vad returnerar len((1, 2, 3))?"""
    assert len((1, 2, 3)) == 3


def test_tuple_with_immutable_elements_can_be_dict_key():
    """Tupler med immutabla element är hashbara och kan användas som dict-nycklar.
    Vad returnerar {(1, 2): "pos"}[(1, 2)]?"""
    assert {(1, 2): "pos"}[(1, 2)] == "pos"
