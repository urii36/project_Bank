from src.utils import select_data, format_data, sort_data


def test_select_data(sample_data):
    assert select_data(sample_data) == [sample_data[2]]


def test_sort_data(sample_data):
    assert sort_data(sample_data) == sample_data


def test_format_data(sample_data):
    formatted_data = format_data(sample_data)
    expected_output = [
        "\n03.07.2019 Перевод организации\n"
        "Visa Platinum 7000 79** **** 6361 -> Счет **9589\n"
        "82771.72 руб\n",
        "\n03.07.2018 Перевод организации\n"
        "Visa Platinum 8900 79** **** 6361 -> Счет **9589\n"
        "82771.72 usd\n",
        "\n30.06.2018 Перевод организации\n"
        "Счет **6702\n"
        "9824.07 USD\n"
    ]
    assert formatted_data == expected_output
