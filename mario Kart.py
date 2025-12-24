"""
Mario Kart - Jeu de course simplifié
Contrôles: Flèches gauche/droite pour tourner, Flèche haut pour accélérer, Flèche bas pour freiner
"""

import tkinter as tk
import random
import math

class MarioKart:
    def __init__(self, root):
        self.root = root
        self.root.title("Mario Kart 🏎️")
        self.root.resizable(False, False)
        
        # Dimensions
        self.width = 800
        self.height = 600
        
        # Canvas
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='#228B22')
        self.canvas.pack()
        
        # Variables du jeu
        self.game_running = False
        self.score = 0
        self.coins = 0
        self.total_coins = 0  # Pièces totales collectées (persistent)
        self.speed = 0
        self.max_speed = 8
        self.player_x = self.width // 2
        self.player_y = self.height - 100
        self.player_angle = 0
        
        # Voitures disponibles
        self.cars = {
            'Mario': {'color': 'red', 'speed': 8, 'cost': 0},
            'Luigi': {'color': 'green', 'speed': 7.5, 'cost': 50},
            'Peach': {'color': 'pink', 'speed': 7, 'cost': 100},
            'Bowser': {'color': 'orange', 'speed': 9, 'cost': 150},
            'Yoshi': {'color': 'lime', 'speed': 8.5, 'cost': 200},
            'Toad': {'color': 'blue', 'speed': 7, 'cost': 250}
        }
        self.selected_car = 'Mario'
        self.unlocked_cars = ['Mario']  # Mario est débloqué par défaut
        
        # Obstacles (autres voitures)
        self.obstacles = []
        self.obstacle_speed = 3
        
        # Pièces à collecter
        self.coins_on_road = []
        
        # Route
        self.road_offset = 0
        self.road_width = 300
        self.road_x = (self.width - self.road_width) // 2
        
        # Touches pressées
        self.keys = {'Left': False, 'Right': False, 'Up': False, 'Down': False}
        
        # Éléments visuels
        self.player = None
        self.score_text = None
        self.speed_text = None
        
        # Bind des touches
        self.root.bind('<KeyPress>', self.key_press)
        self.root.bind('<KeyRelease>', self.key_release)
        
        # Menu de démarrage
        self.show_main_menu()
        
    def show_main_menu(self):
        """Affiche le menu principal"""
        self.canvas.delete('all')
        
        # Titre
        self.canvas.create_text(
            self.width // 2, 80,
            text="🏎️ MARIO KART 🏎️",
            font=('Arial', 48, 'bold'),
            fill='red'
        )
        
        # Afficher les pièces totales
        self.canvas.create_text(
            self.width // 2, 150,
            text=f"💰 Pièces totales: {self.total_coins}",
            font=('Arial', 24, 'bold'),
            fill='gold'
        )
        
        # Boutons
        btn_y = 220
        
        # Bouton Jouer
        self.create_button(self.width // 2, btn_y, "JOUER", 
                          lambda: self.show_car_selection(), 'green')
        
        # Bouton Garage
        self.create_button(self.width // 2, btn_y + 70, "GARAGE", 
                          lambda: self.show_garage(), 'blue')
        
        # Instructions
        instructions = [
            "Contrôles:",
            "← → : Tourner  |  ↑ : Accélérer  |  ↓ : Freiner",
            "Collectez des pièces 💰 et évitez les obstacles !"
        ]
        
        y = 420
        for line in instructions:
            self.canvas.create_text(
                self.width // 2, y,
                text=line,
                font=('Arial', 14),
                fill='white'
            )
            y += 30
    
    def create_button(self, x, y, text, command, color='gray'):
        """Crée un bouton cliquable"""
        width = 200
        height = 50
        
        # Rectangle du bouton
        btn_rect = self.canvas.create_rectangle(
            x - width//2, y - height//2,
            x + width//2, y + height//2,
            fill=color, outline='white', width=3
        )
        
        # Texte du bouton
        btn_text = self.canvas.create_text(
            x, y,
            text=text,
            font=('Arial', 20, 'bold'),
            fill='white'
        )
        
        # Bind du clic
        self.canvas.tag_bind(btn_rect, '<Button-1>', lambda e: command())
        self.canvas.tag_bind(btn_text, '<Button-1>', lambda e: command())
        
        return btn_rect, btn_text
    
    def show_car_selection(self):
        """Affiche l'écran de sélection de voiture"""
        self.canvas.delete('all')
        
        # Titre
        self.canvas.create_text(
            self.width // 2, 50,
            text="Choisissez votre voiture",
            font=('Arial', 32, 'bold'),
            fill='white'
        )
        
        # Afficher les voitures
        x_start = 100
        y = 150
        col = 0
        
        for car_name, car_info in self.cars.items():
            x = x_start + (col * 250)
            
            # Cadre de la voiture
            is_unlocked = car_name in self.unlocked_cars
            is_selected = car_name == self.selected_car
            
            border_color = 'yellow' if is_selected else ('white' if is_unlocked else 'gray')
            
            self.canvas.create_rectangle(
                x - 80, y - 60,
                x + 80, y + 100,
                outline=border_color, width=3,
                fill='#333333'
            )
            
            # Nom de la voiture
            self.canvas.create_text(
                x, y - 30,
                text=car_name,
                font=('Arial', 16, 'bold'),
                fill='white'
            )
            
            # Dessin de la voiture
            self.draw_car(x, y + 10, car_info['color'], 0)
            
            # Vitesse
            self.canvas.create_text(
                x, y + 50,
                text=f"Vitesse: {car_info['speed']}",
                font=('Arial', 12),
                fill='lightblue'
            )
            
            # Prix ou Sélectionné
            if is_unlocked:
                if not is_selected:
                    btn = self.canvas.create_text(
                        x, y + 75,
                        text="Sélectionner",
                        font=('Arial', 12, 'bold'),
                        fill='lime'
                    )
                    self.canvas.tag_bind(btn, '<Button-1>', 
                                        lambda e, c=car_name: self.select_car(c))
                else:
                    self.canvas.create_text(
                        x, y + 75,
                        text="✓ SÉLECTIONNÉ",
                        font=('Arial', 12, 'bold'),
                        fill='yellow'
                    )
            else:
                cost_text = f"💰 {car_info['cost']}"
                btn = self.canvas.create_text(
                    x, y + 75,
                    text=cost_text,
                    font=('Arial', 12, 'bold'),
                    fill='gold' if self.total_coins >= car_info['cost'] else 'red'
                )
                if self.total_coins >= car_info['cost']:
                    self.canvas.tag_bind(btn, '<Button-1>', 
                                        lambda e, c=car_name: self.buy_car(c))
            
            col += 1
            if col >= 3:
                col = 0
                y += 200
        
        # Bouton Retour
        self.create_button(150, self.height - 50, "← RETOUR", 
                          lambda: self.show_main_menu(), 'gray')
        
        # Bouton Commencer
        self.create_button(self.width - 150, self.height - 50, "COMMENCER →", 
                          lambda: self.start_game(), 'green')
    
    def show_garage(self):
        """Affiche le garage (boutique)"""
        self.show_car_selection()
    
    def select_car(self, car_name):
        """Sélectionne une voiture"""
        self.selected_car = car_name
        self.show_car_selection()
    
    def buy_car(self, car_name):
        """Achète une voiture"""
        cost = self.cars[car_name]['cost']
        if self.total_coins >= cost:
            self.total_coins -= cost
            self.unlocked_cars.append(car_name)
            self.selected_car = car_name
            self.show_car_selection()
        
    def show_start_menu(self):
        """Affiche le menu de démarrage (obsolète, remplacé par show_main_menu)"""
        self.show_main_menu()
        
    def start_game(self):
        """Démarre le jeu"""
        self.canvas.unbind('<Button-1>')
        self.game_running = True
        self.score = 0
        self.coins = 0  # Pièces de la partie actuelle
        self.speed = 3
        self.obstacles = []
        self.coins_on_road = []
        self.player_x = self.width // 2
        self.player_angle = 0
        
        # Appliquer la vitesse max de la voiture sélectionnée
        self.max_speed = self.cars[self.selected_car]['speed']
        
        self.draw_game()
        self.game_loop()
        
    def draw_game(self):
        """Dessine tous les éléments du jeu"""
        self.canvas.delete('all')
        
        # Herbe sur les côtés
        self.canvas.create_rectangle(0, 0, self.road_x, self.height, fill='#228B22')
        self.canvas.create_rectangle(self.road_x + self.road_width, 0, self.width, self.height, fill='#228B22')
        
        # Route
        self.canvas.create_rectangle(
            self.road_x, 0,
            self.road_x + self.road_width, self.height,
            fill='#555555'
        )
        
        # Lignes de route
        line_height = 40
        line_gap = 20
        num_lines = (self.height // (line_height + line_gap)) + 2
        
        for i in range(num_lines):
            y = (i * (line_height + line_gap) + self.road_offset) % (self.height + line_height + line_gap)
            self.canvas.create_rectangle(
                self.width // 2 - 5, y,
                self.width // 2 + 5, y + line_height,
                fill='yellow'
            )
        
        # Pièces sur la route
        for coin in self.coins_on_road:
            self.draw_coin(coin['x'], coin['y'])
        
        # Joueur (voiture du personnage sélectionné)
        player_color = self.cars[self.selected_car]['color']
        self.draw_car(self.player_x, self.player_y, player_color, self.player_angle)
        
        # Obstacles
        for obs in self.obstacles:
            self.draw_car(obs['x'], obs['y'], obs['color'], 0)
        
        # Score et vitesse
        self.canvas.create_text(
            10, 10,
            text=f"Score: {self.score}",
            font=('Arial', 20, 'bold'),
            fill='white',
            anchor='nw'
        )
        
        # Pièces collectées
        self.canvas.create_text(
            10, 40,
            text=f"💰 Pièces: {self.coins}",
            font=('Arial', 20, 'bold'),
            fill='gold',
            anchor='nw'
        )
        
        self.canvas.create_text(
            self.width - 10, 10,
            text=f"Vitesse: {int(self.speed)}",
            font=('Arial', 20, 'bold'),
            fill='white',
            anchor='ne'
        )
        
        # Nom de la voiture
        self.canvas.create_text(
            self.width - 10, 40,
            text=f"🏎️ {self.selected_car}",
            font=('Arial', 16),
            fill='lightblue',
            anchor='ne'
        )
    
    def draw_coin(self, x, y):
        """Dessine une pièce"""
        # Pièce dorée
        self.canvas.create_oval(
            x - 12, y - 12,
            x + 12, y + 12,
            fill='gold', outline='orange', width=2
        )
        
        # Symbole sur la pièce
        self.canvas.create_text(
            x, y,
            text="$",
            font=('Arial', 14, 'bold'),
            fill='orange'
        )
        
    def draw_car(self, x, y, color, angle=0):
        """Dessine une voiture"""
        car_width = 30
        car_height = 50
        
        # Corps de la voiture
        points = [
            x - car_width//2, y - car_height//2,
            x + car_width//2, y - car_height//2,
            x + car_width//2, y + car_height//2,
            x - car_width//2, y + car_height//2
        ]
        
        if angle != 0:
            # Rotation pour le joueur
            points = self.rotate_points(points, x, y, angle)
        
        self.canvas.create_polygon(points, fill=color, outline='black', width=2)
        
        # Fenêtre
        window_points = [
            x - car_width//3, y - car_height//3,
            x + car_width//3, y - car_height//3,
            x + car_width//3, y - car_height//6,
            x - car_width//3, y - car_height//6
        ]
        
        if angle != 0:
            window_points = self.rotate_points(window_points, x, y, angle)
        
        self.canvas.create_polygon(window_points, fill='lightblue', outline='black')
        
    def rotate_points(self, points, cx, cy, angle):
        """Fait pivoter des points autour d'un centre"""
        rad = math.radians(angle)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        
        rotated = []
        for i in range(0, len(points), 2):
            x = points[i] - cx
            y = points[i + 1] - cy
            
            new_x = x * cos_a - y * sin_a + cx
            new_y = x * sin_a + y * cos_a + cy
            
            rotated.extend([new_x, new_y])
        
        return rotated
        
    def key_press(self, event):
        """Gère les touches pressées"""
        if event.keysym in self.keys:
            self.keys[event.keysym] = True
            
    def key_release(self, event):
        """Gère les touches relâchées"""
        if event.keysym in self.keys:
            self.keys[event.keysym] = False
            
    def update_player(self):
        """Met à jour la position du joueur"""
        # Accélération/Freinage
        if self.keys['Up']:
            self.speed = min(self.speed + 0.3, self.max_speed)
        elif self.keys['Down']:
            self.speed = max(self.speed - 0.5, 1)
        else:
            # Décélération naturelle
            if self.speed > 3:
                self.speed -= 0.1
        
        # Rotation
        turn_speed = 5
        if self.keys['Left']:
            self.player_angle = max(self.player_angle - turn_speed, -30)
            self.player_x -= self.speed * 0.5
        elif self.keys['Right']:
            self.player_angle = min(self.player_angle + turn_speed, 30)
            self.player_x += self.speed * 0.5
        else:
            # Retour à 0
            if self.player_angle > 0:
                self.player_angle = max(0, self.player_angle - 3)
            elif self.player_angle < 0:
                self.player_angle = min(0, self.player_angle + 3)
        
        # Limites de la route
        margin = 15
        self.player_x = max(self.road_x + margin, min(self.player_x, self.road_x + self.road_width - margin))
        
    def update_obstacles(self):
        """Met à jour les obstacles"""
        # Déplacer les obstacles
        for obs in self.obstacles[:]:
            obs['y'] += self.speed + self.obstacle_speed
            
            # Supprimer si hors écran
            if obs['y'] > self.height + 50:
                self.obstacles.remove(obs)
                self.score += 10
        
        # Ajouter de nouveaux obstacles
        if random.random() < 0.02:
            colors = ['blue', 'green', 'yellow', 'purple', 'orange']
            lane = random.choice([-60, 0, 60])
            self.obstacles.append({
                'x': self.width // 2 + lane,
                'y': -50,
                'color': random.choice(colors)
            })
    
    def update_coins(self):
        """Met à jour les pièces sur la route"""
        # Déplacer les pièces
        for coin in self.coins_on_road[:]:
            coin['y'] += self.speed + self.obstacle_speed
            
            # Supprimer si hors écran
            if coin['y'] > self.height + 50:
                self.coins_on_road.remove(coin)
        
        # Ajouter de nouvelles pièces
        if random.random() < 0.03:  # Fréquence d'apparition
            lane = random.choice([-60, -30, 0, 30, 60])
            self.coins_on_road.append({
                'x': self.width // 2 + lane,
                'y': -30
            })
    
    def check_coin_collection(self):
        """Vérifie si le joueur collecte des pièces"""
        player_rect = {
            'left': self.player_x - 20,
            'right': self.player_x + 20,
            'top': self.player_y - 30,
            'bottom': self.player_y + 30
        }
        
        for coin in self.coins_on_road[:]:
            coin_rect = {
                'left': coin['x'] - 12,
                'right': coin['x'] + 12,
                'top': coin['y'] - 12,
                'bottom': coin['y'] + 12
            }
            
            if (player_rect['left'] < coin_rect['right'] and
                player_rect['right'] > coin_rect['left'] and
                player_rect['top'] < coin_rect['bottom'] and
                player_rect['bottom'] > coin_rect['top']):
                self.coins_on_road.remove(coin)
                self.coins += 1
                self.total_coins += 1
                self.score += 5
        
    def check_collision(self):
        """Vérifie les collisions"""
        player_rect = {
            'left': self.player_x - 20,
            'right': self.player_x + 20,
            'top': self.player_y - 30,
            'bottom': self.player_y + 30
        }
        
        for obs in self.obstacles:
            obs_rect = {
                'left': obs['x'] - 15,
                'right': obs['x'] + 15,
                'top': obs['y'] - 25,
                'bottom': obs['y'] + 25
            }
            
            if (player_rect['left'] < obs_rect['right'] and
                player_rect['right'] > obs_rect['left'] and
                player_rect['top'] < obs_rect['bottom'] and
                player_rect['bottom'] > obs_rect['top']):
                return True
        
        return False
        
    def game_loop(self):
        """Boucle principale du jeu"""
        if not self.game_running:
            return
        
        # Mettre à jour
        self.road_offset = (self.road_offset + self.speed) % 60
        self.update_player()
        self.update_obstacles()
        self.update_coins()
        self.check_coin_collection()
        
        # Vérifier collision
        if self.check_collision():
            self.game_over()
            return
        
        # Redessiner
        self.draw_game()
        
        # Continuer la boucle
        self.root.after(30, self.game_loop())
        
    def game_over(self):
        """Fin du jeu"""
        self.game_running = False
        
        # Afficher Game Over
        self.canvas.create_rectangle(
            self.width // 2 - 250, self.height // 2 - 150,
            self.width // 2 + 250, self.height // 2 + 150,
            fill='black', outline='red', width=3
        )
        
        self.canvas.create_text(
            self.width // 2, self.height // 2 - 80,
            text="GAME OVER!",
            font=('Arial', 36, 'bold'),
            fill='red'
        )
        
        self.canvas.create_text(
            self.width // 2, self.height // 2 - 30,
            text=f"Score Final: {self.score}",
            font=('Arial', 24),
            fill='white'
        )
        
        self.canvas.create_text(
            self.width // 2, self.height // 2 + 10,
            text=f"💰 Pièces collectées: {self.coins}",
            font=('Arial', 22),
            fill='gold'
        )
        
        self.canvas.create_text(
            self.width // 2, self.height // 2 + 50,
            text=f"💰 Total de pièces: {self.total_coins}",
            font=('Arial', 18),
            fill='lightblue'
        )
        
        self.canvas.create_text(
            self.width // 2, self.height // 2 + 100,
            text="Cliquez pour retourner au menu",
            font=('Arial', 16),
            fill='yellow'
        )
        
        self.canvas.bind('<Button-1>', lambda e: self.show_main_menu())

def main():
    root = tk.Tk()
    game = MarioKart(root)
    root.mainloop()

if __name__ == "__main__":
    main()