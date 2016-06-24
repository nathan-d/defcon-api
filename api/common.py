from defcon import core
defcon = core.Defcon()


def get_status():
    return defcon.get_status()


def increment_status():
    status = defcon.get_status()
    if status > 1:
        status -= 1
        return set_status(status)
    else:
        print 'Status already at highest level.'


def decrement_status():
    status = defcon.get_status()
    if status <= 5:
        status += 1
        return set_status(status)
    else:
        print 'Status already at lowest level.'


def set_status(status):
    if status >= 0 and status <= 5:
        if defcon.save_status(status):
            resp = "Status set to %d." % status
        else:
            resp = "Any unknown error occured."
    else:
        resp = "Value outside of supported range."
    return (resp)


def party_mode():
    # defcon.party()
    return "Party mode started."
