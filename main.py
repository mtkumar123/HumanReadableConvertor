import argparse
import re
from typing import Optional

word_mapping = {"S": "Soft", "T": "Tough"}


def validate_string(arg: str) -> str:
    """Helper function to validate input string

    :param str arg: input string
    :raises argparse.ArgumentTypeError
    :return str: returns input string after validation
    """
    if not re.match(r"^[ST]*$", arg):
        raise argparse.ArgumentTypeError("Text should contain only S and T.")
    return arg


def recursive_human_readable_convertor(
    text: str,
    iter: int,
    pos: int = 0,
    result: str = "",
) -> str:
    """Recursive function to convert given text
    into human readable form based on number of
    iterations required.

    :param str text: pattern of S and T string
    :param int iter: number of iterations
    :param int pos: current position in text, defaults to 0
    :param str result: human readable pattern result, defaults to ""
    :return str: human readable pattern result
    """
    if iter < 1:
        return result
    if iter == 1:
        if result:
            result += f" and {word_mapping[text[pos]]}."
        else:
            result = f"{word_mapping[text[pos]]}."
        return result
    result += (
        f", {word_mapping[text[pos]]}" if result else word_mapping[text[pos]]
    )
    pos = pos + 1 if (pos + 1) < len(text) else 0
    iter -= 1
    return recursive_human_readable_convertor(text, iter, pos, result)


def convertor(argv: Optional[list[str]] = None) -> list[str]:
    """Driver function to convert input string
    to human readable form.

    :param Optional[list[str]] argv: list of input strings, defaults to None
    :return list[str]: list of human readable strings
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "text",
        type=validate_string,
        help="Enter string of S and T to format output",
    )
    parser.add_argument(
        "numbers",
        type=int,
        nargs="+",
        help="Enter a sequence of integers separated by a space",
    )
    args = parser.parse_args(argv)
    result: list[str] = []
    for number in args.numbers:
        result.append(recursive_human_readable_convertor(args.text, number))
    return result


if __name__ == "__main__":
    results = convertor()
    for result in results:
        print(result)
