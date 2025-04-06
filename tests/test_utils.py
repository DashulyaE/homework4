import json
import os

from src.utils import read_json, create_category_json


def test_read_valid_json():
    """Тест с корректным JSON файлом."""

    test_json_valid = "test_valid.json"
    with open(test_json_valid, "w", encoding="UTF-8") as f:
        json.dump({"categories": ["cat1", "cat2"], "products": ["prod1", "prod2"]}, f)
    result = read_json(test_json_valid)
    expected = {"categories": ["cat1", "cat2"], "products": ["prod1", "prod2"]}
    assert result == expected
    os.remove(test_json_valid)


def test_empty_input():
    assert create_category_json([]) == []
