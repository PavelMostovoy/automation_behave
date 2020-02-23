# Created by shevchenko at 2/23/2020
Feature: Submit email form
  # Enter feature description here

  Scenario Outline: Fill up data in the email field
    When I open website <link> using <browser>
    When I change <reply_form> and fill up <data> in <field> using <browser>
    When I press the submit <button> using <browser>
    Then I check <message> in <element> using <browser>


    Examples: Data for the "email" form verification
      | link                               | browser | reply_form                           | data                    | field                        | button              | element                            | message                               |
      | https://dev.svetlitsky.photography | chrome  | //*[@id="field-reply"]/div/button[2] | mike.wazowski.gmail.com | //*[@id="field-email"]/input | //*[@type="submit"] | //*[@id="field-email"]/label       | Please enter your valid Email address |
      | https://dev.svetlitsky.photography | chrome  | //*[@id="field-reply"]/div/button[2] | mike.wazowski@gmail.com | //*[@id="field-email"]/input | //*[@type="submit"] | //*[@id="contact-success-sent-to"] | mike.wazowski@gmail.com               |
