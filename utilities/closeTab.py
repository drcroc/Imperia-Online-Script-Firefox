
def closeLastLoginsTab(driver):
    find_popups_to_close = driver.find_elements("xpath",'//*[@class="ui-ib fright close"]')
    for popups in find_popups_to_close:
        popups.click()

    # if driver.find_element("xpath",'//[@class="txt-title"]'):   <---- missing '*' in front of  the '//'
    #     driver.find_element("xpath",'//[@title="Затваряне"]').click()   <---- missing '*' in front of  the '//'
