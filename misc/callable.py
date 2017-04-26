# -*- coding: utf-8 -*-


class TestCallable(object):

    def func(self):
        print "func"

    def __call__(self, msg):
        self.func()
        print msg


if __name__ == '__main__':
    TestCallable()("hello, call...")
