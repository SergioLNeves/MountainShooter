#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class BossEnemy(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]
        self.direction = -1

    def move(self):

        # Movimento vertical: sobe e desce na tela
        self.rect.centery += self.speed * self.direction
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical: sobe e desce na tela
        self.rect.centery += self.speed * self.direction

        # Verifica se bateu na borda superior
        if self.rect.top <= 0:
            self.direction = 1  # Quando bater, muda a direção
            self.speed *= 2  # Dobra a velocidade ao descer

        # Verifica se bateu na borda inferior
        elif self.rect.bottom >= WIN_HEIGHT:
            self.direction = -1  # Muda direção para subir
            self.speed = ENTITY_SPEED[self.name]  # Reseta a velocidade normal ao subir

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
