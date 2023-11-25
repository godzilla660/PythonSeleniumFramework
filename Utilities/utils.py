# import self
import softest


class Utils(softest.TestCase):
    def assertListItems(self, list, value):
        for stop in list:
            print("The text is: " +stop.text)
            self.soft_assert(self.assertEquals, stop.text, value)
            if stop.text == value:
                print("test passed")
            else:
                print("test failed")
            #pass
        self.assert_all()