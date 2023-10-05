#!/usr/bin/env python

from selenium import selenium

sel = selenium.selenium('localhost', 4444, '*firefox',
                        'http://www.google.com/')
sel.start()
sel.open('/')
sel.wait_for_page_to_load(10000)
sel.stop()
