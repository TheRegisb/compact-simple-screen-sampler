# Compact Simple Screen Sampler
cs3 is a simple, cross-platform graphic desktop utility that can sample the color of a pixel or a region of the screen, display its value in numerous formats, reformat the output and copy it to the clipboard.
This software is also multi-language, as in the UI will be in French if your system locale is also French. Thrilling!

# Usage
You can download a pre-compiled binary release of this program to immediately start using it. You may also run it from the source files using the Python interpreter or compile it into your own version (see installation instruction below).
Here are the features and behavior of cs3:
* Press the “Sample Screen” button to start the sampling session. cs3 will take exclusive control of the mouse and keyword for the duration of the session.
	* Using the single-pixel selection mode, left-click on any point of a screen to sample the color of the pixel.
	* Using the region-average selection mode, left-click and drag the mouse to draw a rectangular selection.
* You can cancel a sampling session at any time using the Esc key, the right-mouse button or middle-mouse button.
* Use the “Previous” and “Next” arrow buttons to display previously-taken color samples. These samples are not saved when you quit the application.
* Use the check-boxes and editable text boxes to adjust the format of the color.
* Click on the copy buttons to replace the content of your clipboard with the value of the field.

# Limitation
* Color values may not be accurate outside of an 8-bits sRGB color space.
* In region selection mode, the selection rectangle cannot span over multiple screens.
* This program has only been tested on Windows 10 and Fedora 38 (x11). Other OS or graphic environments may or may not work as intended.

