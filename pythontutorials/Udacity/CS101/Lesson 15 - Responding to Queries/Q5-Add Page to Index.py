# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurrences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])


# Note that as written, multiple occurrences of the same word in
# the same page will be stored in the index. TODO: Update to not repeat entries
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
    return None


add_page_to_index(index, 'fake.text', "This is a test")
print(index)
# >>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
# >>> ['test',['fake.text']]]
