from copy import copy
import random

import pygame
from Organism import Organism


class Animal(Organism):

    def __init__(self, world, strength, initiative, specie, skin):
        super(Animal, self).__init__(
            world, strength, initiative, specie, skin)
        self.moveRange = 1
        self.isAttacking = False

    def action(self):
        if(self.stunned):
            self.stunned = False
            return

        direction = self.get_direction()

        for i in range(self.moveRange):
            if self.dead:
                return

            self.lastPosition = copy(self.position)
            self.move(direction)
            defender = self.world.get_collider_with(self)
            if defender != 0:
                if defender.specie == self.specie:
                    self.breed(defender)
                    return
                self.isAttacking = True
                self.world.write_event(
                    self.name() + " attacks " + defender.name() + ".", (255, 120, 0))
                self.collide(defender)
                self.isAttacking = False

    def breed(self, partner):
        self.move_back()
        if random.randint(0, 1) == 1:
            return

        for x in range(3):
            for y in range(3):
                birthPos = {"x": max(min(self.position["x"] + x - 1, self.world.terrainWidth - 1), 0),
                            "y": max(min(self.position["y"] + y - 1, self.world.terrainHeight - 1), 0)}
                if self.world.get_cell(birthPos["x"], birthPos["y"]).organism == 0:
                    self.world.write_event(
                        self.name() + " has a baby with " + partner.name() + ".", (249, 93, 204))
                    self.world.add_organism(self.give_birth(), birthPos)
                    return

    def give_birth(self):
        raise NotImplementedError("Implement give_birth method")

    def take_hit(self, attacker):
        self.world.write_event(
            self.name() + " took a hit from " + attacker.name() + " and died.", (255, 0, 0))
        self.dead = True

    def move(self, direction):
        moveDescription = self.name()
        if direction == "NOWHERE":
            moveDescription += " doesn't move."
            return
        elif direction == "LEFT":
            if self.position["x"] > 0:
                self.position["x"] -= 1
                moveDescription += " moves left."
            else:
                moveDescription += " tries to move left but hits a wall."
        elif direction == "RIGHT":
            if self.position["x"] + 1 < self.world.terrainWidth:
                self.position["x"] += 1
                moveDescription += " moves right."
            else:
                moveDescription += " tries to move right but hits a wall."
        elif direction == "UP":
            if self.position["y"] > 0:
                self.position["y"] -= 1
                moveDescription += " moves up."
            else:
                moveDescription += " tries to move up but hits a wall."
        else:
            if self.position["y"] + 1 < self.world.terrainHeight:
                self.position["y"] += 1
                moveDescription += " moves down."
            else:
                moveDescription += " tries to move down but hits a wall."
        self.world.write_event(moveDescription)

    def get_direction(self):
        rnd = random.randint(1, 4)
        if rnd == 1:
            return "LEFT"
        elif rnd == 2:
            return "UP"
        elif rnd == 3:
            return "RIGHT"
        else:
            return "DOWN"


class Antelope(Animal):

    def __init__(self, world):
        super(Antelope, self).__init__(world, 4, 4, "Antelope", (238, 182, 95))
        self.moveRange = 2

    def give_birth(self):
        return Antelope(self.world)

    def take_hit(self, attacker):
        if random.randint(0, 1) == 1 and self.isAttacking == False:
            self.escape()
        else:
            self.world.write_event(
                self.name() + " took a hit from " + attacker.name() + " and died.", (255, 0, 0))
            self.dead = True

    def escape(self):
        escapePositions = []
        for x in range(3):
            for y in range(3):
                escapePos = {"x": max(min(self.position["x"] + x - 1, self.world.terrainWidth - 1), 0),
                             "y": max(min(self.position["y"] + y - 1, self.world.terrainHeight - 1), 0)}
                organism = self.world.get_cell(
                    escapePos["x"], escapePos["y"]).organism
                if organism == 0:
                    escapePositions.append(escapePos)

        if len(escapePositions) == 0:
            self.world.write_event(
                self.name() + " couldn't escape.", (50, 50, 50))
        else:
            self.world.write_event(
                self.name() + " escapes  unharmed.", (255, 0, 0))
            self.position = escapePositions[random.randint(
                0, len(escapePositions) - 1)]


