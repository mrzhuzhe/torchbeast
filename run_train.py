from torchbeast.monobeast import train

class conf:
    def __init__(self):
        self.env =  "PongNoFrameskip-v4"
        #self.env =  "BoxingNoFrameskip-v0"

        self.savedir = "./logs/test"
        self.xpid =  "torchbeast-train_test"
        self.use_lstm = False
        self.mode = "train"

        self.disable_checkpoint = None

        self.num_actors = 45
        #self.num_actors = 4
        #self.batch_size = 8
        self.batch_size = 4

        #self.num_buffers = max(2 * self.num_actors, self.batch_size)
        self.num_buffers = 60
        #self.num_learner_threads = 2
        self.num_learner_threads = 4

        self.unroll_length = 80
        self.disable_cuda = None

        #self.entropy_cost = 0.0006
        self.entropy_cost = 0.01
        self.baseline_cost = 0.5
        self.discounting = 0.99
        self.reward_clipping = "abs_one"

        #self.learning_rate = 0.00048
        self.learning_rate = 0.0004
        self.alpha = 0.99
        self.momentum = 0
        self.epsilon = 0.01
        self.grad_norm_clipping = 40.0
        #self.total_steps = 1e7
        self.total_steps = 3e7
    """
     --num_actors 45 \
     --total_steps 30000000 \
     --learning_rate 0.0004 \
     --epsilon 0.01 \
     --entropy_cost 0.01 \
     --batch_size 4 \
     --unroll_length 80 \
     --num_buffers 60 \
     --num_threads 4 \
    """
   


#test(flags)
if __name__ == "__main__":
    flags = conf()
    train(flags)