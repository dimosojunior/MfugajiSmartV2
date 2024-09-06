from django.apps import AppConfig
from django.utils.autoreload import restart_with_reloader
import threading


class AppConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'App'

	#-------------FOR JOBS.py------------
	# def ready(self):
	# 	from jobs import updater
	# 	updater.start()

	#--------------FOR SCHEDULER.py-----------
	# def ready(self):
	# 	from .scheduler import start
	# 	start()

	#------------For test1.py-----------
	def ready(self):
		from .test1 import start_scheduler

		def start_scheduler_thread():
		    start_scheduler()

		thread = threading.Thread(target=start_scheduler_thread)
		thread.daemon = True  # Daemonize thread to exit when the main program exits
		thread.start()