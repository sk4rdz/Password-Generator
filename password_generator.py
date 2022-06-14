import argparse
import string
import random

DEFAULT_DIGIT = 8
DEFAULT_NUM = 1

def parse():
    parser = argparse.ArgumentParser(description="数字、大文字、小文字からなるパスワードを生成します。")
    parser.add_argument("-d", "--digit", type=int, default=DEFAULT_DIGIT, help="パスワードの桁数")
    parser.add_argument("-n", "--number", type=int, default=DEFAULT_NUM, help="生成するパスワードの数")
    parser.add_argument('--nonduplicate', action='store_true', help="重複なしで生成する")
    args = parser.parse_args()
    return args.digit, args.number, args.nonduplicate

def main():
    digit, num, non_duplicate = parse()
    letters = string.digits + string.ascii_letters
    generate = random.sample if non_duplicate else random.choices
    print(*["".join(generate(letters, k=digit)) for _ in range(num)])

if __name__ == "__main__": main()
