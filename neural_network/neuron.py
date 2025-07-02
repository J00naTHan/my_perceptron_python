class Neuron:
    def __init__(self, entry_list, weight_list):
        self.entry_list = entry_list
        self.weight_list = weight_list

    def calc_error(self, info):
        pass

    def delta_rule(self, learning_rate, err_index):
        for n in range(len(self.weight_list)):
            self.weight_list[n] = self.weight_list[n] + learning_rate * self.entry_list[n] * err_index

    def step_function(self):
        return 1 if self.weighted_sum() >= 1 else 0

    def training(self):
        pass

    def weighted_sum(self):
        controller = 0
        for n in range(len(self.entry_list)):
            controller += self.entry_list[n] * self.weight_list[n]
        return controller
