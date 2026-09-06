from sentinel import ____


# === Uppslagning och get() ===


def test_missing_key_raises_keyerror():
    """Att läsa en nyckel som inte finns kastar ett undantag.
    Vilken exception kastar d["b"] när "b" inte finns i d?"""
    import pytest
    d = {"a": 1}
    with pytest.raises(KeyError):
        d["b"]


def test_get_returns_none_for_missing_key():
    """get() kastar ingen exception för saknade nycklar.
    Vad returnerar d.get("b") när "b" saknas?"""
    d = {"a": 1}
    assert d.get("b") == None


def test_get_with_default_returns_default_for_missing_key():
    """get(nyckel, standard) returnerar standardvärdet om nyckeln saknas.
    Vad returnerar d.get("b", 0) när "b" saknas?"""
    d = {"a": 1}
    assert d.get("b", 0) == 0


# === Vyer och iteration ===


def test_keys_returns_a_dict_keys_view_type():
    """d.keys() returnerar en vytyp, inte en lista.
    Vad är typen av d.keys()?"""
    d = {"a": 1}
    assert type(d.keys()) == type({}.keys())


def test_items_elements_are_tuples():
    """d.items() ger nyckel-värde-par. Vad är typen på varje par?"""
    d = {"a": 1}
    pairs = list(d.items())
    assert type(pairs[0]) == tuple


def test_iterating_dict_yields_keys():
    """Iteration över en dict ger nycklarna — inte paren och inte värdena.
    Vad innehåller list(d) för d = {"a": 1, "b": 2}?"""
    d = {"a": 1, "b": 2}
    assert list(d) == ["a", "b"]


# === Mutation och merge ===


def test_updating_key_does_not_increase_len():
    """Att sätta ett nytt värde på en befintlig nyckel skapar inte en ny post.
    Vad är len(d) efter d = {"a": 1}; d["a"] = 2?"""
    d = {"a": 1}
    d["a"] = 2
    assert len(d) == 1


def test_pop_returns_value_of_removed_key():
    """pop(nyckel) tar bort nyckeln och returnerar dess värde.
    Vad returnerar d.pop("a") när d = {"a": 99}?"""
    d = {"a": 99}
    assert d.pop("a") == 99


def test_pipe_merges_dicts_into_new_dict():
    """| skapar en ny dict med alla par från båda dictarna (Python 3.9+).
    Vilka nycklar innehåller {"a": 1} | {"b": 2}?"""
    result = {"a": 1} | {"b": 2}
    assert set(result.keys()) == {"a", "b"}


# === Dict comprehension ===


def test_dict_comprehension_transforms_values():
    """Dict comprehension bygger en ny dict med transformerade värden.
    Vad är result["a"] efter {k: v*2 for k, v in {"a": 1, "b": 2}.items()}?"""
    result = {k: v * 2 for k, v in {"a": 1, "b": 2}.items()}
    assert result["a"] == 2
