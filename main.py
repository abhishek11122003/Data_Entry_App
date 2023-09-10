from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.button import MDFlatButton,MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDCustomBottomSheet, MDListBottomSheet
from kivy.lang import Builder
from datetime import datetime
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.toolbar import MDTopAppBar
#from kivy.storage.jsonstore import JsonStore
import os
import json
def read_or_create_json(file_path1, default_data1, file_path2, default_data2):
    """
    Check if two JSON files exist at the specified paths. If they exist, read and return their contents.
    If they don't exist, create the files with default data and return default data.

    :param file_path1: The path to the first JSON file.
    :param default_data1: Default data for the first file.
    :param file_path2: The path to the second JSON file.
    :param default_data2: Default data for the second file.
    :return: Two sets of JSON data read from or created in the files.
    """
    data1 = read_or_create_single_json(file_path1, default_data1)
    data2 = read_or_create_single_json(file_path2, default_data2)
    
    return data1, data2
def read_or_create_single_json(file_path, default_data):
    """
    Check if a JSON file exists at the specified path. If it exists, read and return its content.
    If it doesn't exist, create the file with default_data and return default_data.

    :param file_path: The path to the JSON file.
    :param default_data: Default data to write to the file if it doesn't exist.
    :return: JSON data read from or created in the file.
    """
    if os.path.exists(file_path):
        # If the file exists, read and return its content
        with open(file_path, 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}")
                data = default_data
    else:
        # If the file doesn't exist, create it with default_data
        with open(file_path, 'w') as json_file:
            json.dump(default_data, json_file, indent=4)
        data = default_data

    return data
