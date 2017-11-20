import urllib.request as request

def captureImage():
	fileName = "/home/pi/Desktop/dev/python/robot/controller/static/img/capture.jpg"
	request.urlretrieve("http://localhost:8080/?action=snapshot", fileName)
	return fileName


print(captureImage())
