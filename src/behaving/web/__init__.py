from urllib2 import URLError


def setup(context):
    if not hasattr(context, 'default_browser'):
        context.default_browser = ''
    if not hasattr(context, 'attachment_dir'):
        context.attachment_dir = '/'
    if not hasattr(context, 'base_url'):
        context.base_url = ''

    context.browser = None
    context.browsers = {}


def teardown(context):
    for browser in context.browsers.values():
        try:
            browser.quit()
        except URLError:
            pass

    context.browser = None
    context.browsers = {}
