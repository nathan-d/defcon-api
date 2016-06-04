def get_status():
  return 'Status is working...'
  
def set_status(status):
  if status >= 0 and status <= 5:  
    resp = ("Set status to %d" % status)
  else:
    resp = "Value outside of supported range."
  return (resp)
  
def party_mode():
  if party_mode == true:
      print "Ending party mode."
      pass
  else:
      print "Starting party mode."
      pass