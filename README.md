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

# Installation and Execution
## From binary release
Pre-compiled cs3 releases are portables and do not require a local installation. Download an executable matching your system and run it by clicking on it.
## From source
cs3 is made using [Qt 6.5](https://www.qt.io/) through [PySide6](https://wiki.qt.io/Qt_for_Python) and requires at least Python 3.7 or above. Using a virtual environment is the preferred way to compile this program, but isn't mandatory. All the following commands are issued from the root directory of the project.

### On Windows
1.  Creating the virtual environment (optional)
```batch
python3 -m venv .cs3_venv
cs3_venv\Scripts\activate.bat
```
2. Installing the dependencies
```batch
pip3 install -r requirements.txt
```
3. Generate UI resource files
Note: If your shell cannot find the following programs, either `activate` your virtual environment again, restart your shell or explicit their path (e.g. `.cs3_venv\bin\pyside6-uic`).
```batch
pyside6-rcc resources\icons.qrc -o icons_rc.py
pyside6-uic -o app\ui\main_window.py designer\main_window.ui
```
4. Running the program from the Python interpreter
Note:  If using a virtual environment, you have to `activate` it once before running the Python interpreter for the first time in your current shell session.
```batch
python3 main.py
```
5. Compile the program to a self-contained native application
_TBA_

### On *NIX
1. Creating the virtual environment (optional)
```bash
python3 -m venv .cs3_venv
source .cs3_venv/bin/activate
```
2. Installing the dependencies
```bash
pip3 install -r requirements.txt
```
3. Generate UI resource files
Note: If your shell cannot find the following programs, either `source` your virtual environment again, restart your shell or explicit their path (e.g. `.cs3_venv/bin/pyside6-uic`).
```bash
pyside6-rcc resources/icons.qrc -o icons_rc.py
pyside6-uic -o app/ui/main_window.py designer/main_window.ui
```
4. Run the program from the Python interpreter
Note: If using a virtual environment, you have to `source` it once before running the Python interpreter for the first time in your current shell session.
```bash
python3 main.py
```
5. Compile the program to a self-contained native application (optional)
This is a timely and compute-intensive step. You may also have to manually tweak the deployment file to solve possible paths issues you may encounter outside of a virtual environment.
5.1 Firstly, create the deployment specifications: ```pyside6-deploy --init --name cs3```
5.2 Open the file `pysidedeploy.spec` you just have created
5.3 Change the content of the `python_path` variable so that it's path is relative to the root folder of the project (such as `python_path = ./.cs3_venv/...`)
5.4 Change the content of the `excluded_qml_plugins`  variable by `QtQuick, QtQuick3D, QtCharts, QtWebEngine, QtTest, QtSensors` to reduce size of the produced application
5.5 Feel free to tweak the other variables as you see fit [if you know what you are doing](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#pysidedeploy-spec)
5.6 Run the command `pyside6-deploy -c pysidedeploy.spec`
5.7 Once the compilation is completed, you can run the application as any other graphic application by clicking on it. You no longer have to use the Python interpreter or to setup the virtual environment to run it.

# License
cs3 is released under the [LGPL v3](https://www.gnu.org/licenses/lgpl-3.0.html).
Some icons are taken from [KDE's Breeze icons pack](https://github.com/KDE/breeze-icons/tree/master), also under the LGPL v3.