class Fox(Animal):

    def __init__(self, world):
        super(Fox, self).__init__(world, 3, 7, "Fox", (247, 135, 51))

    def give_birth(self):
        return Fox(self.world)

    def get_direction(self):
        emptyDirections = []
        left = self.world.get_cell(
            self.position["x"] - 1, self.position["y"])

        right = self.world.get_cell(
            self.position["x"] + 1, self.position["y"])

        up = self.world.get_cell(
            self.position["x"], self.position["y"] - 1)

        down = self.world.get_cell(
            self.position["x"], self.position["y"] + 1)

        if self.is_safe(left):
            emptyDirections.append("LEFT")
        if self.is_safe(right):
            emptyDirections.append("RIGHT")
        if self.is_safe(up):
            emptyDirections.append("UP")
        if self.is_safe(down):
            emptyDirections.append("DOWN")

        if len(emptyDirections) == 0:
            return "NOWHERE"
        else:
            return emptyDirections[random.randint(0, len(emptyDirections) - 1)]

    def is_safe(self, direction):
        return direction != "OUT_OF_BOUND" and (direction.organism == 0
                                                or direction.organism.is_stronger(self) == False
                                                or direction.organism.specie == self.specie)


class Human(Animal):
    def __init__(self, world, abilityTurns=0, abilityActive=False, abilityOnCooldown=False):
        super(Human, self).__init__(world, 5, 4, "Human", (255, 195, 170))
        self.abilityTurns = abilityTurns
        self.abilityActive = abilityActive
        self.abilityOnCooldown = abilityOnCooldown

    def give_birth(self):
        return Human(self.world)

    def action(self):
        if(self.stunned):
            self.stunned = False
            return

        direction = self.get_direction()

        self.moveRange = 1
        self.ability()
        for i in range(self.moveRange):
            if self.dead:
                return

            self.lastPosition = copy(self.position)
            self.move(direction)
            defender = self.world.get_collider_with(self)
            if defender != 0:
                if defender.specie == self.specie:
                    self.breed(defender)
                    return
                self.isAttacking = True
                self.world.write_event(
                    self.name() + " attacks " + defender.name() + ".", (255, 120, 0))
                self.collide(defender)
                self.isAttacking = False

    def get_direction(self):
        displayBQH = False
        while True:
            hints = []
            self.set_hints(hints, displayBQH)
            self.draw_hints(hints)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    displayBQH = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return "LEFT"
                    elif event.key == pygame.K_RIGHT:
                        return "RIGHT"
                    elif event.key == pygame.K_UP:
                        return "UP"
                    elif event.key == pygame.K_DOWN:
                        return "DOWN"
                    elif event.key == pygame.K_e:
                        self.abilityActive = True

    def set_hints(self, hints, displayBQH):
        hints.append("You're a Human (Pink rectangle), arrows- movement, ")
        if self.abilityActive:
            turnsLeft = 5 - self.abilityTurns
            hints.append("ability is active for the next " +
                         str(turnsLeft) + " turns.")
        elif self.abilityOnCooldown:
            hints.append("ability is on cool down for the next " +
                         str(self.abilityTurns) + " turns.")
        else:
            hints.append("e- activate a special ability.")

        if displayBQH:
            hints.append("Please move your character before quiting")

    def draw_hints(self, hints):
        y = self.world.terrain[-1].rect.y + \
            self.world.terrain[-1].rect.height + 10
        row = 0
        FONT = pygame.font.SysFont("Noto Sans", 12)
        for hint in hints:
            entry = FONT.render(hint, True, (0, 0, 0))
            entry.fill((109, 166, 209))
            self.world.window.blit(entry, (10, y + row))
            entry = FONT.render(hint, True, (0, 0, 0))
            self.world.window.blit(entry, (10, y + row))
            row += 15
        pygame.display.update()

    def ability(self):
        if self.abilityActive:
            self.abilityTurns += 1
            if self.abilityTurns <= 3:
                self.moveRange = 2
            elif random.randint(0, 1) == 1:
                self.world.write_event("Human got lucky!", (0, 255, 0))
                self.moveRange = 2

            if self.abilityTurns >= 5:
                self.abilityActive = False
                self.abilityOnCooldown = True

        elif self.abilityOnCooldown:
            self.abilityTurns -= 1
            if self.abilityTurns <= 0:
                self.abilityOnCooldown = False


class Sheep(Animal):

    def __init__(self, world):
        super(Sheep, self).__init__(world, 4, 4, "Sheep", (231, 232, 168))

    def give_birth(self):
        return Sheep(self.world)


class CyberSheep(Sheep):

    def __init__(self, world):
        super(CyberSheep, self).__init__(world)
        self.cyber = True

    def give_birth(self):
        return CyberSheep(self.world)


class Turtle(Animal):

    def __init__(self, world):
        super(Turtle, self).__init__(world, 2, 1, "Turtle", (28, 138, 7))

    def give_birth(self):
        return Turtle(self.world)


class Wolf(Animal):

    def __init__(self, world):
        super(Wolf, self).__init__(world, 9, 5, "Wolf", (144, 144, 144))

    def give_birth(self):
        return Wolf(self.world)
