import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from webbrowser import open as openLink

FACTOR_CODE = '0123456789'
COLOR_CODE = 'abcdefghijklmnopqrstuvwxyz'
BLANK_CODE = '.'
NEWLINE_CODE = ','

COLOR_BUTTON_SIZE = 25
BORDER_COLOR = '#cccccc'
SELECTED_COLOR = '#000000'
TRANSPARENT_COLOR_1 = '#f0f0f0'
TRANSPARENT_COLOR_2 = '#e6e6e6'

defaultWindowSize = 300
spriteWidth = 10
spriteHeight = 10
pixelSize = defaultWindowSize // max(spriteWidth, spriteHeight)
displayGrid = True

sprite = []
pallet = ['#ff0000', '#00ff00', '#0000ff']
selectedColor = 'a'
canvasPressed = 0
isSaved = True

class Scrollable(tk.Frame):
    def __init__(self, frame, width, height):
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set, width=width, height=height)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.canvas.yview)
        self.canvas.bind('<Configure>', self.fillCanvas)
        tk.Frame.__init__(self, frame)
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)
        
    def fillCanvas(self, e):
        canvas_width = e.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)

    def update(self):
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))
        self.setHeight(spriteHeight*pixelSize)

    def setHeight(self, height):
        self.canvas.config(height=height)

class ColorButton:
    def __init__(self, color):
        self.color = color
        self.frame = tk.Frame(palletScrollable, width=COLOR_BUTTON_SIZE, height=COLOR_BUTTON_SIZE, borderwidth=2)
        self.update()
        self.frame.bind('<Button-1>', self.onLeftClick)
        self.frame.bind('<Double-Button-1>', self.onDoubleLeftClick)
        self.frame.pack(pady=1)

    def update(self):
        if selectedColor == self.color:
            self.frame.config(bg=getHexColor(self.color), highlightbackground=SELECTED_COLOR, highlightthickness=2)
        else:
            self.frame.config(bg=getHexColor(self.color), highlightbackground=BORDER_COLOR, highlightthickness=1)

    def onLeftClick(self, e):
        global selectedColor
        selectedColor = self.color
        updataAllColorButtons()

    def onDoubleLeftClick(self, e):
        color = colorchooser.askcolor(getHexColor(selectedColor))[1]
        if color:
            index = COLOR_CODE.index(selectedColor)
            pallet[index] = color
            self.update()
            drawCanvas()

def createArray(c, w, h):
    array = []
    for i in range(h):
        array.append([c]*w)
    return array

def getHexColor(color):
    if color == '.':
        return
    return pallet[COLOR_CODE.index(color)]

def spriteIsEmpty():
    for row in range(spriteHeight):
        for col in range(spriteWidth):
            if sprite[row][col] != BLANK_CODE:
                return False
    return True

def drawPixel(col, row):
    color = getHexColor(sprite[row][col])
    if color:
        canvas.create_rectangle(col*pixelSize, row*pixelSize, (col+1)*pixelSize, (row+1)*pixelSize, fill=color, outline=BORDER_COLOR if displayGrid else '')
    else:
        canvas.create_rectangle(col*pixelSize, row*pixelSize, (col+1)*pixelSize, (row+1)*pixelSize, fill=TRANSPARENT_COLOR_1, outline='')
        canvas.create_rectangle(col*pixelSize, row*pixelSize, (col+0.5)*pixelSize, (row+0.5)*pixelSize, fill=TRANSPARENT_COLOR_2, outline='')
        canvas.create_rectangle((col+0.5)*pixelSize, (row+0.5)*pixelSize, (col+1)*pixelSize, (row+1)*pixelSize, fill=TRANSPARENT_COLOR_2, outline='')
        canvas.create_rectangle(col*pixelSize, row*pixelSize, (col+1)*pixelSize, (row+1)*pixelSize, outline=BORDER_COLOR if displayGrid else '')
    

