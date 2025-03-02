import tkinter as tk
import random

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20

class PySnake:
    def __init__(self, root):
        self.root = root
        self.root.title("PySnake")
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.high_score = 0
        self.reset_game()
        
        self.root.bind("<KeyPress>", self.change_direction)
        self.update()
    
    def reset_game(self):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.spawn_food()
        self.direction = "Right"
        self.score = 0
    
    def spawn_food(self):
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        return (x, y)
    
    def change_direction(self, event):
        directions = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        if event.keysym in directions and directions[event.keysym] != self.direction:
            self.direction = event.keysym
    
    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == "Left":
            x -= CELL_SIZE
        elif self.direction == "Right":
            x += CELL_SIZE
        elif self.direction == "Up":
            y -= CELL_SIZE
        elif self.direction == "Down":
            y += CELL_SIZE
        
        new_head = (x, y)
        if new_head in self.snake or x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:
            self.game_over()
            return
        
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 10
            self.high_score = max(self.high_score, self.score)
        else:
            self.snake.pop()
    
    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH//2, HEIGHT//2 - 20, text="Game Over", fill="red", font=("Arial", 24))
        self.canvas.create_text(WIDTH//2, HEIGHT//2 + 20, text=f"High Score: {self.high_score}", fill="white", font=("Arial", 16))
        self.root.after(2000, self.reset_game)
    
    def update(self):
        self.move_snake()
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + CELL_SIZE, self.food[1] + CELL_SIZE, fill="red")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + CELL_SIZE, segment[1] + CELL_SIZE, fill="green")
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", font=("Arial", 12))
        self.canvas.create_text(450, 10, text=f"High Score: {self.high_score}", fill="yellow", font=("Arial", 12))
        self.after_id = self.root.after(100, self.update)

root = tk.Tk()
PySnake(root)
root.mainloop()
