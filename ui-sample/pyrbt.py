#!/usr/bin/python3

import os

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')

from gi.repository import GObject, Gtk, GtkSource

from pyrob import tasks


def refresh_labels_state(labels, state):
    for (id, task) in tasks.task_list:
        text = task.title
        st = state['tasks'][id]
        if st['locked']:
            prefix = '🔒'
        elif st['failed']:
            prefix = '✘'
        elif st['solved']:
            prefix = '✔'
        else:
            prefix = '❗'

        text = prefix + ' ' + text
        if id == state['current_task']:
            text = '<b>{}</b>'.format(text)

        labels[id].set_markup(text)


# загружаем интерфейс при помощи GtkBuilder
GObject.type_register(GtkSource.View)
builder = Gtk.Builder()
builder.add_from_file(os.path.join(os.path.dirname(__file__), 'ui', 'main_window.ui'))

# загружаем список задач
container = builder.get_object('task_list_vbox')

labels = {}
for (id, task) in tasks.task_list:
    label = Gtk.Label()
    labels[id] = label
    #label.set_markup("<b>✓✔✘🔒 %s</b>" % )
    container.pack_start(label, False, False, 0)

# включаем подсветку синтаксиса
buffer = GtkSource.Buffer()
source_view = builder.get_object('editor')
source_view.set_buffer(buffer)

lang_manager = GtkSource.LanguageManager()
python_lang = lang_manager.get_language('python')
buffer.set_language(python_lang)

# отображаем главное окно
main_window = builder.get_object('main_window')
main_window.show_all()
main_window.connect("delete-event", Gtk.main_quit)

# задаём начальное состояние
state = {
    'current_task': tasks.task_list[0][0],
    'tasks': {id: dict(locked=n > 0, solved=False, failed=False, code=None) for (n, (id, _)) in enumerate(
        tasks.task_list)}
}

# отрисовываем текущее состояние
refresh_labels_state(labels, state)

# запускаем основной цикл
Gtk.main()


# bounds = buffer.get_bounds()
# print(buffer.get_text(bounds.start, bounds.end, True))
