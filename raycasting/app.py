# from settings import *
# from mobs import Mobs
# from player import Player
# from drawing import *
# from buttons import *
# from map import world_map
# pygame.init()
#
#
#
#
#
#
#
# class App:
#     def __init__(self, ):
#         self.pause = False
#         self.sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
#         self.drawing = Drawing
#         self.Player = Player()
#         self.clock = pygame.time.Clock()
#         self.mobs = []
#         mob = Mobs((3000, 4000), 1)
#         self.mobs += mob
#         self.Continue = False
#     def pause(self, buttons):
#         self.sc.blit(self.sc.copy(), (0, 0))
#         self.sc.blit(sc_pause, (0, 0))
#         for button in buttons:
#             button.draw_button()
#         pygame.display.flip()
#     def music_player(self, music_list):
#
#     def game(self, ):
#         self.drawing.background(self.Player.angle)
#         self.drawing.world(self.Player.pos, self.Player.angle, self.mobs, world_map)
#         self.drawing.fps(self.clock)
#         self.drawing.mini_map(self.Player)
#         self.drawing.compass(Player.angle)
#         pygame.display.flip()
#         self.clock.tick(FPS)