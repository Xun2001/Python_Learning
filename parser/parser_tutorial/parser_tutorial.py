import argparse


parser = argparse.ArgumentParser() # 创建一个 ArgumentParser 对象，用于定义和解析命令行参数。

# Positional argument

parser.add_argument("echo", help="echo the string you use here")

parser.add_argument("square", help="display a square of a given number",
                    type=int)


# Optional argument

parser.add_argument("--verbosity", help="increase output verbosity")

parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true") # 如果指定，则将该值存储为 True 否则为 False

parser.add_argument("-num","--number", help="number for choice",choices=[0, 1, 2],
                    default=1,type=int)

parser.add_argument('-g','--usegpu',help='whether to use gpu',
                    default=True,type=bool)

# Parse_args() method return the args
args = parser.parse_args() # 调用 parse_args() 方法解析命令行参数，并将解析结果返回给 args 对象中。

print(f"Running '{__file__}'") # Running 'parser_tutorial.py'
print(f"Running '{__name__}'") # Running '__main__' 以主函数直接运行的都叫 __main__

print(args.echo)

print(args.square**2)

if args.verbosity:
    print("verbosity turned on")