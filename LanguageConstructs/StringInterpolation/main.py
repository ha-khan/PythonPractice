

class Orchestrator():
    def __init__(self) -> None:
        self.state = 'OFF'
        self.cpu = '1.5'
        self.memory = 1024
    
    def __repr__(self) -> str:
        return f'state: {self.state}, cpu: {self.cpu}, memory: {self.memory}'
    
    def __str__(self) -> str:
        return 'state: %s, cpu: %s, memory: %s' % (self.state, self.cpu, self.memory)


def main():
    o = Orchestrator()

    print('__repr__({})'.format(repr(o)))
    print('__str__({})'.format(str(o)))

if __name__ == '__main__':
    main()
