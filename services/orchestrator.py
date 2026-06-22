from packages.core import Engine


class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self) -> None:
        self.engine.start()

    def stop(self) -> None:
        self.engine.stop()

    def execute(self, tasks: list) -> None:
        self.engine.orchestrate(tasks)
