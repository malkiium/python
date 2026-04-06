import tkinter as tk
from tkinter import messagebox
import torch
import torch.nn as nn
from PIL import Image, ImageDraw
import torchvision.transforms as transforms

# Define the neural network class
class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = x.view(-1, 28 * 28)  # Flatten the image
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Load the trained model
model = NeuralNet()
model.load_state_dict(torch.load('mnist_model.pth'))  # Load the saved model
model.eval()

# Define the transform to match the MNIST preprocessing
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

# Tkinter GUI for drawing
class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Handwritten Digit Recognition")
        
        # Set up the canvas to draw
        self.canvas = tk.Canvas(self.root, width=280, height=280, bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
        # Image preparation for prediction
        self.image = Image.new("L", (28, 28), color=255)
        self.draw = ImageDraw.Draw(self.image)
        
        # Clear button
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.grid(row=1, column=0, pady=10)
        
        # Label to display the prediction
        self.prediction_label = tk.Label(self.root, text="Prediction: ?", font=("Arial", 16))
        self.prediction_label.grid(row=2, column=0, pady=10)
    
    def paint(self, event):
        # Draw on the canvas
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=10)
        
        # Draw on the image as well
        self.draw.line([x1, y1, x2, y2], fill="black", width=10)
    
    def on_release(self, event):
        # Once the user releases the mouse, predict the digit
        self.predict_digit()
    
    def clear_canvas(self):
        # Clear the canvas and image
        self.canvas.delete("all")
        self.image = Image.new("L", (28, 28), color=255)
        self.draw = ImageDraw.Draw(self.image)
        self.prediction_label.config(text="Prediction: ?")
    
    def predict_digit(self):
        # Resize the drawn image to 28x28
        img_resized = self.image.resize((28, 28), Image.Resampling.LANCZOS).convert('L')
        
        # Convert the image to tensor
        img_tensor = transform(img_resized).unsqueeze(0)  # Add batch dimension
        
        # Predict using the trained model
        with torch.no_grad():
            output = model(img_tensor)
            _, predicted = torch.max(output, 1)
        
        # Update the label with the predicted digit
        self.prediction_label.config(text=f"Prediction: {predicted.item()}")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DigitRecognizerApp(root)
    root.mainloop()
