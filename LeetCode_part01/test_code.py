# -*- coding:utf8 -

def out_func(out_name):
    def in_func(in_name):
        print(out_name.title() + " " + in_name.title())
    print("this is user()")
    return in_func


# 你好
a = out_func("tom")
a("jerry")
out_func("tom")("jerry")
