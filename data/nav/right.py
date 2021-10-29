# Enter script code
stickyC=store.get_global_value('stickyC')
if stickyC: keyboard.send_keys('<alt>+<right>')
keyboard.send_key('<right>')