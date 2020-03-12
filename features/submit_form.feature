# Created by mostovoi at 17.02.2020
Feature: Submit form
  # Enter feature description here

  @phone_number
  Scenario Outline: Fill Data in the Phone number field

    When I open https://dev.svetlitsky.photography/ using chrome
    When I fill <data> in <field> using chrome
    When I press the <button> using chrome
    Then I verify <message> in <element> using chrome


    Examples:
     |  data      | field                        | button              | element                            | message                                      |
     | 1234567890 | //*[@id="field-email"]/input | //*[@type="submit"] | //*[@id="field-email"]/label       | Please enter your 10-digit Cell Phone Number |
     | 5509456780 | //*[@id="field-email"]/input | //*[@type="submit"] | //*[@id="contact-success-sent-to"] | 550-945-6780                                 |



  @email_form
  Scenario Outline: Fill Data in the E-mail field

      When I open https://dev.svetlitsky.photography using chrome
      When I change <reply_form> and fill up <data> in <field> using chrome
      When I press the <button> using chrome
      Then I verify <message> in <element> using chrome


    Examples: Fill Data in the e-mail field
      | reply_form                           | data                    | field                        | button              | element                            | message                               |
      | //*[@id="field-reply"]/div/button[2] | mike.wazowski.gmail.com | //*[@id="field-email"]/input | //*[@type="submit"] | //*[@id="field-email"]/label       | Please enter your valid Email address |
      | //*[@id="field-reply"]/div/button[2] | mike.wazowski@gmail.com | //*[@id="field-email"]/input | //*[@type="submit"] | //*[@id="contact-success-sent-to"] | mike.wazowski@gmail.com               |