# Installation and Execution
## From binary release
Pre-compiled cs3 releases are portables and do not require a local installation. Download an executable matching your system and run it by clicking on it.
## From source
cs3 is made using [Qt 6.5](https://www.qt.io/) through [PySide6](https://wiki.qt.io/Qt_for_Python) and requires at least Python 3.7 or above. Using a virtual environment is the preferred way to compile this program, but isn't mandatory.

### On Windows
1. Creating the virtual environment (optional)
Should you wish to compile the program, the virtual environment __must not__ be present in the same folder as the root of the project. You could create it at the same level of the folder that contains the project, like the following:
```
My Documents
├─── cs3
│   ├─── .cs3_venv
└───└─── cs3_main
        ├─── README.md
        └─── ...
```
```batch
:: in "My Documents\cs3"
py -3 -m venv .cs3_venv
.cs3_venv\Scripts\activate.bat
cd cs3_main
```
2. Installing the dependencies
```batch
pip3 install -r requirements.txt
```
3. Generating the UI resource files
Note: If your shell cannot find the following programs, either `activate` your virtual environment again, restart your shell or explicit their path (e.g. `.cs3_venv\bin\pyside6-uic`).
```batch
FOR /F %i IN ('DIR /B/D resources\translations\*.ts') DO pyside6-lrelease resources\translations\%i -qm resources\translations\%~ni.qm
pyside6-rcc resources\cs3.qrc -o cs3_rc.py
pyside6-uic -o app\ui\main_window.py designer\main_window.ui
```
4. Running the program from the Python interpreter
Note:  If using a virtual environment, you have to `activate` it once before running the Python interpreter for the first time in your current shell session.
```batch
python main.py
```
5. Compiling the program to a self-contained native application (optional)
This is a timely and compute-intensive step. You may also have to manually tweak the deployment file to solve possible paths issues you may encounter outside of a virtual environment.
5.1 Firstly, create the deployment specifications: ```pyside6-deploy --init --name cs3```
5.2 Open the file `pysidedeploy.spec` you just have created
5.3 Change the content of the `excluded_qml_plugins`  variable by `QtQuick, QtQuick3D, QtCharts, QtWebEngine, QtTest, QtSensors` to reduce size of the produced application
5.4 Add `--windows-disable-console` to the arguments of `extra_args`
5.5 Feel free to tweak the other variables as you see fit [if you know what you are doing](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#pysidedeploy-spec)
5.6 Run the command `pyside6-deploy -c pysidedeploy.spec`
5.7 Once the compilation is completed, you can run the application as any other graphic application by clicking on it. You no longer have to use the Python interpreter or to setup the virtual environment to run it.

### On *NIX
1. Creating the virtual environment (optional)
Should you wish to compile the program, the virtual environment __should not__ be present in the same folder as the root of the project, or you will slowly generated a over-bloated application. You could create it at the same level of the folder that contains the project, like the following:
```
projects
├─── cs3
│   ├─── .cs3_venv
└───└─── cs3_main
        ├─── README.md
        └─── ...
```
```bash
# In projects/cs3
python3 -m venv .cs3_venv
source .cs3_venv/bin/activate
cd cs3_main
```
2. Installing the dependencies
```bash
pip3 install -r requirements.txt
```
3. Generating UI resource files
Note: If your shell cannot find the following programs, either `source` your virtual environment again, restart your shell or explicit their path (e.g. `.cs3_venv/bin/pyside6-uic`).
```bash
for i in resources/translations/*.ts; do pyside6-lrelease "$i" -qm "${i%.*}".qm; done
pyside6-rcc resources/cs3.qrc -o cs3_rc.py
pyside6-uic -o app/ui/main_window.py designer/main_window.ui
```
4. Running the program from the Python interpreter
Note: If using a virtual environment, you have to `source` it once before running the Python interpreter for the first time in your current shell session.
```bash
python3 main.py
```
5. Compiling the program to a self-contained native application (optional)
This is a timely and compute-intensive step. You may also have to manually tweak the deployment file to solve possible paths issues you may encounter outside of a virtual environment.
5.1 Firstly, create the deployment specifications: ```pyside6-deploy --init --name cs3```
5.2 Open the file `pysidedeploy.spec` you just have created
5.3 Change the content of the `python_path` variable so that it's path is relative to the root folder of the project (such as `python_path = ./.cs3_venv/...`)
5.4 Change the content of the `excluded_qml_plugins`  variable by `QtQuick, QtQuick3D, QtCharts, QtWebEngine, QtTest, QtSensors` to reduce size of the produced application
5.5 Feel free to tweak the other variables as you see fit [if you know what you are doing](https://doc.qt.io/qtforpython-6/deployment/deployment-pyside6-deploy.html#pysidedeploy-spec)
5.6 Run the command `pyside6-deploy -c pysidedeploy.spec`
5.7 Once the compilation is completed, you can run the application as any other graphic application by clicking on it. You no longer have to use the Python interpreter or to setup the virtual environment to run it.
# Creating Additional Translations
Using the [Qt Linguist module](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/translations.html), one is able to translate the dozen of strings displayed by this application. All required utilities are bundled with the PySide6-essentials PIP package. The following steps are identical between Windows ans other systems, just mind the path separator (backward or forward slash).
1. Generate a transcription file from the exiting UI element by running the following command. Replace `<target_language>` with the actual language name or locale code you want to translate in.
```bash
pyside6-lupdate designer/cs3.ui -ts resources/translations/<target_language>.ts
```
2. To translate a transcription file, you could either do it by editing the `.ts` file by hand or by running QLinguist, a graphic program.
```bash
pyside6-linguist resources/translations/<target_language>.ts # Or your editor of choice
pyside6-lrelease resources/translations/<target_language>.ts -qm resources/translations/<target_language>.qm # If you did not released the .qm file using QLinguist
```
3. You must now add the reference of your new translation into the resource bundle file, namely `resources/cs3.qrc`. Within the `<qresource prefix="lang">` tag, add the a new entry such as
```xml
<file>translations/<target_language>.qm</file>
```
4. Refresh the auto-generated Python resources by running the `rcc` utility again.
```bash
pyside6-rcc resources/cs3.qrc -o cs3_rc.py
```
5. Lastly, manually update the code of the Cs3Runner Python class located at the bottom of the `app/cs3.py` file. You can try to match you file to a specific locale ([see official documentation](https://doc.qt.io/qtforpython-6/tutorials/basictutorial/translations.html)) or hack in some mechanism to use a single translation for multiple dialects. On Linux, you can try to change your local for a single command by overloading the `LC_ALL` variable before a command.
```bash
LC_ALL="es_ES.UTF-8" python3 main.py
```
# License
cs3 is released under the [LGPL v3](https://www.gnu.org/licenses/lgpl-3.0.html).
Some icons are taken from [KDE's Breeze icons pack](https://github.com/KDE/breeze-icons/tree/master), also under the LGPL v3.
