

class MonsterGame:
    def __init__(self, xp=0, click_value=1, upgrade_cost=10, current_stage=1):
        self.xp = xp
        self.click_value = click_value
        self.upgrade_cost = upgrade_cost
        self.current_stage = current_stage

    def click(self):
        self.xp += self.click_value

    def can_upgrade(self):
        return self.xp >= self.upgrade_cost

    def calculate_stage(self):
        if self.xp >= 250:
            return 4
        elif self.xp >= 50:
            return 3
        elif self.xp >= 10:
            return 2
        else:
            return 1

    def upgrade(self):
        if self.can_upgrade():
            eligible_stage = self.calculate_stage()

            self.xp -= self.upgrade_cost
            self.click_value *= 2
            self.upgrade_cost *= 5

            if eligible_stage > self.current_stage:
                self.current_stage = eligible_stage

    def get_stage(self):
        return self.current_stage
