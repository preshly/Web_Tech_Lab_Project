
#############################
#                           #
##          Testing        ##
##      Using selenium;    ##
##         unittest        ##
#                           #
#############################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

from admin_conversation import chancellor_conversation, dean_conversation, \
    vice_chancellor_conversation, registrar_conversation, general_conversation, \
    finance_officer_conversation

from greetings_convers import greetings_conversation
# general_course_conversation
from courses_conserv import courses_conversation, bachelors_courses_conversation,\
    master_courses_conversation, mphil_courses_conversation, pgdiploma_courses_conversation, \
    doctoral_courses_conversation

from department_convers import department_conversation
from examination_conv import apply_for_conversations, convocation_conversations
from admission_conv import admission_notices_converstion

from contact_conv import contact_conversations,email_conversations

from college_convo import genral_college_conversation, general_edu_institution_convo, \
    professional_edu_institution_convo, recognised_edu_institution_convo

from academic_matter_conv import eligibility_conversations,migration_conversations,transcripts_conversations

from hostel_conves import hostel_conversation

all_convo = [greetings_conversation, chancellor_conversation, dean_conversation, vice_chancellor_conversation, 
            registrar_conversation, finance_officer_conversation, general_conversation, courses_conversation, 
            bachelors_courses_conversation, master_courses_conversation, mphil_courses_conversation, 
            pgdiploma_courses_conversation, doctoral_courses_conversation, department_conversation, 
            apply_for_conversations, convocation_conversations, admission_notices_converstion, 
            hostel_conversation, contact_conversations,email_conversations, genral_college_conversation, 
            general_edu_institution_convo, professional_edu_institution_convo, 
            recognised_edu_institution_convo, eligibility_conversations,migration_conversations,
            transcripts_conversations,
            ]

class Test_Bot_Ui(unittest.TestCase):
    '''
        class to test the chatbot ui.
        open and close the ui.
    '''

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
    
    def test_bot_ui(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/')

        chatbot_icon = driver.find_element_by_class_name('chat-bot-icon')
        # chatbot_icon_close = driver.find_element_by_class_name('feather-x')

        action = ActionChains(driver= driver)

        action.click(on_element= chatbot_icon)

        action.perform()

        time.sleep(2)

        input_element = driver.find_element_by_id('input_msg')
        input_element.send_keys('Hello')
        input_element.send_keys('\ue007') #send enter key

        # send_button = driver.find_element_by_id('send_button')
        time.sleep(2)

        action.click(on_element= chatbot_icon)
        action.perform()
        time.sleep(2)
    
    def tearDown(self) -> None:
        self.driver.close()

class Test_Conversations(unittest.TestCase):
    '''
        class to test if all the conversations are working properly or not.
    '''

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
    
    def test_convo(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/')

        chatbot_icon = driver.find_element_by_class_name('chat-bot-icon')

        action = ActionChains(driver= driver)
        action.click(on_element= chatbot_icon)
        action.perform()

        time.sleep(1)

        input_element = driver.find_element_by_id('input_msg')

        for convo in all_convo:
            i = 0
            while i < len(convo):
                input_element.send_keys(convo[i])
                input_element.send_keys('\ue007') #send enter key
                time.sleep(2)

                i += 2
            time.sleep(2)

        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

