from unittest.mock import patch
import urllib.request

def read_webpage(url):
    response = urllib.request.urlopen(url)
    return response.read()


@patch('urllib.request.urlopen')
def dummy_reader(mock_obj):
    result = read_webpage('https://www.google.com/') #webreader.read_webpage('https://www.google.com/')
    mock_obj.assert_called_with('https://www.google.com/')
    print(result)

if __name__ == '__main__':
    dummy_reader()

'''
    Here we just import our previously created module and the patch function from the mock module. Then we create a decorator that patches urllib.request.urlopen. Inside the function, we call our webreader module’s read_webpage function with Google’s URL and print the result. If you run this code, you will see that instead of getting HTML for our result, we get a MagicMock object instead. This demonstrates the power of patch. We can now prevent the downloading of data while still calling the original function correctly.

    The documentation points out that you can stack path decorators just as you can with regular decorators. So if you have a really complex function that accesses databases or writes file or pretty much anything else, you can add multiple patches to prevent side effects from happening.
'''