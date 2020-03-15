# Created by mostovoi at 17.02.2020
Feature: Submit form
  # Enter feature description here


  Scenario Outline: Fill User's contact details
    Given the users
      | name | phone      | e_mail         | comments                  |
      | Alex | 5509456780 | alex@gmail.com | I leave here some message |
#      | Alex | 1234567890 | alex.gmail.com | I leave here some message |  # Checking fields for "correct" input


    When I open https://dev.svetlitsky.photography/ using chrome
    And I choose <reply_form> and fill Alex contact details in <field> using chrome
    And I leave Alex comment in <comments_field> using chrome
    And I press the <button> using chrome
    Then I verify <message> in <element> using chrome

    @phone_number
    Examples:
      | reply_form                           | field                        | comments_field                    | button              | element                            | message      |
#      | //*[@id="field-reply"]/div/button[1] | //*[@id="field-email"]/input | //*[@id="field-message"]/textarea | //*[@type="submit"] | //*[@id="field-email"]/label       | Please enter your 10-digit Cell Phone Number |    # Checking fields for "correct" input
      | //*[@id="field-reply"]/div/button[1] | //*[@id="field-email"]/input | //*[@id="field-message"]/textarea | //*[@type="submit"] | //*[@id="contact-success-sent-to"] | 550-945-6780 |

    @email_form
    Examples: Fill Data in the e-mail field
      | reply_form                           | field                        | comments_field                    | button              | element                            | message        |
#      | //*[@id="field-reply"]/div/button[2] | //*[@id="field-email"]/input | //*[@id="field-message"]/textarea | //*[@type="submit"] | //*[@id="field-email"]/label       | Please enter your valid Email address |   # Checking fields for "correct" input
      | //*[@id="field-reply"]/div/button[2] | //*[@id="field-email"]/input | //*[@id="field-message"]/textarea | //*[@type="submit"] | //*[@id="contact-success-sent-to"] | alex@gmail.com |
