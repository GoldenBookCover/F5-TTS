from argparse import ArgumentParser
from importlib import import_module
from glob import glob


_version = '1.0.0'


def main(args) :
    if args.unique :
        all_chars = set()
        accumulate = all_chars.add
    else :
        all_chars = []
        accumulate = all_chars.append

    tokenizer = import_module(f"f5_tts.model.cctokenizers.{args.language[0]}").Tokenizer()
    for tt in args.text_files :
        for t in glob(tt) :
            with open(t, 'r', encoding='utf-8') as f :
                for line in f :
                    for c in tokenizer.convert_chars(line.strip()):
                        accumulate(c)
    with open(args.output[0], 'w', encoding='utf-8') as f :
        f.write('\n'.join(all_chars))


if __name__ == '__main__' :
    # Arguments list
    parser = ArgumentParser(description='这个程序的说明')
    parser.add_argument('-v', '--version', action='version', version=f"version: {_version}", help='显示版本并退出')
    parser.add_argument('-l', '--language', type=str, nargs=1, choices=('ne', ), help='指定文本语言')
    parser.add_argument('-o', '--output', type=str, nargs=1, default=('result.txt', ), help='指定输出路径')
    parser.add_argument('-u', '--unique', action='store_true', help='去重')
    parser.add_argument('text_files', metavar='TEXT_FILES', type=str, nargs='*', default=(), help='输入的文本文件')

    args = parser.parse_args()
    main(args)
