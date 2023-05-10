class StarkConfig(object):

    def __init__(self, num):
        self.num = num

    def changelist(self, request):
        print(self.num, request)

    def run(self):
        self.changelist(999)


class RoleConfig(StarkConfig):

    def changelist(self, request):
        print(666, self.num)


class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self, k, v):
        self._registry[k] = v


site = AdminSite()

site.register('武沛齐', StarkConfig(19))
site.register('root', StarkConfig(20))
site.register("admin", RoleConfig(33))

print(len(site._registry))

for k, row in site._registry.items():
    row.changelist(5)

