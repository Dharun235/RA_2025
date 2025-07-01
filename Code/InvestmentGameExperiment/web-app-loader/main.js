const { app, BrowserWindow, globalShortcut } = require('electron');
const path = require('path');

let mainWindow;
let splash;

function createWindow() {
    // Splash Window in kiosk/fullscreen mode
    splash = new BrowserWindow({
        width: 1024,
        height: 768,
        frame: false,
        transparent: true,
        alwaysOnTop: true,
        resizable: false,
        skipTaskbar: true,
        show: false,
        kiosk: true,
        fullscreen: true,
        autoHideMenuBar: true,
    });

    splash.loadFile('splash.html');
    splash.once('ready-to-show', () => splash.show());

    mainWindow = new BrowserWindow({
        width: 1024,
        height: 768,
        resizable: false,
        frame: false,
        kiosk: true,
        autoHideMenuBar: true,
        movable: false,
        minimizable: false,
        maximizable: false,
        closable: false,
        skipTaskbar: true,
        show: false,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    });

    // Disable minimize action
    mainWindow.on('minimize', e => e.preventDefault());

    // Remove move handler if present
    // mainWindow.on('move', () => {});  // Remove or comment this out


    mainWindow.loadURL('http://127.0.0.1:1234');

    mainWindow.webContents.on('did-finish-load', () => {
        if (splash && !splash.isDestroyed()) splash.destroy();
        mainWindow.show();
    });

    mainWindow.webContents.on('did-start-loading', () => {
        const [width, height] = mainWindow.getSize();
        const [x, y] = mainWindow.getPosition();

        if (!splash || splash.isDestroyed()) {
            splash = new BrowserWindow({
                width,
                height,
                x,
                y,
                frame: false,
                transparent: true,
                alwaysOnTop: true,
                resizable: false,
                skipTaskbar: true,
                show: false,
                kiosk: true,
                fullscreen: true,
                autoHideMenuBar: true,
            });
            splash.loadFile('splash.html');
            splash.once('ready-to-show', () => splash.show());
        }
    });

    mainWindow.webContents.on('did-stop-loading', () => {
        if (splash && !splash.isDestroyed()) splash.close();
    });

    mainWindow.on('move', () => {
        if (splash && !splash.isDestroyed()) {
            const [x, y] = mainWindow.getPosition();
            splash.setPosition(x, y);
        }
    });

    // Register global shortcut Ctrl+Q / Cmd+Q to quit app
    globalShortcut.register('CommandOrControl+Q', () => {
        app.quit();
    });
}

app.whenReady().then(createWindow);

app.on('will-quit', () => {
    // Unregister all shortcuts when quitting
    globalShortcut.unregisterAll();
});

app.on('window-all-closed', () => {
    // Quit app on all platforms except macOS where apps stay active until Cmd+Q
    if (process.platform !== 'darwin') {
        app.quit();
    }
});
