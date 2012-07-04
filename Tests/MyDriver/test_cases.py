__author__ = 'Denis Arkusha'

from nose.plugins.attrib import attr
import Tests.MyDriver.Pages.landing_page as landing_page
import Tests.MyDriver.expected_results as expected

class TestCasesForCrocs():
    @attr('parallel')
    def test_the_landing_page_is_opened(self):
        landing_page.open()
        assert landing_page.get_title() == expected.landing_page_title

    @attr('parallel')
    def test_the_landing_page_search_performed_correctly(self):
        landing_page.open()
        landing_page.search()
        assert landing_page.get_search_result() == expected.landing_page_search_result