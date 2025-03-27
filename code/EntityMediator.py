from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:
    score = 0

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                EntityMediator.score += 1  # score por inimigo desviado
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
            player = ent2
            enemy = ent1
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
            player = ent1
            enemy = ent2

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom):

                if isinstance(player, Player):
                    player.take_damage()

                ent1.health -= ent2.damage
                ent2.health -= ent1.damage

    @staticmethod
    def __give_score():
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        entities_to_remove = [ent for ent in entity_list if ent.health <= 0 and not isinstance(ent, Player)]

        for ent in entities_to_remove:
            entity_list.remove(ent)