# Example usage:
file_path1 = 'data.json'
default_data1 = []
file_path2 = 'filtered_data.json'
default_data2 = []
data1, data2 = read_or_create_json(file_path1, default_data1, file_path2, default_data2)
# Now 'data1' contains the JSON data from the first file, and 'data2' contains the JSON data from the second file.
helpstr= """
ScreenManager:
    DataEntryScreen:
    ViewSavedDataScreen:
    SearchDataScreen:
    ViewGrandTotals:
    ViewGrandTotals_filtered:
<DataEntryScreen>:
    name: 'DataEntryScreen:'
    MDScreen:
        MDNavigationLayout:
            MDScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        #padding: dp(20)
                        spacing: dp(8)
                        #pos_hint: {'center_x': 0.5}
                        MDTopAppBar:
                            pos_hint: {"top":1}
                            title:"Add New Data"
                            left_action_items:[['menu', lambda x: nav_drawer.set_state("open")]]
                            elevation: 3
                        BoxLayout:
                            orientation: 'vertical'
                            padding: dp(20)
                            spacing: dp(8)
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: None  # Disable relative width
                            width: dp(300)  # Set a fixed width (adjust as needed)
                            MDTextField:
                                id: username_field
                                hint_text: "Name"
                                helper_text: "Enter the name of the person"
                                helper_text_mode: "on_focus"
                                icon_left: "account"
                            MDTextField:
                                id: date_field
                                hint_text: "Date"
                                helper_text: "Enter today's date"
                                helper_text_mode: "on_focus"
                                on_focus: app.show_date_picker(self) if self.focus else None
                                icon_left: "calendar"
                            MDTextField:
                                id: policy_field
                                hint_text: "Policy"
                                helper_text: "Select policy type"
                                icon_left: "shield-account"
                                helper_text_mode: "on_focus"
                                on_focus: app.dropdown(self) if self.focus else None
                            MDTextField:
                                id: deposit_field
                                hint_text: "Deposit Amount"
                                helper_text: "Enter amount deposited"
                                helper_text_mode: "on_focus"
                                icon_left: "currency-inr"
                                input_filter: "float"  # Allow float (decimal) input
                            BoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(20)
                                pos_hint: {'center_x': 0.65, 'center_y': 0.5}  # Center-align horizontally
                                MDRectangleFlatButton:
                                    text: 'Submit'
                                    on_release: app.calculate_commission_and_show_bottom_sheet()
                                MDRectangleFlatButton:
                                    text: 'Clear'
                                    on_release:app.clear_field()
            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)
                ContentNavigationDrawer:
                    BoxLayout:
                        orientation: 'vertical'
                        padding: dp(0)
                        spacing: dp(8)
                        pos_hint: {'center_x': 0.5}
                        Image:
                            source:r"kisspng-data-entry-clerk-information-technology-computer-i-data-entry-5b257cc23a5259.5923551615291834262389.png"
                        MDTopAppBar:
                            pos_hint: {"top":1}
                            title:"Add New Data"
                            left_action_items:[['', lambda x: nav_drawer.set_state("open")]]
                            elevation: 3
                        ScrollView:
                            MDList:
                                OneLineIconListItem:
                                    text :"Add New"
                                    on_press: app.add_new()
                                    IconLeftWidget:
                                        icon:'android'
                                OneLineIconListItem:
                                    text :"View All"
                                    on_press: app.show_data_table()
                                    IconLeftWidget:
                                        icon:'android'
                                OneLineIconListItem:
                                    text :"Filter Data"
                                    on_press: app.open_search()
                                    IconLeftWidget:
                                        icon:'android'
<ViewSavedDataScreen>:
    name:'ViewSavedDataScreen:'
    MDScreenManager:
        MDScreen:
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(8)
<SearchDataScreen>:
    name:'SearchDataScreen:'
<ViewGrandTotals>:
    name:'ViewGrandTotals:'
    MDScreen:
        MDNavigationLayout:
            MDScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: dp(8)
                        MDTopAppBar:
                            pos_hint: {"top":1}
                            title:"Add New Data"
                            left_action_items:[['menu', lambda x: nav_drawer.set_state("open")]]
                            elevation: 3
                        BoxLayout:
                            orientation: 'vertical'
                            padding: dp(20)
                            spacing: dp(8)
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: None  # Disable relative width
                            width: dp(300)  # Set a fixed width (adjust as needed)
                            MDTextField:
                                id: grand_deposit_field
                                hint_text: "Grand Deposit Amount"
                                helper_text: "This is the grand total of deposit amount"
                                helper_text_mode: "persistent"
                                icon_left: "currency-inr"
                                readonly: True  # Set the text field to read-only
                            MDTextField:
                                id: grand_commission_field
                                hint_text: "Grand Commission"
                                helper_text: "This is the grand total of commission"
                                helper_text_mode: "persistent"
                                icon_left: "currency-inr"
                                readonly: True  # Set the text field to read-only
                            MDTextField:
                                id: grand_tax_field
                                hint_text: "Grand Tax"
                                helper_text: "This is the grand total of tax"
                                helper_text_mode: "persistent"
                                icon_left: "currency-inr"
                                readonly: True  # Set the text field to read-only
                            MDTextField:
                                id: grand_final_amount_field
                                hint_text: "Grand Final Amount"
                                helper_text: "This is the grand total of final amount"
                                helper_text_mode: "persistent"
                                icon_left: "currency-inr"
                                readonly: True  # Set the text field to read-only                            
                            BoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(20)
                                pos_hint: {'center_x': 0.85, 'center_y': 0.5}  # Center-align horizontally
                                MDRectangleFlatButton:
                                    text: 'Back'
                                    on_release: app.show_data_table()
            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)
                ContentNavigationDrawer:
                    BoxLayout:
                        orientation: 'vertical'
                        padding: dp(0)
                        spacing: dp(8)
                        pos_hint: {'center_x': 0.5}
                        Image:
                            source:r"kisspng-data-entry-clerk-information-technology-computer-i-data-entry-5b257cc23a5259.5923551615291834262389.png"
                        MDTopAppBar:
                            pos_hint: {"top":1}
                            title:"Add New Data"
                            left_action_items:[['', lambda x: nav_drawer.set_state("open")]]
                            elevation: 3
                        ScrollView:
                            MDList:
                                OneLineIconListItem:
                                    text :"Add New"
                                    on_press: app.add_new()
                                    IconLeftWidget:
                                        icon:'android'
                                OneLineIconListItem:
                                    text :"View All"
                                    on_press: app.show_data_table()
                                    IconLeftWidget:
                                        icon:'android'
                                OneLineIconListItem:
                                    text :"Filter Data"
                                    on_press: app.open_search()
                                    IconLeftWidget:
                                        icon:'android'
<ViewGrandTotals_filtered>:
    name:'ViewGrandTotals_filtered:'
    MDScreen:
        MDNavigationLayout:
            MDScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: dp(8)
                        MDTopAppBar:
                            pos_hint: {"top":1}
                            title:"Add New Data"
                            left_action_items:[['menu', lambda x: nav_drawer.set_state("open")]]
                            elevation: 3
                        BoxLayout:
                            orientation: 'vertical'
                            padding: dp(20)
                            spacing: dp(8)
                            pos_hint: {'center_x': 0.5}
                            size_hint_x: None  # Disable relative width
                            width: dp(300)  # Set a fixed width (adjust as needed)
                            MDTextField:
                                id: grand_deposit_field
                                hint_text: "Grand Deposit Amount"
                                helper_text: "Grand total of deposit amount of filteref data"
                                helper_text_mode: "persistent"
                                icon_left: "currency-inr"
                                readonly: True  # Set the text field to read-only
                            MDTextField:
                                id: grand_commission_field
                                hint_text: "Grand Commission"
                                helper_text: "Grand total of commission of filteref data"
                                helper_text_mode: "persistent"
                                icon_left: "currency-inr"
                                readonly: True  # Set the text field to read-only
                            MDTextField:
                                id: grand_tax_field
                                hint_text: "Grand Tax"
                                helper_text: "Grand total of tax of filteref data"
                                helper_text_mode: "persistent"
                                icon_left: "currency-inr"
                                readonly: True  # Set the text field to read-only
                            MDTextField:
                                id: grand_final_amount_field
                                hint_text: "Grand Final Amount"
                                helper_text: "Grand total of final amount of filteref data"
                                helper_text_mode: "persistent"
                                icon_left: "currency-inr"
                                readonly: True  # Set the text field to read-only
                            BoxLayout:
                                orientation: 'horizontal'
                                spacing: dp(20)
                                pos_hint: {'center_x': 0.85, 'center_y': 0.5}  # Center-align horizontally
                                MDRectangleFlatButton:
                                    text: 'Back'
                                    on_release: app.open_search()
            MDNavigationDrawer:
                id: nav_drawer
                radius: (0, 16, 16, 0)
                ContentNavigationDrawer:
                    BoxLayout:
                        orientation: 'vertical'
                        padding: dp(0)
                        spacing: dp(8)
                        pos_hint: {'center_x': 0.5}
                        Image:
                            source:r"kisspng-data-entry-clerk-information-technology-computer-i-data-entry-5b257cc23a5259.5923551615291834262389.png"
                        MDTopAppBar:
                            pos_hint: {"top":1}
                            title:"Add New Data"
                            left_action_items:[['', lambda x: nav_drawer.set_state("open")]]
                            elevation: 3
                        ScrollView:
                            MDList:
                                OneLineIconListItem:
                                    text :"Add New"
                                    on_press: app.add_new()
                                    IconLeftWidget:
                                        icon:'android'
                                OneLineIconListItem:
                                    text :"View All"
                                    on_press: app.show_data_table()
                                    IconLeftWidget:
                                        icon:'android'
                                OneLineIconListItem:
                                    text :"Filter Data"
                                    on_press: app.open_search()
                                    IconLeftWidget:
                                        icon:'android'        
"""
class DataEntryScreen(Screen):
    pass
