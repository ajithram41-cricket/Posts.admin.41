import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 650
FLAG_WIDTH, FLAG_HEIGHT = 250, 200
FPS = 60

# Colors
SAFFRON = (255, 153, 51)
WHITE = (255, 255, 255)
GREEN = (19, 136, 8)
NAVY_BLUE = (0, 0, 128)
BACKGROUND = (240, 240, 240)

class WavingFlag:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.stripe_height = height / 3
        self.wave_value = 0
        self.wave_speed = 0.05
        self.pole_width = 5
        self.pole_height = height + 250  # Extends below flag
        
    def update(self):
        self.wave_value += self.wave_speed
        if self.wave_value > 2 * math.pi:
            self.wave_value = 0
    
    def create_wave_stripe(self, y_offset, color):
        """Create points for a waving stripe"""
        points = []
        
        # Top edge with wave
        for x in range(0, self.width + 1, 2):
            wave_y = math.sin((x / self.width * 2 * math.pi) + self.wave_value) * 10
            points.append((self.x + x, self.y + y_offset + wave_y))
        
        # Bottom edge with wave
        for x in range(self.width, -1, -2):
            wave_y = math.sin((x / self.width * 2 * math.pi) + self.wave_value) * 10
            points.append((self.x + x, self.y + y_offset + self.stripe_height + wave_y))
        
        return points
    
    def get_wave_offset(self, x):
        """Calculate wave offset for a given x position"""
        return math.sin((x / self.width * 2 * math.pi) + self.wave_value) * 10
    
    def draw_ashoka_chakra(self, surface):
        """Draw the authentic Ashoka Chakra with proper proportions"""
        # Chakra dimensions based on flag specifications
        chakra_diameter = self.stripe_height * 0.92  # Chakra diameter approximates white band width
        chakra_radius = chakra_diameter / 2
        chakra_center_x = self.x + self.width / 2
        chakra_center_y = self.y + self.stripe_height * 1.5
        
        # Apply wave to chakra center
        wave_offset = self.get_wave_offset(self.width / 2)
        chakra_center_y += wave_offset
        
        # Chakra proportions based on construction sheet
        outer_rim_thickness = chakra_radius / 7.67  # ~6 units for radius 46
        inner_hub_radius = chakra_radius / 5.75  # ~8 units for radius 46
        spoke_thick_distance = chakra_radius / 2.875  # ~16 units from center
        
        # Draw outer rim (navy blue circle)
        outer_circle_points = []
        for i in range(120):
            angle = (2 * math.pi / 120) * i
            point_x = chakra_radius * math.cos(angle)
            point_y = chakra_radius * math.sin(angle)
            
            abs_x = (chakra_center_x + point_x) - self.x
            local_wave = self.get_wave_offset(abs_x)
            
            outer_circle_points.append((
                chakra_center_x + point_x,
                chakra_center_y + point_y + (local_wave - wave_offset) * 0.3
            ))
        
        if len(outer_circle_points) > 2:
            pygame.draw.lines(surface, NAVY_BLUE, True, outer_circle_points, int(outer_rim_thickness))
        
        # Draw 24 spokes (tapered shape)
        for i in range(24):
            spoke_angle = (2 * math.pi / 24) * i
            
            # Each spoke is tapered - wider at the middle, narrow at ends
            # Create polygon for each spoke
            spoke_points = []
            
            # Outer edge points (at rim)
            angle_offset = math.radians(5)  # ~10 degree width at thickest point
            
            # Point at outer rim (right side of spoke)
            outer_r = chakra_radius - outer_rim_thickness/2
            x1 = outer_r * math.cos(spoke_angle + angle_offset * 0.3)
            y1 = outer_r * math.sin(spoke_angle + angle_offset * 0.3)
            abs_x1 = (chakra_center_x + x1) - self.x
            wave1 = self.get_wave_offset(abs_x1)
            spoke_points.append((
                chakra_center_x + x1,
                chakra_center_y + y1 + (wave1 - wave_offset) * 0.3
            ))
            
            # Thickest point (right side)
            thick_x2 = spoke_thick_distance * math.cos(spoke_angle + angle_offset)
            thick_y2 = spoke_thick_distance * math.sin(spoke_angle + angle_offset)
            abs_x2 = (chakra_center_x + thick_x2) - self.x
            wave2 = self.get_wave_offset(abs_x2)
            spoke_points.append((
                chakra_center_x + thick_x2,
                chakra_center_y + thick_y2 + (wave2 - wave_offset) * 0.3
            ))
            
            # Inner hub point (right side)
            hub_x3 = inner_hub_radius * math.cos(spoke_angle + angle_offset * 0.5)
            hub_y3 = inner_hub_radius * math.sin(spoke_angle + angle_offset * 0.5)
            abs_x3 = (chakra_center_x + hub_x3) - self.x
            wave3 = self.get_wave_offset(abs_x3)
            spoke_points.append((
                chakra_center_x + hub_x3,
                chakra_center_y + hub_y3 + (wave3 - wave_offset) * 0.3
            ))
            
            # Inner hub point (left side)
            hub_x4 = inner_hub_radius * math.cos(spoke_angle - angle_offset * 0.5)
            hub_y4 = inner_hub_radius * math.sin(spoke_angle - angle_offset * 0.5)
            abs_x4 = (chakra_center_x + hub_x4) - self.x
            wave4 = self.get_wave_offset(abs_x4)
            spoke_points.append((
                chakra_center_x + hub_x4,
                chakra_center_y + hub_y4 + (wave4 - wave_offset) * 0.3
            ))
            
            # Thickest point (left side)
            thick_x5 = spoke_thick_distance * math.cos(spoke_angle - angle_offset)
            thick_y5 = spoke_thick_distance * math.sin(spoke_angle - angle_offset)
            abs_x5 = (chakra_center_x + thick_x5) - self.x
            wave5 = self.get_wave_offset(abs_x5)
            spoke_points.append((
                chakra_center_x + thick_x5,
                chakra_center_y + thick_y5 + (wave5 - wave_offset) * 0.3
            ))
            
            # Outer edge (left side)
            x6 = outer_r * math.cos(spoke_angle - angle_offset * 0.3)
            y6 = outer_r * math.sin(spoke_angle - angle_offset * 0.3)
            abs_x6 = (chakra_center_x + x6) - self.x
            wave6 = self.get_wave_offset(abs_x6)
            spoke_points.append((
                chakra_center_x + x6,
                chakra_center_y + y6 + (wave6 - wave_offset) * 0.3
            ))
            
            # Draw the spoke
            if len(spoke_points) > 2:
                pygame.draw.polygon(surface, NAVY_BLUE, spoke_points, 0)
        
        # Draw inner hub (solid circle)
        hub_points = []
        for i in range(60):
            angle = (2 * math.pi / 60) * i
            point_x = inner_hub_radius * math.cos(angle)
            point_y = inner_hub_radius * math.sin(angle)
            
            abs_x = (chakra_center_x + point_x) - self.x
            local_wave = self.get_wave_offset(abs_x)
            
            hub_points.append((
                chakra_center_x + point_x,
                chakra_center_y + point_y + (local_wave - wave_offset) * 0.3
            ))
        
        if len(hub_points) > 2:
            pygame.draw.polygon(surface, NAVY_BLUE, hub_points, 0)
    
    def draw_pole(self, surface):
        """Draw the flag pole"""
        # Pole dimensions
        pole_x = self.x - self.pole_width
        pole_y = self.y - 50  # Extends above flag
        pole_bottom_y = self.y + self.pole_height
        
        # Main pole (dark brown/wooden color)
        pole_color = (101, 67, 33)  # Dark brown
        pole_rect = pygame.Rect(pole_x, pole_y, self.pole_width, pole_bottom_y - pole_y)
        pygame.draw.rect(surface, pole_color, pole_rect)
        
        # Add shading to make it look 3D
        highlight_color = (130, 90, 50)  # Lighter brown
        shadow_color = (70, 47, 23)  # Darker brown
        
        # Left highlight
        pygame.draw.line(surface, highlight_color, 
                        (pole_x, pole_y), 
                        (pole_x, pole_bottom_y), 2)
        
        # Right shadow
        pygame.draw.line(surface, shadow_color, 
                        (pole_x + self.pole_width - 1, pole_y), 
                        (pole_x + self.pole_width - 1, pole_bottom_y), 2)
        
        # Pole top finial (decorative top)
        finial_radius = 8
        finial_color = (218, 165, 32)  # Golden color
        pygame.draw.circle(surface, finial_color, 
                          (pole_x + self.pole_width // 2, pole_y), 
                          finial_radius)
        
        # Add shine to finial
        shine_color = (255, 215, 0)
        pygame.draw.circle(surface, shine_color, 
                          (pole_x + self.pole_width // 2 - 3, pole_y - 3), 
                          4)
        
        # Pole base (wider base for stability)
        base_width = self.pole_width * 3
        base_height = 20
        base_x = pole_x - (base_width - self.pole_width) // 2
        base_y = pole_bottom_y
        
        # Draw base with gradient effect
        base_color = (80, 60, 40)
        pygame.draw.rect(surface, base_color, 
                        (base_x, base_y, base_width, base_height))
        pygame.draw.rect(surface, pole_color, 
                        (base_x, base_y, base_width, base_height), 2)
    
    def draw(self, surface):
        # Draw the pole first (behind the flag)
        self.draw_pole(surface)
        # Draw saffron stripe
        saffron_points = self.create_wave_stripe(0, SAFFRON)
        if len(saffron_points) > 2:
            pygame.draw.polygon(surface, SAFFRON, saffron_points)
        
        # Draw white stripe
        white_points = self.create_wave_stripe(self.stripe_height, WHITE)
        if len(white_points) > 2:
            pygame.draw.polygon(surface, WHITE, white_points)
        
        # Draw green stripe
        green_points = self.create_wave_stripe(self.stripe_height * 2, GREEN)
        if len(green_points) > 2:
            pygame.draw.polygon(surface, GREEN, green_points)
        
        # Draw the Ashoka Chakra
        self.draw_ashoka_chakra(surface)

def main():
    # Setup display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Waving Indian Flag')
    clock = pygame.time.Clock()
    
    # Create flag (positioned higher to show pole base)
    flag_x = (WIDTH - FLAG_WIDTH) // 2 + 20
    flag_y = 120
    flag = WavingFlag(flag_x, flag_y, FLAG_WIDTH, FLAG_HEIGHT)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update
        flag.update()
        
        # Draw
        screen.fill(BACKGROUND)
        flag.draw(screen)
        
        # Display title
        font = pygame.font.Font(None, 36)
        title = font.render('Waving Indian Flag', True, (50, 50, 50))
        title_rect = title.get_rect(center=(WIDTH // 2, 40))
        screen.blit(title, title_rect)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()