# Created by mostovoi at 17.02.2020
Feature: Submit form
  # Enter feature description here

  Scenario Outline: Fill Data in the Phone number field

    When I open <link> using <browser>
    And I find <field> using <browser>
    When I fill <data> in <field> using <browser>
    When I press the <button> using <browser>
    Then I verify <message> in <element> using <browser>



    Examples:
      | link                               | browser | field                        | data       | button              | element                            | message                                      |
      | https://dev.svetlitsky.photography | chrome  | //*[@id="field-email"]/input | 1234567890 | //*[@type="submit"] | //*[@id="field-email"]/label       | Please enter your 10-digit Cell Phone Number |
      | https://dev.svetlitsky.photography | chrome  | //*[@id="field-email"]/input | 5509456780 | //*[@type="submit"] | //*[@id="contact-success-sent-to"] | 550-945-6780                                 |




