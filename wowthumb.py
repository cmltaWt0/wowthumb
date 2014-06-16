import request

cams_setting = {
	'cam1': 'http://user:camera46@192.168.0.46/axis-cgi/jpg/image.cgi?resolution=320x180',
	'cam2': 'http://user:camera47@192.168.0.47/axis-cgi/jpg/image.cgi?resolution=320x180',
	'cam3': 'http://user:camera48@192.168.0.48/axis-cgi/jpg/image.cgi?resolution=320x180',
	'cam4': 'http://user:camera49@192.168.0.49/axis-cgi/jpg/image.cgi?resolution=320x180',
	'cam5': 'http://user:camera50@192.168.0.50/axis-cgi/jpg/image.cgi?resolution=320x180',
	'cam6': 'http://user:camera53@192.168.0.53/axis-cgi/jpg/image.cgi?resolution=320x180',
	'cam7': 'http://user:camera54@192.168.0.54/axis-cgi/jpg/image.cgi?resolution=320x180',
	'cam8': 'http://user:camera52@192.168.0.52/axis-cgi/jpg/image.cgi?resolution=320x180',
	'cam9': 'http://user:camera51@192.168.0.51/axis-cgi/jpg/image.cgi?resolution=320x180'
}


# TODO change request.get() to twisted specific method
# TODO add caching for 30 sec
def callback(request, cam):
    try:
        img = requests.get(cams_settings.get('cam' + str(cam),
	                       cams_settings['cam4']), timeout=1)
        f = open('cam' + str(cam), 'wb')
        f.write(img.content)
        f.close()
    except requests.exceptions.Timeout:
        f = open('cam' + str(cam), 'rb')
        img = f.read()
        f.close()
    # TODO add content-type: "image/jpeg"
    # Django-like: return HttpResponse(img, content_type="image/jpeg")
    return img


# TODO Add Factory and Protocol with callback


# TODO resolve folowing regex:
# urlpatterns = patterns('',
#    url(r'^$', TemplateView.as_view(template_name='camsgrab/default.html'), name='default'),
#    url(r'^pathkey=cam(\d+)/*$', 'camsgrab.views.dispatcher', name='dispatcher'),
#)