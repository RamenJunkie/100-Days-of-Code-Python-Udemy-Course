1. The Facebook login page opens in a new window. In order for our selenium code to work on the new window, we have to switch to the window in front.

In Selenium, each window has a identification handle, we can get all the window handles with:

    driver.window_handles

The above line of code returns a list of all the window handles. The first window is at position 0 e.g.

    base_window = driver.window_handles[0]

New windows that have popped out from the base_window are further down in the sequence e.g.

    fb_login_window = driver.window_handles[1]

We can switch our Selenium to target the new facebook login window by:

    driver.switch_to.window(fb_login_window)

You can print the driver.title to verify that it's the facebook login window that is currently target:

    print(driver.title)

The full code to switch to the new pop-up window is thus:

    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)

If successful the printed title should be "Facebook" and not "Tinder | Match. Chat. Date."