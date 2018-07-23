import os
import os.path
import re

import logging

logging.basicConfig(format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.DEBUG)

# TODO: Реализовать получение из конфига
task_rot = 'E:\\Work\\python\\task_manager\\test\\Задачи'


def task_dir_create():
    hg_dir = os.getcwd()
    logging.info('Текущий каталог (клон репозитория Mercurial) {}'.format(hg_dir))

    task_dir_name = re.search('dev-local-(\d+-\w+)', hg_dir).group(1)
    if not task_dir_name:
        logging.error('Данную команду необходимо запускать из клона репозитория Mercurial')
        logging.error('Имя каталога клона должено соответствовать формату dev-local-<Номер задачи>-<Краткое кодовое описание задачи>')
        return

    logging.info('Хранилище рабоих гаталогов задач: {}'.format(task_rot))
    if not os.path.exists(task_rot):
        logging.error('Хранилище рабоих гаталогов задач не существует')
        return

    task_dir = os.path.join(task_rot, task_dir_name)
    if os.path.exists(task_dir):
        logging.info('Рабоий гаталог задачи [{}] уже создан'.format(task_dir))
    else:
        os.mkdir(task_dir)
        logging.info('Создан Рабоий гаталог задачи [{}]'.format(task_dir))
    task_keep = os.path.join(task_dir, 'keep.txt')
    open(task_keep, 'a').close()
    logging.info('Создан файл заметок [{}]'.format(task_keep))

