class MyCls:
    attr = 123
    def get1(self, name):
        return MyCls.attr
    def get2(self, name):
        # return self.attr
        return getattr(self, name)
    def get3(self, name):
        cls = type(self)
        # return cls.attr
        return getattr(cls, name)

myobj = MyCls()
print(f"{myobj.get1('attr')=}")
print(f"{myobj.get2('attr')=}")
print(f"{myobj.get3('attr')=}")