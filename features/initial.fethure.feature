# Created by mostovoi at 19.12.2019
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

  Scenario: Open browser
     Given Browser name Chrome
      When we implement a test
      Then behave will test it for us!