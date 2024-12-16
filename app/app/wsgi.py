import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

from whitenoise import WhiteNoise

# from my_project import MyWSGIApp

# application = MyWSGIApp()
# application = WhiteNoise(application, root="/path/to/static/files")
# application.add_files("/path/to/more/static/files", prefix="more-files/")