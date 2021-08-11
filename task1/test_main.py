# Выполним проверку на соотвествие полченного файла output.txt требуемому output_expected.txt

import task1_for_OZON


def test_main():
    task1_for_OZON.main()
    with open("output.txt", 'r') as f:
        d = list(f.readlines())

    with open("output_expected.txt", 'r') as f:
        e = list(f.readlines())
    assert d == e
