from converter import Converter


def main():
    text = "A.B*(A+B)"
    converter = Converter()
    print(converter.converterPosFixa(text))


if __name__ == '__main__':
    main()
