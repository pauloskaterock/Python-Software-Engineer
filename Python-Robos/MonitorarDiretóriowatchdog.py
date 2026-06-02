# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import shutil
# import time

# class MyHandler(FileSystemEventHandler):
#     def on_created(self, event):
#         if event.is_directory:
#             return
#         shutil.copy(event.src_path, 'caminho/para/destino')

# event_handler = MyHandler()
# observer = Observer()
# observer.schedule(event_handler, path='caminho/para/diretorio', recursive=False)
# observer.start()

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     observer.stop()
# observer.join()
