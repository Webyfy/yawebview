# yawebview
yawebview(Yet Another Webview library) that helps you build cross platform GUI for python applications using web technologies(HTML, JavaScript and CSS).

yawebview is tailor-made for [YADE](https://gitlab.com/webyfy/iot/e-gurukul/yade) development. yawebview contains common code that we were going to write anyway.

## Dependencies
`yawebview` uses QtWebChannel via PySide2. It can be installed via native packages as well as pip.

### Native packages (recommended)
To install dependencies on Debian-based systems 
```shell
sudo apt install python3-pyside2.qtwebenginewidgets
```

### pip (no recommended)
```shell
pip install pywebview[pyside2]
```

If you get an error similar to the following,
```
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

Aborted (core dumped)
```
install `libxcb-xinerama0` to resolve the issue.
