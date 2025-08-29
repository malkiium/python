import tkinter as tk

class Companion:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.attributes('-topmost', True)  # Keep window always on top
        self.root.geometry("150x50+500+300")  # Set initial size and position
        self.canvas = tk.Canvas(root, width=150, height=50, bg='black')
        self.canvas.pack()
        
        self.character = self.canvas.create_text(20, 25, text="_/", font=("Arial", 20), anchor='w', fill='white')
        
        self.animations = {
            1: ["/_", "\\_"],
            -1: ["_\\", "_/"],
        }
        self.anim_index = 0
        
        self.x_pos = 10  # Initial X position inside the box
        self.speed = 3  # Speed of movement
        self.target_x = self.x_pos  # Target position
        self.direction = 1  # Initial direction
        
        self.move_character()
        
        self.canvas.bind("<Motion>", self.update_target)  # Track mouse movement inside the box
        self.root.bind("<Escape>", lambda e: self.root.destroy())  # Close on Esc
    
    def move_character(self):
        if abs(self.x_pos - self.target_x) > self.speed:
            self.direction = 1 if self.target_x > self.x_pos else -1
            self.x_pos += self.direction * self.speed
        
        self.canvas.coords(self.character, self.x_pos, 25)
        
        self.anim_index = 1 - self.anim_index  # Toggle animation frame
        self.canvas.itemconfig(self.character, text=self.animations[self.direction][self.anim_index])
        
        self.root.after(50, self.move_character)  # Repeat movement every 50ms
    
    def update_target(self, event):
        self.target_x = min(max(event.x, 10), 130)  # Keep target within bounds

if __name__ == "__main__":
    root = tk.Tk()
    app = Companion(root)
    root.mainloop()