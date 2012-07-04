__author__ = 'Denis Arkusha'

# Example of pytomate usage

import inject
from selenium import webdriver
import nose
from environment import Environment, test_scope
from nose_plugin import EnvironmentRunnerPlugin

class MyEnv(Environment):

    def configure(self):

        def get_webdriver():
            return webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)

        @inject.param("webdriver", "webdriver")
        def driver_quit(webdriver):
            webdriver.quit()

        self.injector.bind("webdriver", to=get_webdriver, scope=test_scope)
        self.after_test_hook(driver_quit)

env = MyEnv()
if __name__ == '__main__':
    nose.main(argv=['-c setup.cfg'],addplugins=[EnvironmentRunnerPlugin(env)])

  