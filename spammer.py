from selenium import webdriver
import time

browser = webdriver.Chrome()

frequency = 2

mobile_number ="9901488415"

for i in range(frequency):

    ###### FLIPKART ######

	browser.get('https://www.flipkart.com/account/login?ret=/')

	fnumber = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')

	fnumber.send_keys(mobile_number)

	fforgot = browser.find_element_by_link_text('Forgot?')
	
	fforgot.click()

	time.sleep(0.1)

#	###### AMAZON ######
#
#	browser.get('https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1')
#    
#	anumber = browser.find_element_by_xpath('//*[@id="ap_email"]')
#	anumber.send_keys(mobile_number)
#
#	acontinue = browser.find_element_by_id('continue')
#	acontinue.click()
#
#	agetotp = browser.find_element_by_id('auth-login-via-otp-btn')
#	agetotp.click()
#
#	# acontinue = browser.find_element_by_id('continue')
#	# acontinue.click()
#
#	time.sleep(1)

browser.quit()
