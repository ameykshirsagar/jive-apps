#!/usr/bin/env python
import gtk
import webkit
def key_press_event(widget, event) :
    if event.string == "`":
        gtk.main_quit()
window = gtk.Window()
window.fullscreen()
window.connect("key-press-event", key_press_event)
view = webkit.WebView()
view.open('file:///home/jarvis/support/index.html')
window.add(view)
window.show_all()
gtk.main()

