from naoqi import ALProxy

# Connect to robot
tablet = ALProxy("ALTabletService", "192.168.0.108", 9559)

# Display a web page (can be local or online)
tablet.showWebview("http://example.com")

# Hide the webview
# tablet.hideWebview()

# Show an image
# tablet.showImage("http://url-to-your-image.jpg")
