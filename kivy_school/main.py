from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class SayHello(App):
    def build(self):
        self.window = GridLayout(cols=1, size_hint=(0.6, 0.7), pos_hint={"center_x": 0.5, "center_y": 0.5})

        #background color
        Window.clearcolor = (0, 0, 0, 1)  

        # Hello image 
        self.img1 = Image(source='download.png', size_hint=(0.6, None), pos_hint={"center_x": 0.5, "center_y": 0.5}, size=(400, 400))
        self.window.add_widget(self.img1)
        
        # Label
        self.greeting = Label(
            text="On a scale of 1-5, what is your stress level?", 
            font_size=45,
            color=(0.63, 0.01, 0.35, 1)  
        )
        self.window.add_widget(self.greeting)
        
        # Input
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.user)
        
        #button
        self.button = Button(
            text="REPORT",
            size_hint=(1, 0.5),
            bold=True,
            background_color=(0.63, 0.01, 0.35, 1),
            background_normal=""
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window
    
   #callback
    def callback(self, instance):
        user_input = self.user.text
        
        if user_input.isdigit():
            if 1 <= int(user_input) <= 5:
                self.greeting.text = f"Your stress level is {user_input}!"
                self.stress_level = int(user_input)  
                self.change_to_genre_question()
            else:
                self.greeting.text = "Please enter a number between 1 and 5."
        else:
            self.greeting.text = "Oops! Please enter a valid number."
    
    def change_to_genre_question(self):
        #clear
        self.window.clear_widgets()
        
        # Image 
        self.img1 = Image(source='download.png', size_hint=(0.6, None), pos_hint={"center_x": 0.5, "center_y": 0.5}, size=(400, 400))
        self.window.add_widget(self.img1)
        
        #label
        self.greeting = Label(
            text="What is your favorite genre from this list: \nfantasy, romance, horror, sci-fi, mystery, thriller, comedy, or murder mystery?",
            font_size=45,
            color=(0.63, 0.01, 0.35, 1)  
        )
        self.window.add_widget(self.greeting)
        
        # new input
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.user)
        
        # new button
        self.button = Button(
            text="REPORT",
            size_hint=(1, 0.5),
            bold=True,
            background_color=(0.63, 0.01, 0.35, 1),
            background_normal=""
        )
        self.button.bind(on_press=self.callback_genre)
        self.window.add_widget(self.button)

    def callback_genre(self, instance):
        user_input = self.user.text.strip().lower()
        genres = ["fantasy", "romance", "horror", "sci-fi", "mystery", "thriller", "comedy", "murder mystery"]
        
        if user_input in genres:
            self.genre = user_input
            self.greeting.text = "Got it!"
            self.greeting.font_size = 55
            self.recommend_book()
        else:
            self.greeting.text = "Please enter a valid genre!"
            self.greeting.font_size = 55

    def recommend_book(self):
        # clear widgets
        self.window.clear_widgets()

        # Book recommendations based on stress level and genre
        recommendations = {
            "fantasy": ["The Hobbit", "Harry Potter", "Mistborn", "A Game of Thrones", "The Name of the Wind"],
            "romance": ["Pride and Prejudice", "Outlander", "Me Before You", "The Notebook", "Twilight"],
            "horror": ["The Shining", "It", "Dracula", "Bird Box", "The Haunting of Hill House"],
            "sci-fi": ["Dune", "Ender's Game", "The Martian", "Neuromancer", "Foundation"],
            "mystery": ["Gone Girl", "Sherlock Holmes", "The Girl with the Dragon Tattoo", "Big Little Lies", "In the Woods"],
            "thriller": ["The Girl on the Train", "The Da Vinci Code", "The Silent Patient", "Before I Go to Sleep", "The Woman in the Window"],
            "comedy": ["Good Omens", "Bossypants", "The Hitchhiker's Guide to the Galaxy", "Yes Please", "Catch-22"],
            "murder mystery": ["Murder on the Orient Express", "The Hound of the Baskervilles", "The ABC Murders", "The Cuckoo's Calling", "In the Woods"]
        }

        book = recommendations[self.genre][self.stress_level - 1]

        #new label
        self.greeting = Label(
            text=f"We recommend you read: '{book}'",
            font_size=45,
            color=(0.63, 0.01, 0.35, 1)  
        )
        self.window.add_widget(self.greeting)

# Run the app
if __name__ == "__main__":
    SayHello().run()
