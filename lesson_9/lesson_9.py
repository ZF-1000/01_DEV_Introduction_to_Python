"""
python -m venv .folder - создание виртуального окружения
Флаг -m указывает Python-у запустить venv как исполняемый модуль.
.folder — название виртуального окружения (где будут храниться ваши библиотеки).

Активация
Чтобы начать пользоваться виртуальным окружением, необходимо его активировать:
.\.folder\Scripts\activate.bat - для Windows; - так не сработало
source .folder/bin/activate - для Linux и MacOS.

.\.folder\Scripts\activate - вот так сработало

pip list - список установленных пакетов
очень длинный путь надо переместить проект ближе к корню
"""

from isOdd import isOdd

print(isOdd(1))   # => true
print(isOdd(5))   # => true

print(isOdd(0))     # => false
print(isOdd(4))     # => false


from progress.bar import Bar
import time

bar = Bar('Processing', max=20)
for i in range(20):
    time.sleep(1)
    bar.next()
bar.finish()


import emoji
print(emoji.emojize('Python is :thumbs_up:'))                   # -> Python is 👍
print(emoji.emojize('Python is :thumbsup:', language='alias'))  # -> Python is 👍
print(emoji.demojize('Python is 👍'))                           # -> Python is :thumbs_up:
print(emoji.emojize("Python is fun :red_heart:"))               # -> Python is fun ❤
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type")) # -> Python is fun ❤️ #red heart, not black heart
print(emoji.is_emoji("👍"))  # -> True


import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()



