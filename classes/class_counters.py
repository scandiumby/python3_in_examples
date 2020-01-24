class CallsCounter:
    number_calls = 0

    def __call__(self):
        self.number_calls += 1
        return self

    def __str__(self):
        return f'This class was called {self.number_calls} times'

    def __repr__(self):
        self.__str__()


class CreationCounter:
    number_instances = 0

    def __init__(self):
        self.__class__.number_instances += 1

    def __str__(self):
        return self.get_message_with_counter()

    @classmethod
    def get_message_with_counter(cls):
        return f'For this class was created instance {cls.number_instances} times'


def calls_counters_demo():
    calls_counter_instance = CallsCounter()
    print(calls_counter_instance)
    calls_counter_instance()
    calls_counter_instance()
    print(calls_counter_instance)

    print(f'{CallsCounter.number_calls=}')
    print(CallsCounter()()()()())


def creation_counter_demo():
    instance_1 = CreationCounter()
    print(CreationCounter.get_message_with_counter())
    print(instance_1)

    instance_2 = CreationCounter()
    CreationCounter()
    print(CreationCounter.get_message_with_counter())
    print(instance_2)

    CreationCounter()
    print(CreationCounter.get_message_with_counter())
    print(instance_1)


if __name__ == '__main__':
    calls_counters_demo()
    creation_counter_demo()
