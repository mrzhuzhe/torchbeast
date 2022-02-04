from torchbeast.monobeast import test

class Flag:
    def __init__(self):
        self.env =  "PongNoFrameskip-v4"
        self.savedir = "../torch-beast-results/logs/torchbeast/"
        self.xpid =  "torchbeast-20220204-090124"
        self.use_lstm = False
        self.mode = "test_render"

#test(flags)

flags = Flag()
test(flags)