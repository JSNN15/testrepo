from PythonTSI.Communicator import Communicator
from PythonTSI.DataAnalyzer import DataAnalyzer


def main():
    communicator = Communicator(115200)
    communicator.run()


if __name__ == '__main__':
    main()
