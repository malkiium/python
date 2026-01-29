import pygame
import cupy as cp
import random
import time
import sys

WIDTH, HEIGHT = 1900, 400
TOP_MARGIN = 20
FPS = 60
DELAY_TIME = 0.5

# Downsampling factor (number of bars to display)
DISPLAY_BARS = 1000  # Reduced for display optimization

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GPU Sort + CPU Render (Downsampled)")
font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()

# ---------- Sorting with GPU ----------
def gpu_sort(array, batch_size):
    # Transfer to GPU
    gpu_array = cp.asarray(array)
    
    # Perform sorting in batches
    batch_start = 0
    while batch_start < len(gpu_array):
        batch_end = min(batch_start + batch_size, len(gpu_array))
        gpu_array[batch_start:batch_end] = cp.sort(gpu_array[batch_start:batch_end])
        batch_start += batch_size

    # Return sorted array (still on GPU)
    return gpu_array

# ---------- Downsampling function ----------
def downsample(values, target_count):
    if len(values) <= target_count:
        return values
    step = len(values) // target_count
    return [values[i] for i in range(0, len(values), step)]

# ---------- Visualizer ----------
class Visualizer:
    def __init__(self):
        self.values = []
        self.bars = []
        self.sorted = False
        self.last_sort_time = time.time()
        self.batch_size = 1000  # Initial batch size for sorting

    def initialize_array(self, count):
        self.values = [random.uniform(10, HEIGHT - TOP_MARGIN) for _ in range(count)]
        self.bars = [(v, (0, 0, 255)) for v in self.values]
        self.sorted = False

    def draw_bars(self):
        screen.fill((255, 255, 255))
        
        # Downsample bars for display to `DISPLAY_BARS`
        downsampled_values = downsample(self.values, DISPLAY_BARS)
        bar_width = max(2, WIDTH // len(downsampled_values))

        # Draw downsampled bars
        for i, value in enumerate(downsampled_values):
            pygame.draw.rect(screen, (255, 0, 0), (int(i * bar_width), int(HEIGHT - value), int(bar_width) - 1, int(value)))

        # Only show FPS on screen (no number of bars)
        fps = font.render(f"FPS: {clock.get_fps():.2f}", True, (0, 0, 0))
        screen.blit(fps, (10, 50))

    def sort_with_gpu(self):
        # Perform sorting on GPU in batches
        self.values = gpu_sort(self.values, self.batch_size)

        # Downsample for display
        self.bars = [(v, (255, 0, 0)) for v in downsample(self.values, DISPLAY_BARS)]
        self.sorted = True
        self.last_sort_time = time.time()

# ---------- Main ----------
visualizer = Visualizer()
count = random.randint(10, 50)
visualizer.initialize_array(count)

sorting = True
running = True

while running:
    clock.tick(FPS)
    visualizer.draw_bars()
    pygame.display.flip()

    # Print the number of bars to console each loop
    print(f"Number of bars: {len(visualizer.values)}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if sorting:
        visualizer.sort_with_gpu()
        sorting = False
    elif visualizer.sorted and time.time() - visualizer.last_sort_time >= DELAY_TIME:
        count *= 2
        visualizer.initialize_array(count)
        sorting = True

pygame.quit()
sys.exit()
