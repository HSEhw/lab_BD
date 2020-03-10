from back_end import *
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DBApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
