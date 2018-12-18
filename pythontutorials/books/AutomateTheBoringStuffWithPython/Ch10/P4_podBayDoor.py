# This program raises an AssertionError
# Note: correction submitted for line 6

podBayDoorStatus = "open"
assert podBayDoorStatus == "open", "The pod bay doors need to be 'open'."
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == "open", "The pod bay doors need to be 'open'."
