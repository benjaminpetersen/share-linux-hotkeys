# Enter script code
stickyC=store.get_global_value('stickyC')
if stickyC: keyboard.send_keys('<alt>+<down>')
else: keyboard.send_key('<down>')