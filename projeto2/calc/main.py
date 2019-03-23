from converter import Converter


def main():
    text = "(A.B*(A|B)+)*"
    converter = Converter()
    print(converter.converterPreFixa(text))


if __name__ == '__main__':
    main()
