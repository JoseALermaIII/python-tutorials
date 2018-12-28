"""Pod Bay Door

This program raises an :py:class:`AssertionError`.

Note:
    Correction submitted for line 13
"""


def main():
    podBayDoorStatus = "open"
    assert podBayDoorStatus == "open", "The pod bay doors need to be 'open'."
    podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
    assert podBayDoorStatus == "open", "The pod bay doors need to be 'open'."


if __name__ == '__main__':
    main()
