import argparse
import logging
from aligner.justify_aligner import JustifyAligner
from filesystem.file_local import FileLocal

from formatter.formatter import Formatter
from wrapper.paragraph_wrapper import ParagraphWrapper

parser = argparse.ArgumentParser(description='Formatter for Strings, wrap, align and save texts.')
parser.add_argument('--limit', dest='limit', default=40, type=int, help="Limit of characters by line")
parser.add_argument('--path', dest='path', type=str, help="Path with files to read", default=False)
parser.add_argument('--input', dest='input', type=str, help="Input String with the text to format", required=True)
parser.add_argument('--align', dest='align', type=str, help="Type of text align", choices=['justify'])

if __name__ == '__main__':
    args = parser.parse_args()

    file_system = FileLocal(args.path)
    wrapper = ParagraphWrapper(limit=args.limit)
    aligner = None

    if args.align:
        aligner = JustifyAligner(limit=args.limit)

    formatter = Formatter(input_str=args.input, wrapper=wrapper, aligner=aligner, file_system=file_system)

    print(formatter.format(load_from_disk=bool(args.path)))
