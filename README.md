# pyqt-hidable-menubar
PyQt Hidable Menubar (show/hide menu bar with close button at the right corner of it)

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-hidable-menubar.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-icon-pushbutton.git">pyqt-svg-icon-pushbutton</a> - To svg file button (close button's icon is svg file)

## Usage
You can see the button at the right corner. 

![image](https://user-images.githubusercontent.com/55078043/157560268-866c9e48-8a8c-4060-8526-0c8d1ad298ff.png)

If you click it, menu bar will be hidden but not completely(small space remains). 

If you want to show it again, just move the mouse cursor to the space.

![image](https://user-images.githubusercontent.com/55078043/157560287-97c6fcfe-7a1f-4a12-940e-6cc9f4049711.png)

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from pyqt_hidable_menubar import HidableMenuBar

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    hidableMenuBar = HidableMenuBar()
    fileMenu = QMenu('File', mainWindow)
    hidableMenuBar.addMenu(fileMenu)
    mainWindow.setMenuBar(hidableMenuBar)
    mainWindow.show()
    app.exec_()
```

Result

Showing state

![image](https://user-images.githubusercontent.com/55078043/157560268-866c9e48-8a8c-4060-8526-0c8d1ad298ff.png)

Hiding state

![image](https://user-images.githubusercontent.com/55078043/157560287-97c6fcfe-7a1f-4a12-940e-6cc9f4049711.png)
