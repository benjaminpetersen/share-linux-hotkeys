# Enter script code
stickyC=store.get_global_value('stickyC')
if stickyC: keyboard.send_keys('<alt>+<shift>+<up>')
else: keyboard.send_keys('<shift>+<up>')