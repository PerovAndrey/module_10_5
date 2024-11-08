import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':
    start1 = datetime.datetime.now()

    for filename in filenames:
        # print(f)
        read_info(filename)
        end1 = datetime.datetime.now()
        time_of_line_function = end1 - start1
        print(f'{time_of_line_function} (линейный)')

    with multiprocessing.Pool(processes=4) as pool:
        start2 = datetime.datetime.now()
        pool.map(read_info, filenames)
        end2 = datetime.datetime.now()
        time_of_multiprocessing = end2 - start2
        print(f'{time_of_multiprocessing} (многопроцессный)')