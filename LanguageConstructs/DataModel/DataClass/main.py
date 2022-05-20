from dataclasses import dataclass


@dataclass
class Orchestrator:
    name: str
    cpu_utilization: int

    def __post_init__(self) -> None:
        """
            https://docs.python.org/3/library/dataclasses.html#post-init-processing 
        """
        import logging
        import time
        l = logging.getLogger().setLevel(logging.INFO)
        logging.info('establishing connection')
        time.sleep(0.5)
        logging.info('connection established!')

    def compute(self) -> None:
        import time
        print('Computing!!!')
        time.sleep(2)
        print('Done')


def main():
    o = Orchestrator('vm', 1)
    print(o)
    o.compute()
    o.name = 'hypervisor'
    print(o)
    print(dir(o))

if __name__ == '__main__':
    main()
