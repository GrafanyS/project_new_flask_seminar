import requests
from multiprocessing import Process
import time

urls = [
    'https://vk.com/',
    'https://youtube.com/',
    'https://wireframe.cc/WJ4Lb1',
    'https://letsencrypt.org/ru/',
    'https://getbootstrap.com/docs/5.3/components/button-group/',
    'https://edit.org/edit/all/14sxb7zt9',
    'https://pythontutor.com/render.html#mode=edit',
    'https://timeweb.cloud/',
    'https://linkmeup.ru/blog/',
    'https://ya.ru'
]


def download(url_):
    response = requests.get(url_)
    filename = 'bd/multiprocessing_' + url_.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url_} in {time.time() - start_time:.2f}seconds")


processes = []
start_time = time.time()


if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
