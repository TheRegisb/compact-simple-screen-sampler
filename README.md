# Compact Simple Screen Sampler
cs3 is a simple and cross-platform graphic utility that can sample the color of a pixel or a region of the screen, display its value in numerous formats, reformat the output and copy it to the clipboard.

# Usage
* Press the “Sample Screen” button to start the sampling session. cs3 will take exclusive control of the mouse and keybord for the duration of the session.
* Using the single-pixel selection mode, left-click on any point of a screen to sample the color of the pixel. Using the region-average selection mode, left-click and drag the mouse to draw a rectangular selection.
* You can cancel a sampling session at any time using the Esc key, the right-mouse button or middle-mouse button.
* Use the “Previous” and “Next” arrow buttons to display previously-taken color samples. These samples are not saved when you quit the application.
* Use the checkboxes and editable text boxes to adjust the format of the color.
* Click on the copy buttons to replace the content of your clipboard with the value of the field.

# Limitation
* Region-average selection cannot span over multiple screens
* Color values may not be accurate outside of an 8-bits sRGB color space.

# Installation
## From source
cs3 is made using Qt 6.5 through PySide6 and requires at least Python 3.5. Using a virtual environment is the preferred way of installing this program, but isn't mandatory. Clone this repository and then type these command at the root of the projects.

```python
python3 -m venv cs3_venv
source cs3_venv/bin/activate
pip3 install -r requirements.txt
```

If you wish to not use a virtual environment, skip to the pip install.
Once all dependencies are resolved on your system, you may run cs3 using
```python
source cs3_venv/bin/activate
python3 src/cs3.py
```
Skip the `source` command if you do not use a virtual environment.

## From binary release
_TBA_

# Licence
cs3 is released under the [LGPL v3](https://www.gnu.org/licenses/lgpl-3.0.html).
