# def movement(self):
    #     sin_a = math.sin(self.angle)
    #     cos_a = math.cos(self.angle)
    #     keys = pygame.key.get_pressed()
    #     delt_x = delt_y = 0
    #     if keys[pygame.K_w]:
    #         delt_x += player_speed * cos_a
    #         delt_y += player_speed * sin_a
    #     if keys[pygame.K_s]:
    #         delt_x += -player_speed * cos_a
    #         delt_y += -player_speed * sin_a
    #     if keys[pygame.K_a]:
    #         delt_x += player_speed * sin_a
    #         delt_y += -player_speed * cos_a
    #     if keys[pygame.K_d]:
    #         delt_x += -player_speed * sin_a
    #         delt_y += player_speed * cos_a
    #     if keys[pygame.K_LEFT]:
    #         self.angle -= rotation_speed
    #     if keys[pygame.K_RIGHT]:
    #         self.angle += rotation_speed
    #     self.x += delt_x
    #     self.y += delt_y
    #     self.rect.centerx = self.x
    #     self.rect.centery = self.y
    #     i = self.x // TILE
    #     self.collide(delt_y, delt_x, i + 1, j + 1)
    #     self.collide(delt_y, delt_x, i - 1, j - 1)
    #     self.collide(delt_y, delt_x, i + 1, j)
    #     self.collide(delt_y, delt_x, i - 1, j)
    #     self.collide(delt_y, delt_x, i, j + 1)
    #     self.collide(delt_y, delt_x, i, j - 1)
    #     self.collide(delt_y, delt_x, i + 1, j - 1)
    #     self.collide(delt_y, delt_x, i - 1, j + 1)
    #
    # def collide(self, delt_y, delt_x, i, j):
    #     print(i, j)
    #     if pygame.sprite.collide_rect(self, function_map[i][j]):
    #         if delt_x > 0:
    #             self.rect.right = function_map[i][j].rect.left
    #         if delt_x < 0:
    #             self.rect.left = function_map[i][j].rect.right
    #         if delt_y > 0:
    #             self.rect.bottom = function_map[i][j].rect.top
    #         if delt_y < 0:
    #             self.rect.top = function_map[i][j].rect.bottom


# print(i, j)


# dy = - delt_y
# dx = - delt_x
# self.y += delt_y
# self.rect.centery = self.y
# if delt_y <= 0:
#     if ((i, j - TILE) in world_map and pygame.sprite.collide_rect(self, function_map[j // TILE - 1][i // TILE])) \
#             or ((i - TILE, j - TILE) in world_map and pygame.sprite.collide_rect(self, function_map[j // TILE - 1][i // TILE - 1])) \
#             or ((i + TILE, j - TILE) in world_map and pygame.sprite.collide_rect(self, function_map[j // TILE - 1][i // TILE + 1])):
#         self.y = j + player_width + 1
#
# self.x += delt_x
# self.rect.centerx = self.x
# if delt_x < 0:
#     if ((i - TILE, j) in world_map and pygame.sprite.collide_rect(self, function_map[j // TILE][i // TILE - 1])) \
#             or ((i - TILE, j - TILE) in world_map and pygame.sprite.collide_rect(self,function_map[j // TILE - 1][i // TILE - 1])) \
#             or ((i + TILE, j - TILE) in world_map and pygame.sprite.collide_rect(self,function_map[j // TILE - 1][i // TILE + 1])):
#         self.x = i + player_width + 1




# if keys[pygame.K_LEFT]:
        #     self.angle -= rotation_speed
        # if keys[pygame.K_RIGHT]:
        #     self.angle += rotation_speed

        # if delt_y <= 0:
        #     if (i, j - TILE) in world_map:
        #         if j + player_width > self.y + delt_y:
        #             delt_y = j + player_width - self.y
        # if delt_x < 0:
        #     if (i - TILE, j) in world_map:
        #         if i + player_width > self.x + delt_x:
        #             delt_x = i + player_width - self.x
        # if delt_y > 0:
        #     if (i, j + TILE) in world_map:
        #         if j + TILE - player_width < self.y + delt_y:
        #             delt_y = self.y - j - TILE + player_width
        # if delt_x > 0:
        #     if (i + TILE, j) in world_map:
        #         if i + TILE - player_width < self.x + delt_x:
        #             delt_x = self.x - i - TILE + player_width
        # if ((self.x + delt_x) // TILE * TILE, (self.y + delt_y) // TILE * TILE) in world_map:
        #     delt_x = delt_y = 0

# for x in function_map:
#     print(x)


