"""Traffic light

This program emulates traffic lights at intersections with assertions.

Attributes:
    market_2nd (dict): Stoplight at the corner of Market and 2nd streets with
        North-South face and East-West face as keys.
    mission_16th (dict): Stoplight at the corner of Mission and 16th streets with
        North-South face and East-West face as keys.
"""

market_2nd = {"ns": "green", "ew": "red"}
mission_16th = {"ns": "red", "ew": "green"}


def switchLights(stoplight: dict) -> None:
    """Switch lights

    Takes stoplight dictionary and changes values: from 'green' to 'yellow', 'yellow'
    to 'red', and 'red' to 'green'.

    Args:
        stoplight: Dictonary representing stoplight with face directions as keys and
            status as values.

    Returns:
        None. Changes dictionary values.

    Raises:
        AssertionError: If none of the dictionary values are 'red'.
    """
    for key in stoplight.keys():
        if stoplight[key] == "green":
            stoplight[key] = "yellow"
        elif stoplight[key] == "yellow":
            stoplight[key] = "red"
        elif stoplight[key] == "red":
            stoplight[key] = "green"
    assert "red" in stoplight.values(), "Neither light is red! " + str(stoplight)


def main():
    switchLights(market_2nd)


if __name__ == '__main__':
    main()
