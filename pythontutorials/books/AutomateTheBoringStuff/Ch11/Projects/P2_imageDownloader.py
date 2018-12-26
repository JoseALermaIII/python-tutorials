"""Image downloader

Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting images.
You could write a program that works with any photo site that has a search feature.

Note:
    Many photo-sharing sites do not want direct download links easily accessible.
    Therefore, it is likely this script will not work in the future.

"""


def main():
    import requests, os, bs4
    from selenium import webdriver, common

    # Open Browser to photo-sharing site
    url = "https://www.flickr.com/search/?text="        # starting url
    os.makedirs("images", exist_ok=True)                # store images in ./images

    browser = webdriver.Firefox()
    browser.implicitly_wait(10)  # seconds

    # Search for category of photos
    browser.get(url + "Cats")

    # Download all images
    try:
        imageElems = browser.find_elements_by_css_selector("a.overlay")
        for element in imageElems:
            downloadUrl = element.get_attribute("href") + "sizes/o/"
            res = requests.get(downloadUrl)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, "lxml")

            imageElem = soup.select("img")  # FIXME: Last few images are not of the category

            if not imageElem:
                print("Could not find image.")
            else:
                imageUrl = imageElem[2].get("src")

                # Save image to ./images
                res = requests.get(imageUrl)
                res.raise_for_status()

                imageFile = open(os.path.join("images", os.path.basename(imageUrl)), "wb")
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

    except common.exceptions.NoSuchElementException as err:
        print("Unable to locate element: %s" % err)

    browser.close()


if __name__ == '__main__':
    main()
