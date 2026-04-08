from streamlit.testing.v1 import AppTest


def test_basic_addition() -> None:
    at = AppTest.from_file("calculator/app.py", default_timeout=10)
    at.run()
    assert not at.exception


def test_expression_evaluation() -> None:
    at = AppTest.from_file("calculator/app.py", default_timeout=10)
    at.run()
    at.text_input[0].set_value("2 + 3").run()
    at.button[2].click().run()
    assert "5" in at.success[0].value


def test_division_by_zero_shows_error() -> None:
    at = AppTest.from_file("calculator/app.py", default_timeout=10)
    at.run()
    at.text_input[0].set_value("1 / 0").run()
    at.button[2].click().run()
    assert "Cannot divide by zero" in at.error[0].value
