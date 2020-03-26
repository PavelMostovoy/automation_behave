# Created by shevchenko at 3/24/2020
Feature: Verify intro video
  # Enter feature description here

  Scenario Outline: Checking intro video playback
    When I go to https://dev.svetlitsky.photography/ using chrome
    And I pass to <next_page> and verify <url> and <title_name> using chrome
    And I press intro video play <button> using chrome
    Then I check <video_player> and verify duration and current time using chrome


    @newborn
    Examples:
      | next_page                                    | url                 | button               | title_name                 | video_player         |
      | #sec-gallery-newborn .gallery-photos > p > a | newborn-photography | #sec-intro-video > a | #sec-above-fold-newborn h1 | #featured-video-home |


    @family
    Examples:
      | next_page                                   | url                | button               | title_name                | video_player         |
      | #sec-gallery-family .gallery-photos > p > a | family-photography | #sec-intro-video > a | #sec-above-fold-family h1 | #featured-video-home |


    @maternity
    Examples:
      | next_page                                      | url                           | button               | title_name                   | video_player         |
      | #sec-gallery-maternity .gallery-photos > p > a | maternity-newborn-photography | #sec-intro-video > a | #sec-above-fold-maternity h1 | #featured-video-home |


    @smash_cake
    Examples:
      | next_page                                      | url                    | button               | title_name                   | video_player                          |
      | #sec-gallery-smashcake .gallery-photos > p > a | smash-cake-photography | #sec-intro-video > a | #sec-above-fold-smashcake h1 | #sec-intro-video > video:nth-child(1) |