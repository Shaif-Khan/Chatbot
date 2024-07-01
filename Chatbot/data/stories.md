## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy


## greet + show_phones
* greet
  - utter_greet
* buy_phone_laptop{"category":"phone"}
  - product_search_form
  - form{"name":"product_search_form"}
  - form{"name":null}
* goodbye
  - utter_goodbye



## greet + show_phones_featurized_slots

* greet
    - utter_greet
* buy_phone_laptop{"category":"phone"}
    - slot{"category":"phone"}
    - product_search_form
    - form{"name":"product_search_form"}
    - slot{"requested_slot":"ram"}
* goodbye
    - product_search_form
    - slot{"ram":null}
* give_information
    - product_search_form
    - slot{"ram":null}
* give_information
    - product_search_form
    - slot{"ram":8}
* give_information
    - product_search_form
    - slot{"battery":6000}
* give_information
    - product_search_form
    - slot{"camera":50}
* give_information
    - product_search_form
    - form{"name":null}
    - slot{"budget":500}
* goodbye
    - utter_goodbye
* out_of_scope
  - action_my_fallback


## greet + fallback + search + news

* greet
    - utter_greet
* goodbye
    - action_my_fallback
    - slot{"category":"laptop"}
* buy_phone_laptop{"category":"laptop"}
    - product_search_form
    - form{"name":"product_search_form"}
    - slot{"requested_slot":"ram"}
* give_information
    - product_search_form
    - slot{"ram":4}
* give_information
    - product_search_form
    - slot{"battery_backup":"10 hours"}
* give_information
    - product_search_form
    - slot{"storage_capacity":"256 GB"}
* give_information
    - product_search_form
    - form{"name":null}
    - slot{"budget":500}
* out_of_scope
    - action_my_fallback
    - slot{"category":"laptop"}
* latest_news_phones_laptops{"category":"laptop"}
    - action_show_latest_news
* goodbye
    - utter_goodbye


## greet + featurized_slots_laptops

* greet
    - utter_greet
    - slot{"category":"laptop"}
* buy_phone_laptop{"category":"laptop"}
    - product_search_form
    - form{"name":"product_search_form"}
    - slot{"requested_slot":"ram"}
* give_information
    - product_search_form
    - slot{"ram":8}
* give_information
    - product_search_form
    - slot{"battery_backup":"8 hours"}
* give_information
    - product_search_form
    - slot{"storage_capacity":"256 GB"}
* give_information
    - product_search_form
    - form{"name":null}
    - slot{"budget":800}




## greet + show_latest_news
* greet
  - utter_greet
* latest_news_phones_laptops{"category":"phone"}
  - action_show_latest_news
* goodbye
  - utter_goodbye

## out_of_scope_intent
* out_of_scope
  - action_my_fallback
  

## out_of_scope_intent
* out_of_scope
  - action_my_fallback


## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
