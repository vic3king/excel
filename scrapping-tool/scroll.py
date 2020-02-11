import time


def scroll(driver, timeout):
    scroll_pause_time = timeout

    # wait for terms modal to popup and then click
    driver.implicitly_wait(timeout)
    stuff = driver.find_elements_by_css_selector(
        ".qc-cmp-buttons > button:nth-child(2)")
    stuff[0].click()
    time.sleep(2)

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height
