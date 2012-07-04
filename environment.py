from inject.scopes import Request
import inject

test_scope = Request()

class Environment():
    """
    Abstract class for defining the environment. Inherit it and define you dependency injection configuration in configure method.
    """

    def __init__(self):
        self.injector = inject.Injector()

        self.before_suite_hooks = []
        self.after_suite_hooks = []

        self.before_test_hooks = []
        self.after_test_hooks = []

    def before_suite(self):
        self.configure()
        inject.register(self.injector)

        for hook in self.before_suite_hooks:
            hook()

    def after_suite(self):
        for hook in self.after_suite_hooks:
            hook()
        inject.unregister(self.injector)

    def before_test(self):
        for hook in self.before_test_hooks:
            hook()
        self.register_test_scope()

    def register_test_scope(self):
        test_scope.register()

    def after_test(self):
        for hook in self.after_test_hooks:
            hook()
        self.unregister_test_scope()

    def unregister_test_scope(self):
        test_scope.unregister()

    def before_suite_hook(self, hook):
        self.before_suite_hooks.append(hook)

    def after_suite_hook(self, hook):
        self.after_suite_hooks.append(hook)

    def before_test_hook(self, hook):
        self.before_suite_hooks.append(hook)

    def after_test_hook(self, hook):
        self.after_test_hooks.append(hook)

    def configure(self):
        pass
