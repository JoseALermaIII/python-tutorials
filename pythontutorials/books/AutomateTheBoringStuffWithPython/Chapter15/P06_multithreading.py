# This program uses the threading module to manipulate threads

import threading

# Passing Arguments to the Thread's Target Function
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()
