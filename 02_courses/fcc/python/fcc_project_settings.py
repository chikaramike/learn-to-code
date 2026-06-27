test_settings = {}
setting = ("darkmode", "on")

def add_setting(settings, setting):
    print("Setting Added")

def update_setting(settings, setting):
    print("Setting Updated")

def delete_setting(settings, setting):
    print("Setting deleted")

def view_settings(settings):
    print("Your settings are")

add_setting(test_settings, setting)
update_setting(test_settings, setting)
delete_setting(test_settings, setting)
view_settings(test_settings)
