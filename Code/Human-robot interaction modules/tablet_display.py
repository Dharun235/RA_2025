from naoqi import ALProxy

class TabletDisplay:
    def __init__(self, ip="127.0.0.1", port=9559):
        self.tablet = ALProxy("ALTabletService", ip, port)

    def show_web_page(self, url):
        """Displays a web page on Pepper's tablet."""
        self.tablet.showWebview(url)

    def hide_web_page(self):
        """Hides any content currently displayed."""
        self.tablet.hideWebview()

    def display_image(self, image_url):
        """Displays an image on the tablet."""
        html_content = f"<html><body><img src='{image_url}' width='100%' height='100%'></body></html>"
        self.tablet.showWebview("data:text/html," + html_content)
