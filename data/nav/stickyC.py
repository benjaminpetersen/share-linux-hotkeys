# Enter script code
#dialog.info_dialog(title="any")
#keyboard.wait_for_keypress("c", modifiers=["alt"])
#sooo I guess I could use store, and set it's value, then 
"""
Then in the tags of the phrases call a script with a keypress arg... bleck.
newp. I think this should just set stickC: True || False, and all those phrases must become scripts
"""
#dialog.info_dialog(title="after")
stickyC = store.get_global_value("stickyC")
if stickyC: stickyC = False
else: stickyC = True 
store.set_global_value("stickyC", stickyC)