from typing import Any, Text, Dict,Union, List ## Datatypes

from rasa_sdk import Action, Tracker  ##
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted, FollowupAction
import re

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Calling the DB
        #calling an API
        # do anything
        #all caluculations are done
        camera = tracker.get_slot('camera')
        ram = tracker.get_slot('RAM')
        battery = tracker.get_slot('battery')

        dispatcher.utter_message(text='Here are your search results')
        dispatcher.utter_message(text='The features you entered: ' + str(camera) + ", " + str(ram) + ", " + str(battery))
        return []
########################

class ActionShowLatestNews(Action):

    def name(self) -> Text:
        return "action_show_latest_news"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Calling the DB
        #calling an API
        # do anything
        #all caluculations are done
        dispatcher.utter_message(text='Here the latest news for your category')
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/n/m/f/g34-5g-pb1v0002in-motorola-original-imagwu4rayqhgfjh.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/motorola-g34-5g-ocean-green-128-gb/p/itm6b1a33b9d9191?pid=MOBGUFK4TZ2CJYHJ&lid=LSTMOBGUFK4TZ2CJYHJPBUF6M&marketplace=FLIPKART&q=latest+mobile+5g&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=search-autosuggest&iid=dbd1c454-a5c6-4bd6-9d83-0c677dce6152.MOBGUFK4TZ2CJYHJ.SEARCH&ppt=sp&ppn=sp&ssid=nxw49y7cz40000001717998443813&qH=e8d7f823bcc7747d")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/d/h/q/m6-pro-5g-mzb0eprin-poco-original-imags3e7vewsafst.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/poco-m6-pro-5g-power-black-128-gb/p/itmef8fa46f89738?pid=MOBGRNZ3ER4N3K4F&lid=LSTMOBGRNZ3ER4N3K4FIYYGCU&marketplace=FLIPKART&q=latest+mobile+5g&store=tyy%2F4io&srno=s_1_4&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=Search&iid=dbd1c454-a5c6-4bd6-9d83-0c677dce6152.MOBGRNZ3ER4N3K4F.SEARCH&ppt=sp&ppn=sp&ssid=nxw49y7cz40000001717998443813&qH=e8d7f823bcc7747d")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/l/v/8/-original-imaghx9qudmydgc4.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/apple-iphone-14-plus-starlight-128-gb/p/itmc922ddc8af349?pid=MOBGHWFHVCB2YZYR&lid=LSTMOBGHWFHVCB2YZYRBDOEVN&marketplace=FLIPKART&q=latest+mobile+5g&store=tyy%2F4io&srno=s_1_6&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=Search&iid=dbd1c454-a5c6-4bd6-9d83-0c677dce6152.MOBGHWFHVCB2YZYR.SEARCH&ppt=sp&ppn=sp&ssid=nxw49y7cz40000001717998443813&qH=e8d7f823bcc7747d")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/n/i/w/-original-imagzk4mfg6zf2fv.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/realme-12x-5g-twilight-purple-128-gb/p/itmaa3401e5370b5?pid=MOBGYQ6BVK8HYMAG&lid=LSTMOBGYQ6BVK8HYMAGXL2LRY&marketplace=FLIPKART&q=latest+mobile+5g&store=tyy%2F4io&srno=s_1_16&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=Search&iid=dbd1c454-a5c6-4bd6-9d83-0c677dce6152.MOBGYQ6BVK8HYMAG.SEARCH&ppt=sp&ppn=sp&ssid=nxw49y7cz40000001717998443813&qH=e8d7f823bcc7747d")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/j/b/n/-original-imahyuhfzvybhaat.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/realme-p1-5g-peacock-green-128-gb/p/itmae4447062b5b5?pid=MOBGYQ6BEHHQ9H7X&lid=LSTMOBGYQ6BEHHQ9H7XUGYV7T&marketplace=FLIPKART&q=latest+mobile+5g&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=Search&iid=en_vdn-C9XwMSbDtkT34Y1puFdtD8fUd0xVys4hdAvRf4Upr754AYTLraN_1Vl883yOpkv7DNg9r4dKHpRoZmE9mvUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=sp&ppn=sp&ssid=nxw49y7cz40000001717998443813&qH=e8d7f823bcc7747d")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/computer/u/1/4/-original-imaguyt4gyzmcm9y.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/acer-swift-go-14-evo-oled-intel-core-i5-13th-gen-13500h-16-gb-512-gb-ssd-windows-11-home-sfg14-71-58ub-thin-light-laptop/p/itm0a080194d6dd1?pid=COMGZKGGAHZBA3WY&lid=LSTCOMGZKGGAHZBA3WYWOBYJC&marketplace=FLIPKART&q=latest+laptops&store=6bo%2Fb5g&srno=s_1_16&otracker=search&otracker1=search&fm=organic&iid=ace9d8e7-e54f-4114-bd23-3b33ec42d9bd.COMGZKGGAHZBA3WY.SEARCH&ppt=hp&ppn=homepage&ssid=bqlaftuxnk0000001717997900017&qH=ea5c17fe89184cb4")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/computer/e/t/j/250-g9-business-laptop-hp-original-imagwywdz8wmfbxz.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/hp-250-g9-intel-core-i3-12th-gen-1215u-8-gb-512-gb-ssd-windows-11-home-business-laptop/p/itmaeab3e70c465d?pid=COMGWYWD7GTFGFQH&lid=LSTCOMGWYWD7GTFGFQHB1QNTB&marketplace=FLIPKART&q=latest+laptops&store=6bo%2Fb5g&srno=s_1_14&otracker=search&otracker1=search&fm=organic&iid=ace9d8e7-e54f-4114-bd23-3b33ec42d9bd.COMGWYWD7GTFGFQH.SEARCH&ppt=hp&ppn=homepage&ssid=bqlaftuxnk0000001717997900017&qH=ea5c17fe89184cb4")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/computer/w/d/n/245-g8-business-laptop-hp-original-imagykcscqsk5ppk.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/hp-245g9-amd-ryzen-3-dual-core-3250u-8-gb-512-gb-ssd-windows-11-home-245-g8-business-laptop/p/itmf0a680c05d471?pid=COMGHNBG4KF5UYJH&lid=LSTCOMGHNBG4KF5UYJHYXYNO0&marketplace=FLIPKART&q=latest+laptops&store=6bo%2Fb5g&srno=s_1_10&otracker=search&otracker1=search&fm=organic&iid=ace9d8e7-e54f-4114-bd23-3b33ec42d9bd.COMGHNBG4KF5UYJH.SEARCH&ppt=hp&ppn=homepage&ssid=bqlaftuxnk0000001717997900017&qH=ea5c17fe89184cb4")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/computer/j/d/o/v15-g4-thin-and-light-laptop-lenovo-original-imagq57gsgyxxasy.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/lenovo-v15-amd-ryzen-3-quad-core-7320u-8-gb-512-gb-ssd-windows-11-home-g4-amn-1-thin-light-laptop/p/itm5819401743e27?pid=COMGPYKZAWY8UX6C&lid=LSTCOMGPYKZAWY8UX6CSCLSXL&marketplace=FLIPKART&q=latest+laptops&store=6bo%2Fb5g&spotlightTagId=BestsellerId_6bo%2Fb5g&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=ace9d8e7-e54f-4114-bd23-3b33ec42d9bd.COMGPYKZAWY8UX6C.SEARCH&ppt=sp&ppn=sp&ssid=bqlaftuxnk0000001717997900017&qH=ea5c17fe89184cb4")
        dispatcher.utter_message(image="https://rukminim2.flixcart.com/image/312/312/xif0q/computer/y/7/t/-original-imahyfx7md4ghn8v.jpeg?q=70")
        dispatcher.utter_message(text="https://www.flipkart.com/lenovo-ideapad-slim-3-intel-core-i5-13th-gen-13420h-16-gb-512-gb-ssd-windows-11-home-15irh8-thin-light-laptop/p/itm76f0e5d975817?pid=COMGVQ2YB9SU8KMF&lid=LSTCOMGVQ2YB9SU8KMF2MGQ5W&marketplace=FLIPKART&q=latest+laptops&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=en_IOmGxCh13xVxAKveZWHLHv8__qoYaGRPOLQvi2sApWs_sUOVMiV4QHvxQe6z_TqoQ4kMvNhcrdkMpQtu5qlmfvUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=hp&ppn=homepage&ssid=bqlaftuxnk0000001717997900017&qH=ea5c17fe89184cb4")
                                 
                                 
        

        dispatcher.utter_message(template='utter_select_phone')


        return []

class ProductSearchForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "product_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        if tracker.get_slot('category') == 'phone':
            return ["ram","battery","camera","budget"]
        elif tracker.get_slot('category') == 'laptop':
           return ["ram","battery_backup","storage_capacity","budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""


        return {"ram":[self.from_text()],
        "camera":[self.from_text()],
        "battery":[self.from_text()],
        "budget":[self.from_text()],
        "battery_backup":[self.from_text()],
        "storage_capacity":[self.from_text()]
        }

    def validate_battery_backup(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        # 8 | Im looking for 8 GB | 8 GB RAM
        # Im looking for ram
        try:
            battery_backup_int = int(re.findall(r'[0-9]+',value)[0])
        except:
            battery_backup_int = 500000
        #Query the DB and check the max value, that way it can be dynamic
        if battery_backup_int < 50:
            return {"ram":battery_backup_int}
        else:
            dispatcher.utter_message(template="utter_wrong_battery_backup")

            return {"battery_backup":None}


    def validate_storage_capacity(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        # 8 | Im looking for 8 GB | 8 GB RAM
        # Im looking for ram
        try:
            storage_capacity_int = int(re.findall(r'[0-9]+',value)[0])
        except:
            storage_capacity_int = 500000
        #Query the DB and check the max value, that way it can be dynamic
        if storage_capacity_int < 2000:
            return {"ram":storage_capacity_int}
        else:
            dispatcher.utter_message(template="utter_wrong_storage_capacity")

            return {"storage_capacity":None}


    def validate_ram(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        # 8 | Im looking for 8 GB | 8 GB RAM
        # Im looking for ram
        try:
            ram_int = int(re.findall(r'[0-9]+',value)[0])
        except:
            ram_int = 500000
        #Query the DB and check the max value, that way it can be dynamic
        if ram_int < 50:
            return {"ram":ram_int}
        else:
            dispatcher.utter_message(template="utter_wrong_ram")

            return {"ram":None}

    def validate_camera(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        try:
            camera_int = int(re.findall(r'[0-9]+',value)[0])
        except:
            camera_int = 500000
        #Query the DB and check the max value, that way it can be dynamic
        if camera_int < 150:
            return {"camera":camera_int}
        else:
            dispatcher.utter_message(template="utter_wrong_camera")

            return {"camera":None}

    def validate_budget(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        # i want the ram
        try:
            budget_int = int(re.findall(r'[0-9]+',value)[0])
        except:
            budget_int = 500000
        #Query the DB and check the max value, that way it can be dynamic
        if budget_int < 4000:
            return {"budget":budget_int}
        else:
            dispatcher.utter_message(template="utter_wrong_budget")

            return {"budget":None}

    def validate_battery(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""
        #4 GB RAM
        # 10 GB RAM --> integers/number from this -- 10
        #
        try:
            battery_int = int(re.findall(r'[0-9]+',value)[0])
        except:
            battery_int = 500000
        #Query the DB and check the max value, that way it can be dynamic
        if battery_int < 8000:
            return {"battery":battery_int}
        else:
            dispatcher.utter_message(template="utter_wrong_battery")

            return {"battery":None}


    
    # USED FOR DOCS: do not rename without updating in docs
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        if tracker.get_slot('category') == 'phone':
            dispatcher.utter_message(text="Please find your searched items here... Phones...")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/51Zjp5fq1EL._SX679_.jpg")
            dispatcher.utter_message(text=" https://www.amazon.com/OnePlus-Unlocked-IN2025-Version-Verizon/dp/B0874YFLW7/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/71Ns3Z6KFcL.__AC_SX300_SY300_QL70_FMwebp_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Google-Pixel-XL-Black-Unlocked/dp/B07YMG37J4/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/71hj88T5aBL._SX679_.jpg")
            dispatcher.utter_message(text="https://m.media-amazon.com/images/I/71yIGykJFNS._AC_SX679_.jpg https://www.amazon.com/Apple-iPhone-Midnight-Unlocked-Renewed/dp/B07Z4681LQ/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/51EfDWKl24L._SY741_.jpg")
            dispatcher.utter_message(text="https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B07DJHV6VZ")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/61xawbK-ZeL.__AC_SX300_SY300_QL70_FMwebp_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Samsung-Unlocked-Fingerprint-Recognition-Long-Lasting/dp/B082XXZ5K3/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/612kg3rGyYL._AC_SX679_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Apple-iPhone-XR-Fully-Unlocked/dp/B07P839TX1/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/517yha1lhVL.__AC_SX300_SY300_QL70_FMwebp_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Apple-iPhone-11-64GB-Black/dp/B07ZPKN6YR/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/71yIGykJFNS._AC_SX679_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Apple-iPhone-Midnight-Unlocked-Renewed/dp/B07Z4681LQ/")
            

             
        elif tracker.get_slot('category') == 'laptop':
            dispatcher.utter_message(text="Please find your searched items here... Laptops...")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/71wMYNf8MZL._SX679_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Dell-Inspiron-Touchscreen-Performance-Bluetooth/dp/B079ZJLMJN")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/71vvXGmdKWL._AC_SX679_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/71czGb00k5L._SX679_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Lenovo-130S-11IGM-Laptop-Celeron-Windows/dp/B07RHMBGCF/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/61cqXFT53AL._AC_SX466_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Lenovo-130S-11IGM-Laptop-Celeron-Windows/dp/B07RHMBGCF/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/81o8Tll-5-L._AC_SX679_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/VivoBook-procesador-almacenamiento-L203MA-DS04-Microsoft/dp/B07N6S4SY1/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/51qVDwRm72L._AC_SX679_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Acer-i5-10210U-802-11ax-Fingerprint-A515-54-59W2/dp/B07XPLKZ5P/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/71sesDsw95L._AC_SX679_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Port%C3%A1til-Premium-pulgadas-pantalla-t%C3%A1ctil/dp/B081SM57RY/")
            dispatcher.utter_message(image="https://m.media-amazon.com/images/I/31VLYdmz9QL._AC_.jpg")
            dispatcher.utter_message(text="https://www.amazon.com/Premium-Lenovo-IdeaPad-A6-9225-Bluetooth/dp/B081QXVBKH/")
           

        dispatcher.utter_message(template='utter_select_phone')   

        return [SlotSet('ram',None),SlotSet('camera',None),SlotSet('battery_backup',None),\
        SlotSet('battery',None),SlotSet('storage_capacity',None),SlotSet('budget',None)]        
    
class MyFallback(Action):

    def name(self) -> Text:
        return "action_my_fallback"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Calling the DB
        #calling an API
        # do anything
        #all caluculations are done
        dispatcher.utter_message(template="utter_fallback")


        return []
    
class YourResidence(Action):

    def name(self) -> Text:
        return "action_your_residence"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #Calling the DB
        #calling an API
        # do anything
        #all caluculations are done
        dispatcher.utter_message(template="utter_residence")


        return [UserUtteranceReverted(),FollowupAction(tracker.active_form.get('name'))]

