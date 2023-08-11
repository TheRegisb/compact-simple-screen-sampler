
# Compact Simple Screen Sampler
cs3 is a simple and cross-platform graphic desktop utility that can sample the color of a pixel or a region of the screen, display its value in numerous formats, reformat the output and copy it to the clipboard.

# Usage
You can download a pre-compiled binary release of this program to immediately start using it. You may also run it from the source files using the Python interpreter or compile it into your own version (see installation instruction below).
Here are the features and behavior of cs3:
* Press the “Sample Screen” button to start the sampling session. cs3 will take exclusive control of the mouse and keybord for the duration of the session.
	* Using the single-pixel selection mode, left-click on any point of a screen to sample the color of the pixel.
	* Using the region-average selection mode, left-click and drag the mouse to draw a rectangular selection.
* You can cancel a sampling session at any time using the Esc key, the right-mouse button or middle-mouse button.
* Use the “Previous” and “Next” arrow buttons to display previously-taken color samples. These samples are not saved when you quit the application.
* Use the checkboxes and editable text boxes to adjust the format of the color.
* Click on the copy buttons to replace the content of your clipboard with the value of the field.

# Limitation
* Color values may not be accurate outside of an 8-bits sRGB color space.
* This program has only been tested on Windows 10 and Fedora 38 (x11). Other OS or graphic environments may or may not work as intended.

# Installation
## From source
cs3 is made using [Qt 6.5](https://www.qt.io/) through [PySide6](https://wiki.qt.io/Qt_for_Python) and requires at least Python 3.7 or above. Using a virtual environment is the preferred way to compile this program, but isn't mandatory. All the following commands are issued from the root directory of the project.

### On Windows
1.  Creating the virtual environment (optional)
```batch
py -3 -m venv cs3_venv
cs3_venv\Scripts\activate.bat
```
2. Installing the dependencies
```batch
pip3 install -r requirements.txt
```
3. Refreshing UI files (if manual changes were made)
```batch
pyside6-rcc resources\icons.qrc -o src\icons_rc.py
pyside6-uic -o src\ui\main_window.py designer\main_window.ui
```
4. Running the program from the Python interpreter
```batch
python3 src\cs3.py
```
5. Compile the program to a self-contained native application
_TBA_

### On *NIX
1. Creating the virutal environment (optional)
```bash
py -3 -m venv cs3_venv
source cs3_venv/bin/activate
```
2. Installing the dependencies
```bash
pip3 install -r requirements.txt
```
3. Refreshing UI files (if manual changes were made)
```bash
pyside6-rcc resources/icons.qrc -o src/icons_rc.py
pyside6-uic -o src/ui/main_window.py designer/main_window.ui
```
4. Running the program from the Python interpreter
```bash
python3 src/cs3.py
```
4. Compile the program to a self-contained native application
_TBA_


# Licence
cs3 is released under the [LGPL v3](https://www.gnu.org/licenses/lgpl-3.0.html).
Some icons are taken from [KDE's Breeze icons pack](https://github.com/KDE/breeze-icons/tree/master), also under the LGPL v3.
