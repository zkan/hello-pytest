import sys
import argparse


def parse_args(arg_str: str | None = ""):
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--greeting", type=str, default="Hello")
    parser.add_argument("-n", "--name", type=str, default="World")

    arg_list = None if arg_str is None else arg_str.split()

    args = parser.parse_args(arg_list)

    print(f"in parse_args({arg_str=})")
    print(f"    {arg_list=}")
    print(f"    {args=}")
    print(f"    {args.greeting=}")
    print(f"    {args.name=}")

    return args



def main():
    print(f"{sys.argv=}")

    parse_args(None)
    # parse_args("-c 2 -v --out foo.py")  # to test args
    # parse_args("")  # to test no args


if __name__ == "__main__":
    main()
