"""Read/write JSON

This program uses :py:mod:`json` to manipulate JSON data.

"""


def main():
    import json

    # Reading JSON with the loads() Function
    stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,' \
                       '"felineIQ": null}'
    jsonDataAsPythonValue = json.loads(stringOfJsonData)
    print(jsonDataAsPythonValue)

    # Writing JSON with the dumps() Function
    pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
                   'felineIQ': None}
    stringOfJsonData = json.dumps(pythonValue)
    print(stringOfJsonData)


if __name__ == '__main__':
    main()