# Load JSON data from file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
class ViewSavedDataScreen(Screen):
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'DataEntryScreen:'  # Switch to the desired screen
    def go_to_ViewGrandTotals(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ViewGrandTotals:'  # Switch to the desired screen
    def open_search(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'SearchDataScreen:'  # Switch to the desired screen
    def calculate_deposit_grand_total(self):
        try:
            with open("data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["deposit"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_commission_grand_total(self):
        try:
            with open("data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["commission"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_tax_grand_total(self):
        try:
            with open("data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["tax"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_final_amount_grand_total(self):
        try:
            with open("data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["deposit"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def open_bottom_sheet(self):
        bottom_sheet = MDListBottomSheet()
        data = [
            # Existing options...
            {"text": f"Grand Deposit = ₹ {self.calculate_deposit_grand_total()}", "icon": "calculator", "action": self.go_to_ViewGrandTotals},
            {"text": f"Grand Commission = ₹ {self.calculate_commission_grand_total()}", "icon": "calculator", "action": self.go_to_ViewGrandTotals},
            {"text": f"Grand Tax = ₹ {self.calculate_tax_grand_total()}", "icon": "calculator", "action": self.go_to_ViewGrandTotals},
            {"text": f"Grand Final = ₹ {self.calculate_final_amount_grand_total()}", "icon": "calculator", "action": self.go_to_ViewGrandTotals},
        ]
        for item in data:
            bottom_sheet.add_item(
                item["text"],
                #lambda x, y=item["text"]: self.bottom_sheet_callback(y),
                lambda x, y=item["text"], action=item.get("action"): self.bottom_sheet_callback(y, action),
            )
        bottom_sheet.open()
    def bottom_sheet_callback(self, option,action):
        if action is not None:
            action()  # Call the provided action if it exists
    def on_enter(self):
        # Clear the current data table
        self.clear_widgets()
        # Create a BoxLayout to hold both the MDTopAppBar and the MDDataTable
        main_layout = BoxLayout(orientation='vertical')
        # Add the MDTopAppBar to the main layout
        top_app_bar = MDTopAppBar(title="Data", left_action_items=[['arrow-left', lambda x: self.go_back()]], right_action_items=[['magnify', lambda x: self.open_search()], ['cash-register', lambda x: self.open_bottom_sheet()]])
        #button = MDFlatButton(text = "XYZ", on_release=lambda x: self.open_bottom_sheet())        
        main_layout.add_widget(top_app_bar)
        #main_layout.add_widget(button)

        # Create MDDataTable
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1.01, 0.8),
            use_pagination=True,
            check=True,
            column_data=[
                ("NAME", dp(50)),
                ("DATE", dp(30)),
                ("POLICY", dp(20)),
                ("DEPOSIT", dp(50)),
                ("COMMISSION", dp(60)),
                ("TAX", dp(60)),
                ("FINAL AMOUNT", dp(60)),
                # Add more columns based on your JSON data
            ],
            row_data = [
                # Convert JSON data into rows
                (
                    str(entry['name']), str(entry['date']), str(entry['policy']),
                    str(entry['deposit']), str(entry['commission']), str(entry['tax']),
                    str(entry['final_amount'])
                )  # Adjust keys based on your JSON structure
                for entry in data
            ]

        )
        #table.bind(on_row_press=self.on_row_press)
        #table.bind(on_check_press=self.on_check_press)
        main_layout.add_widget(table)
        # Add the main layout to the screen
        self.add_widget(main_layout)
with open('filtered_data.json', 'r') as json_file:
    data_1 = json.load(json_file)
class SearchDataScreen(Screen):
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ViewSavedDataScreen:'  # Switch to the desired screen
    def go_to_ViewGrandTotals_filtered(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ViewGrandTotals_filtered:'  # Switch to the desired screen
    def calculate_deposit_grand_total(self):
        try:
            with open("filtered_data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["deposit"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_commission_grand_total(self):
        try:
            with open("filtered_data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["commission"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_tax_grand_total(self):
        try:
            with open("filtered_data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["tax"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_final_amount_grand_total(self):
        try:
            with open("filtered_data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["final_amount"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def open_bottom_sheet(self):
        bottom_sheet = MDListBottomSheet()
        data = [
            # Existing options...
            {"text": f"Grand Deposit = ₹ {self.calculate_deposit_grand_total()}", "icon": "calculator", "action": self.go_to_ViewGrandTotals_filtered},
            {"text": f"Grand Commission = ₹ {self.calculate_commission_grand_total()}", "icon": "calculator", "action": self.go_to_ViewGrandTotals_filtered},
            {"text": f"Grand Tax = ₹ {self.calculate_tax_grand_total()}", "icon": "calculator", "action": self.go_to_ViewGrandTotals_filtered},
            {"text": f"Grand Final = ₹ {self.calculate_final_amount_grand_total()}", "icon": "calculator", "action": self.go_to_ViewGrandTotals_filtered},
        ]
        for item in data:
            bottom_sheet.add_item(
                item["text"],
                #lambda x, y=item["text"]: self.bottom_sheet_callback(y),
                lambda x, y=item["text"], action=item.get("action"): self.bottom_sheet_callback(y, action),
            )
        bottom_sheet.open()
    def bottom_sheet_callback(self, option,action):
        if action is not None:
            action()  # Call the provided action if it exists
    def filter_data(self, instance):
        policy_type = self.policy_input.text.lower()  # Get the input from the text field
        filtered_data = [entry for entry in data if entry['policy'].lower() == policy_type]
        self.update_data_table(filtered_data)
        # Save the filtered data to a new JSON file
        filtered_file_path = "filtered_data.json"
        with open(filtered_file_path, "w") as json_file:
            json.dump(filtered_data, json_file, indent=4)
    def update_data_table(self, filtered_data):
        self.clear_widgets()
        self.policy_input = MDTextField(hint_text="Enter Policy Type", multiline=False, size_hint_x= None, width = 400, pos_hint={'center_x': 0.5, 'center_y': 0.5}, icon_left= "shield-account")
        self.policy_input.bind(on_text_validate=self.filter_data)
        main_layout = BoxLayout(orientation='vertical')
        top_app_bar = MDTopAppBar(
            title="Search",
            left_action_items=[['arrow-left', lambda x: self.go_back()]],
            right_action_items=[['cash-register', lambda x: self.open_bottom_sheet()]]
        )
        main_layout.add_widget(top_app_bar)
        # Create a horizontal layout for text field and button
        input_layout = BoxLayout(orientation='horizontal', pos_hint={'center_x': 0.53, 'center_y': 0.5}, size_hint_y=None, height=dp(62))

        # Create the filtering button
        filter_button = MDIconButton(
            #text="Filter",
            icon= "magnify",
            on_release=self.filter_data,  # Associate the filtering function
            size_hint_x=None,
            width=dp(64),  # Set the width of the button
        )

        # Create the text field
        self.policy_input = MDTextField(
            hint_text="Enter Policy Type",
            multiline=False,
            size_hint_x=None,
            width=300,
            icon_left="shield-account"
        )
        self.policy_input.bind(on_text_validate=self.filter_data)

        # Add the text field and button to the input layout
        input_layout.add_widget(self.policy_input)
        input_layout.add_widget(filter_button)
        main_layout.add_widget(input_layout)
        self.data_table_layout = BoxLayout()  # Placeholder for the data table
        main_layout.add_widget(self.data_table_layout)
        self.add_widget(main_layout)
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1.1, 1),
            use_pagination=True,
            check=True,
            column_data=[
                ("NAME", dp(50)),
                ("DATE", dp(30)),
                ("POLICY", dp(20)),
                ("DEPOSIT", dp(50)),
                ("COMMISSION", dp(60)),
                ("TAX", dp(60)),
                ("FINAL AMOUNT", dp(60)),
            ],
            row_data=[
                (
                    str(entry['name']), str(entry['date']), str(entry['policy']),
                    str(entry['deposit']), str(entry['commission']), str(entry['tax']),
                    str(entry['final_amount'])
                )
                for entry in filtered_data
            ],
        )
        self.data_table_layout.add_widget(table)  # Add the data table to the layout
        #self.add_widget(main_layout)
    def on_enter(self):
        # Clear the current data table
        self.clear_widgets()
        # Create a BoxLayout to hold both the MDTopAppBar and the MDDataTable
        main_layout = BoxLayout(orientation='vertical')
        # Add the MDTopAppBar to the main layout
        top_app_bar = MDTopAppBar(title="Search", left_action_items=[['arrow-left', lambda x: self.go_back()]])#, right_action_items=[['cash-register', lambda x: self.open_bottom_sheet()]])
        #button = MDFlatButton(text = "XYZ", on_release=lambda x: self.open_bottom_sheet())        
        main_layout.add_widget(top_app_bar)
        #main_layout.add_widget(button)

        # Create a horizontal layout for text field and button
        input_layout = BoxLayout(orientation='horizontal', pos_hint={'center_x': 0.53, 'center_y': 0.5}, size_hint_y=None, height=dp(62))

        # Create the filtering button
        filter_button = MDIconButton(
            #text="Filter",
            icon= "magnify",
            on_release=self.filter_data,  # Associate the filtering function
            size_hint_x=None,
            width=dp(64),  # Set the width of the button
        )

        # Create the text field
        self.policy_input = MDTextField(
            hint_text="Enter Policy Type",
            multiline=False,
            size_hint_x=None,
            width=300,
            icon_left="shield-account"
        )
        self.policy_input.bind(on_text_validate=self.filter_data)

        # Add the text field and button to the input layout
        input_layout.add_widget(self.policy_input)
        input_layout.add_widget(filter_button)
        main_layout.add_widget(input_layout)

        # Create MDDataTable
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1.01, 0.8),
            use_pagination=True,
            check=True,
            column_data=[
                ("NAME", dp(50)),
                ("DATE", dp(30)),
                ("POLICY", dp(20)),
                ("DEPOSIT", dp(50)),
                ("COMMISSION", dp(60)),
                ("TAX", dp(60)),
                ("FINAL AMOUNT", dp(60)),
                # Add more columns based on your JSON data
            ],
            row_data=[
                # Convert JSON data into rows
                (
                    str(entry['name']), str(entry['date']), str(entry['policy']),
                    str(entry['deposit']), str(entry['commission']), str(entry['tax']),
                    str(entry['final_amount'])
                )  # Adjust keys based on your JSON structure
                for entry in data
            ],
        )
        main_layout.add_widget(table)
        # Add the main layout to the screen
        self.add_widget(main_layout)
class ContentNavigationDrawer(MDBoxLayout):
    pass
class ViewGrandTotals(Screen):
    def on_enter(self):
        self.ids.grand_deposit_field.text = f"{self.calculate_deposit_grand_total()}"
        self.ids.grand_commission_field.text = f"{self.calculate_commission_grand_total()}"
        self.ids.grand_tax_field.text = f"{self.calculate_tax_grand_total()}"
        self.ids.grand_final_amount_field.text = f"{self.calculate_final_amount_grand_total()}"
    def calculate_deposit_grand_total(self):
        try:
            with open("data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["deposit"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_commission_grand_total(self):
        try:
            with open("data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["commission"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_tax_grand_total(self):
        try:
            with open("data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["tax"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_final_amount_grand_total(self):
        try:
            with open("data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["final_amount"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
class ViewGrandTotals_filtered(Screen):
    def on_enter(self):
        self.ids.grand_deposit_field.text = f"{self.calculate_deposit_grand_total()}"
        self.ids.grand_commission_field.text = f"{self.calculate_commission_grand_total()}"
        self.ids.grand_tax_field.text = f"{self.calculate_tax_grand_total()}"
        self.ids.grand_final_amount_field.text = f"{self.calculate_final_amount_grand_total()}"
    def calculate_deposit_grand_total(self):
        try:
            with open("filtered_data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["deposit"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_commission_grand_total(self):
        try:
            with open("filtered_data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["commission"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_tax_grand_total(self):
        try:
            with open("filtered_data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["tax"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
    def calculate_final_amount_grand_total(self):
        try:
            with open("filtered_data.json", "r") as json_file:
                data_list = json.load(json_file)
                grand_total = sum(float(entry["final_amount"]) for entry in data_list)
                return grand_total
        except FileNotFoundError:
            return 0
sm = ScreenManager()
sm.add_widget(DataEntryScreen(name ='DataEntryScreen:'))
sm.add_widget(ViewSavedDataScreen(name ='ViewSavedDataScreen:'))
sm.add_widget(SearchDataScreen(name ='SearchDataScreen:'))
sm.add_widget(ViewGrandTotals(name ='ViewGrandTotals:'))
sm.add_widget(ViewGrandTotals_filtered(name ='ViewGrandTotals_filtered:'))
class CustomContent(BoxLayout):
    def __init__(self, output_text,output_text_2,output_text_3, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = "600"
        self.spacing = "10dp"
        
        self.output_label = MDTextField(text=output_text, hint_text= "Commission", size_hint_x = None, width = 400, icon_left= "currency-inr", readonly= True,pos_hint= {'center_x': 0.5, 'center_y': 0.42})
        self.output_label_2 = MDTextField(text=output_text_2, hint_text= "Tax", size_hint_x = None, width = 400, icon_left= "currency-inr", readonly= True, pos_hint= {'center_x': 0.5, 'center_y': 0.3})
        self.output_label_3 = MDTextField(text=output_text_3, hint_text= "Final Amount", size_hint_x = None, width = 400, icon_left= "currency-inr", readonly= True, pos_hint= {'center_x': 0.5, 'center_y': 0.18})

        self.close_button = MDFlatButton(text="Close", on_release=self.close_bottom_sheet, pos_hint= {'center_x': 0.5, 'center_y': 0.1})
        
        self.add_widget(self.output_label)
        self.add_widget(self.output_label_2)
        self.add_widget(self.output_label_3)
        self.add_widget(self.close_button)
    def close_bottom_sheet(self, *args):
        bottom_sheet = self.get_bottom_sheet()
        if bottom_sheet:
            bottom_sheet.dismiss()
    def get_bottom_sheet(self):
        # Traverse through parent widgets until you find the bottom sheet
        parent = self.parent
        while parent:
            if isinstance(parent, MDCustomBottomSheet):
                return parent
            parent = parent.parent
        return None
class RecordsApp(MDApp):    
    def build(self):
        self.strng = Builder.load_string(helpstr)
        self.date_picker = MDDatePicker()
        self.date_picker.bind(on_save=self.selected_date)
        self.data_entry_screen = self.strng.get_screen('DataEntryScreen:')  # Get a reference to the DataEntryScreen
        self.view_savedData_screen = self.strng.get_screen('ViewSavedDataScreen:')  # Get a reference to the DataEntryScreen
        return self.strng
    def dropdown(self,instance):
        self.menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": "Policy 1",
                "on_release": lambda x = "Policy 1": self.policy1()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Policy 2",
                "on_release": lambda x = "Policy 2": self.policy2()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Policy 3",
                "on_release": lambda x = "Policy 3": self.policy3()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Policy 4",
                "on_release": lambda x = "Policy 4": self.policy4()
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Policy 5",
                "on_release": lambda x = "Policy 5": self.policy5()
            }
        ]
        self.menu = MDDropdownMenu(
            caller=self.data_entry_screen.ids.policy_field,  # Access policy_field from data_entry_screen
            items = self.menu_list,
            width_mult = 4
        )
        self.menu.open()
    def policy1(self):
        self.data_entry_screen.ids.policy_field.text = "Policy 1"
        self.menu.dismiss()
    def policy2(self):
        self.data_entry_screen.ids.policy_field.text = "Policy 2"
        self.menu.dismiss()
    def policy3(self):
        self.data_entry_screen.ids.policy_field.text = "Policy 3"
        self.menu.dismiss()
    def policy4(self):
        self.data_entry_screen.ids.policy_field.text = "Policy 4"
        self.menu.dismiss()
    def policy5(self):
        self.data_entry_screen.ids.policy_field.text = "Policy 5"
        self.menu.dismiss()
    def show_date_picker(self, instance):
        self.date_picker.open()
    def selected_date(self, instance, value, touch):
        selected_date = datetime(value.year, value.month, value.day)
        #print("Selected Date:", selected_date)
        # Access the date_field widget from the DataEntryScreen instance and update its text
        self.data_entry_screen.ids.date_field.text = selected_date.strftime('%d-%m-%Y')
    def clear_field(self):
        # Access the policy_field widget and set its text to "Hello"
        self.data_entry_screen.ids.username_field.text = ""
        self.data_entry_screen.ids.date_field.text = ""
        self.data_entry_screen.ids.policy_field.text = ""
        self.data_entry_screen.ids.deposit_field.text = ""
    def calculate_commission_and_show_bottom_sheet(self):
        deposit_text = self.data_entry_screen.ids.deposit_field.text
        if deposit_text is None:
            print("deposit_text is not assigned")
            return
        try:
            deposit = float(self.data_entry_screen.ids.deposit_field.text)
            commission = deposit * 0.005
            tax = commission * 0.05
            final_amount = commission - tax

            # Create a dictionary to store the data
            data = {
                "name": self.data_entry_screen.ids.username_field.text,
                "date": self.data_entry_screen.ids.date_field.text,
                "policy": self.data_entry_screen.ids.policy_field.text,
                "deposit": deposit,
                "commission": commission,
                "tax": tax,
                "final_amount": final_amount
            }

            try:
                # Read existing data from JSON file
                with open("data.json", "r") as json_file:
                    data_list = json.load(json_file)
            except FileNotFoundError:
                # If the file doesn't exist yet, initialize with an empty list
                data_list = []

            # Append the data dictionary to the list
            data_list.append(data)

            # Save the updated data list back to the JSON file
            with open("data.json", "w") as json_file:
                json.dump(data_list, json_file, indent=4)

            # Display the bottom sheet
            output_text = f"{commission}"
            output_text_2 = f"{tax}"
            output_text_3 = f"{final_amount}"
            content = CustomContent(output_text, output_text_2, output_text_3)
            bottom_sheet = MDCustomBottomSheet(screen=content)
            bottom_sheet.open()
            # Update the data table in the ViewSavedDataScreen
            view_saved_data_screen = self.strng.get_screen('ViewSavedDataScreen:')
            view_saved_data_screen.on_enter()
        except ValueError:
            print("Invalid input for deposit amount")
    def show_data_table(self):
        self.root.transition.direction = 'left'
        self.root.current = 'ViewSavedDataScreen:'
    def open_search(self):
        self.root.transition.direction = 'left'
        self.root.current = 'SearchDataScreen:'  # Switch to the desired screen
    def add_new(self):
        self.root.transition.direction = 'left'
        self.root.current = 'DataEntryScreen:'
RecordsApp().run()
