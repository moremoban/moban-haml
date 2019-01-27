import os

from nose.tools import eq_
from moban.plugins import ENGINES, BaseEngine
from moban_haml.engine import EngineHaml


def test_haml_engine_type():
    engine = ENGINES.get_engine("haml", [], "")
    assert engine.engine_cls == EngineHaml
    pass


def test_haml_file_tests():
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "haml_tests")
    engine = BaseEngine([path], path, EngineHaml)
    engine.render_to_file("file_tests.haml", "file_tests.json", output)
    with open(output, "r") as output_file:
        expected_path = os.path.join("tests", "fixtures", "haml_tests",
                                     "expected_output.txt")
        with open(expected_path) as expected_file:
            expected = expected_file.read()
            content = output_file.read()
            eq_(content, expected)
    os.unlink(output)


def test_haml_string_template():
    string_template = "{{ content }}"
    output = "test.txt"
    path = os.path.join("tests", "fixtures", "haml_tests")
    engine = BaseEngine([path], path, EngineHaml)
    engine.render_string_to_file(string_template, "file_tests.json", output)
    with open(output, "r") as output_file:
        expected = "Hello World!"
        content = output_file.read()
        eq_(content, expected)
    os.unlink(output)
