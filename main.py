from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from database import init_db, save_timestamp, get_last_timestamp


class MobileAssistant(App):

    def build(self):
        init_db()

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        last_time = get_last_timestamp()
        self.label = Label(
            text=f"Last Recorded Time:\n{last_time}",
            halign="center"
        )

        btn = Button(
            text="Save Current Time to Memory",
            size_hint=(1, 0.3),
            background_color=(0, 0.5, 1, 1),
        )
        btn.bind(on_press=self.record_time)

        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def record_time(self, instance):
        now = datetime.now().strftime("%I:%M:%S %p (%Y-%m-%d)")
        
        save_timestamp(now)
        
        self.label.text = f"Saved to Database:\n{now}"


if __name__ == "__main__":
    MobileAssistant().run()
