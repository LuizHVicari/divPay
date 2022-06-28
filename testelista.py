from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineListItem

KV = '''
ScrollView:
    MDList:
        id: container
    
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                ThreeLineListItem( text=f"Single-line item {i}",on_release= lambda x:print("click"), secondary_text="Secondary text here", tertiary_text="fit more text than usual")
            )

Test().run()