def drawCanvas():
    canvas.delete('all')
    canvas.configure(width=spriteWidth*pixelSize-2, height=spriteHeight*pixelSize-2)
    for row in range(spriteHeight):
        for col in range(spriteWidth):
            drawPixel(col, row)

def removeUndefinedColor():
    global sprite
    for row in range(spriteHeight):
        for col in range(spriteWidth):
            if sprite[row][col] != BLANK_CODE and COLOR_CODE.index(sprite[row][col]) >= len(pallet):
                sprite[row][col] = BLANK_CODE
    drawCanvas()

def onCanvasPress(e):
    global canvasPressed
    canvasPressed = e.num
    onCanvasMotion(e)

def onCanvasRelease(e):
    global canvasPressed
    canvasPressed = 0

def onCanvasMotion(e):
    if canvasPressed:
        col = min(e.x // pixelSize, spriteWidth -1)
        row = min(e.y // pixelSize, spriteHeight -1)
        if canvasPressed == 1:
            paintPixel(selectedColor, col, row)
        else:
            paintPixel(BLANK_CODE, col, row)

def paintPixel(color, col, row):
    global isSaved
    sprite[row][col] = color
    drawPixel(col, row)
    isSaved = False

def updataAllColorButtons():
    for button in colorButtons:
        button.update()

def selectText(e):
    e.widget.tag_add(tk.SEL, '1.0', 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(e.widget.get('1.0', 'end-1c'))

def render():
    spriteRender = ''
    for row in range(spriteHeight):
        factor = 0
        letter = ''
        for col in range(spriteWidth +1):
            if letter != '' and (col == spriteWidth and letter != BLANK_CODE) or (col < spriteWidth and letter != sprite[row][col]):
                if factor > 1:
                    spriteRender += str(factor)
                spriteRender += letter
                factor = 0
            if col < spriteWidth:
                letter = sprite[row][col]
                factor += 1
        if row < spriteHeight -1:
            spriteRender += ','
    return spriteRender

def decode(spriteRender):
    sprite = createArray(BLANK_CODE, spriteWidth, spriteHeight)
    row = 0
    for column in spriteRender.split(NEWLINE_CODE):
        col = 0
        factorStr = '0'
        for letter in column:
            if letter in FACTOR_CODE:
                factorStr += letter
            else:
                factor = max(int(factorStr), 1)
                if letter != BLANK_CODE:
                    for i in range(factor):
                        sprite[row][col + i] = letter
                col += factor
                factorStr = '0'
        row += 1
    return sprite

def exportSprite():
    renderWindow = tk.Toplevel(root)
    renderWindow.grab_set()
    renderWindow.title('Export')
    renderWindow.transient(root)
    try: renderWindow.iconbitmap('art/favicon.ico')
    except: pass
    imageText = tk.Text(renderWindow, width=40, height=1, wrap=tk.NONE)
    imagePallet = tk.Text(renderWindow, width=40, height=1, wrap=tk.NONE)
    imageText.insert(tk.END, "'" + render() + "'")
    imagePallet.insert(tk.END, "('" + "','".join(pallet) + "')")
    imageText.config(state='disabled')
    imagePallet.config(state='disabled')
    imageText.pack(padx=10, pady=10)
    imagePallet.pack(padx=10, pady=10)
    imageText.bind('<ButtonRelease-1>', selectText)
    imagePallet.bind('<ButtonRelease-1>', selectText)

def saveSprite():
    global isSaved
    file = filedialog.asksaveasfile(initialfile='sprite.txt', defaultextension=".txt",filetypes=(("Text Documents","*.txt"),("All Files","*.*")))
    if file:
        file.write(str(spriteWidth) + ' ' + str(spriteHeight) + '\n' + render() + '\n' + ' '.join(pallet))
    isSaved = True

def openSprite():
    global spriteWidth, spriteHeight, sprite, pallet, colorButtons, isSaved
    try:
        file = filedialog.askopenfile(filetypes=(("Text Documents","*.txt"),("All Files","*.*")))
        if not file: return
        content = file.read().split('\n')
        spriteWidth, spriteHeight = map(int, content[0].split())
        newSprite = decode(content[1])
        if newSprite:
            sprite = newSprite
        pallet = content[2].split()
        zoomAdjust()
        drawCanvas()
    except:
        messagebox.showerror('Error', 'Cannot read this file.')
        root.destroy()
        return
    for button in colorButtons:
        button.frame.pack_forget()
    colorButtons = []
    for i in range(len(pallet)):
        colorButtons.append(ColorButton(COLOR_CODE[i]))
    palletScrollable.update()
    if len(pallet) == 1:
        palletMenu.entryconfig('Remove color', state='disabled')
    elif len(pallet) == len(COLOR_CODE):
        palletMenu.entryconfig('Add color', state='disabled')
    isSaved = True


def resizeCanvas():
    global sprite, spriteWidth, spriteHeight
    newWidth = simpledialog.askinteger('Resize Canvas', 'Canvas width', initialvalue=spriteWidth, minvalue=1)
    if not newWidth: return
    newHeight = simpledialog.askinteger('Resize Canvas', 'Canvas height', initialvalue=spriteHeight, minvalue=1)
    if not newHeight: return
    newSprite = createArray(BLANK_CODE, newWidth, newHeight)
    for row in range(min(newHeight, spriteHeight)):
        for col in range(min(newWidth, spriteWidth)):
            newSprite[row][col] = sprite[row][col]
    spriteWidth, spriteHeight = newWidth, newHeight
    sprite = newSprite
    zoomAdjust()
    drawCanvas()
    palletScrollable.setHeight(spriteHeight*pixelSize)

def fillCanvas():
    if spriteIsEmpty() or messagebox.askokcancel('Fill Canvas ?', 'Fill the entire canvas with the selected color ?'):
        global sprite, isSaved
        sprite = createArray(selectedColor, spriteWidth, spriteHeight)
        drawCanvas()
        isSaved = False

def clearCanvas():
    if not spriteIsEmpty() and messagebox.askokcancel('Clear Canvas ?', 'Clear the canvas ?'):
        global sprite, isSaved
        sprite = createArray(BLANK_CODE, spriteWidth, spriteHeight)
        drawCanvas()
        isSaved = True

def addColor():
    global selectedColor, isSaved
    if len(pallet) == len(COLOR_CODE): return
    pallet.append('#ffffff')
    color = COLOR_CODE[len(pallet)-1]
    colorButtons.append(ColorButton(color))
    selectedColor = color
    updataAllColorButtons()
    palletScrollable.update()
    if len(pallet) == len(COLOR_CODE):
        palletMenu.entryconfig('Add color', state='disabled')
    palletMenu.entryconfig('Remove color', state='normal')
    isSaved = False

def removeColor():
    global selectedColor, isSaved
    if len(pallet) == 1 or not messagebox.askokcancel('Remove color ?', 'Remove last color from palette ?'): return
    colorButtons.pop().frame.pack_forget()
    pallet.pop()
    removeUndefinedColor()
    palletScrollable.update()
    if COLOR_CODE.index(selectedColor) >= len(pallet):
        selectedColor = COLOR_CODE[len(pallet) - 1]
        updataAllColorButtons()
    if len(pallet) == 1:
        palletMenu.entryconfig('Remove color', state='disabled')
    palletMenu.entryconfig('Add color', state='normal')
    isSaved = False

def addZoom(zoom):
    global pixelSize
    pixelSize = max(2, pixelSize + zoom)
    drawCanvas()
    palletScrollable.setHeight(spriteHeight*pixelSize)

def zoomAdjust():
    global pixelSize
    pixelSize = defaultWindowSize // max(spriteWidth, spriteHeight)
    drawCanvas()
    palletScrollable.setHeight(spriteHeight*pixelSize)

def toggleGrid():
    global displayGrid
    displayGrid = not displayGrid
    drawCanvas()

def closing():
    action = False if isSaved else messagebox.askyesnocancel('Save ?', 'Save before exiting ?')
    if action:
        saveSprite()
    elif action == None:
        return
    root.destroy()

sprite = createArray(BLANK_CODE, spriteWidth, spriteHeight)

root = tk.Tk()
root.title('Sprites Editor')
root.resizable(width=False, height=False)
root.protocol("WM_DELETE_WINDOW", closing)
try: root.iconbitmap('art/favicon.ico')
except: pass

canvas = tk.Canvas(root)
drawCanvas()
canvas.pack(side=tk.LEFT)
canvas.bind('<Button-1>', onCanvasPress)
canvas.bind('<Button-3>', onCanvasPress)
canvas.bind('<ButtonRelease-1>', onCanvasRelease)
canvas.bind('<ButtonRelease-3>', onCanvasRelease)
canvas.bind('<Motion>', onCanvasMotion)

palletBody = tk.Frame(root)
palletBody.pack(side='right')
palletScrollable = Scrollable(palletBody, width=pixelSize, height=spriteHeight*pixelSize)
colorButtons = []
for i in range(len(pallet)):
    colorButtons.append(ColorButton(COLOR_CODE[i]))
palletScrollable.update()

menuBar = tk.Menu(root)
root.config(menu=menuBar)

fileMenu = tk.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Export', accelerator='Ctrl+E', command=exportSprite)
fileMenu.add_command(label='Save', accelerator='Ctrl+S', command=saveSprite)
fileMenu.add_command(label='Open', accelerator='Ctrl+O', command=openSprite)
fileMenu.add_separator()
fileMenu.add_command(label='GitHub project', command=lambda: openLink("https://github.com/valmontechno/Sprites-Numworks"))
shortcutsMenu = tk.Menu(menuBar, tearoff=False)
fileMenu.add_cascade(label='Shortcuts', menu=shortcutsMenu)
shortcutsMenu.add_command(label='Paint', accelerator='Left click on canvas', state='disabled')
shortcutsMenu.add_command(label='Erase', accelerator='Right click on canvas', state='disabled')
shortcutsMenu.add_command(label='Pick color', accelerator='Double click on pallet', state='disabled')
shortcutsMenu.add_command(label='Zoom', accelerator='Ctrl+ Mouse wheel', state='disabled')
fileMenu.add_separator()
fileMenu.add_command(label='Quit', accelerator='Ctrl+Q', command=closing)

displayMenu = tk.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='Display', menu=displayMenu)
displayMenu.add_command(label='Zoom adjust', accelerator='Ctrl+0', command=zoomAdjust)
displayMenu.add_command(label='Zoom in', accelerator='Ctrl++', command=lambda: addZoom(10))
displayMenu.add_command(label='Zoom out', accelerator='Ctrl+-', command=lambda: addZoom(-10))
displayMenu.add_separator()
displayMenu.add_command(label='Toggle grid', accelerator='Ctrl+G', command=toggleGrid)

canvasMenu = tk.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='Canvas', menu=canvasMenu)
canvasMenu.add_command(label='Resize canvas', command=resizeCanvas)
canvasMenu.add_separator()
canvasMenu.add_command(label='Fill canvas', command=fillCanvas)
canvasMenu.add_command(label='Clear canvas', command=clearCanvas)

palletMenu = tk.Menu(menuBar, tearoff=False)
menuBar.add_cascade(label='Pallet', menu=palletMenu)
palletMenu.add_command(label='Add color', command=addColor)
palletMenu.add_command(label='Remove color', command=removeColor)

root.bind("<Control-e>", lambda e: exportSprite())
root.bind("<Control-s>", lambda e: saveSprite())
root.bind("<Control-o>", lambda e: openSprite())
root.bind("<Control-q>", lambda e: closing())
root.bind("<Control-plus>", lambda e: addZoom(10))
root.bind("<Control-minus>", lambda e: addZoom(-10))
root.bind("<Control-0>", lambda e: zoomAdjust())
root.bind("<Control-g>", lambda e: toggleGrid())
root.bind("<Control-MouseWheel>", lambda e: addZoom( 1 if e.delta > 0 else -1))

root.mainloop()
