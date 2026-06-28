import logging
from typing import List, Dict
from .types import AgentRuntime, TaskScheduler, WorkerPod, EventBus, PersistentStore, AnalyticsDB
from .exceptions import CoreException, EngineException

class Engine:
    def __init__(self, agent_runtime: AgentRuntime, task_scheduler: TaskScheduler, worker_pod: WorkerPod, event_bus: EventBus, persistent_store: PersistentStore, analytics_db: AnalyticsDB):
        self.agent_runtime = agent_runtime
        self.task_scheduler = task_scheduler
        self.worker_pod = worker_pod
        self.event_bus = event_bus
        self.persistent_store = persistent_store
        self.analytics_db = analytics_db
        self.logger = logging.getLogger(__name__)

    def start(self) -> None:
        try:
            self.logger.info('Starting engine')
            self.task_scheduler.start()
            self.worker_pod.start()
            self.event_bus.start()
            self.persistent_store.start()
            self.analytics_db.start()
        except Exception as e:
            self.logger.error(f'Error starting engine: {e}')
            raise EngineException('Failed to start engine')

    def stop(self) -> None:
        try:
            self.logger.info('Stopping engine')
            self.task_scheduler.stop()
            self.worker_pod.stop()
            self.event_bus.stop()
            self.persistent_store.stop()
            self.analytics_db.stop()
        except Exception as e:
            self.logger.error(f'Error stopping engine: {e}')
            raise EngineException('Failed to stop engine')

    def execute(self, task: Dict) -> None:
        try:
            self.logger.info('Executing task')
            self.task_scheduler.schedule(task)
            self.worker_pod.allocate(task)
            self.event_bus.publish(task)
            self.persistent_store.store(task)
            self.analytics_db.query(task)
        except Exception as e:
            self.logger.error(f'Error executing task: {e}')
            raise EngineException('Failed to execute task')

    def orchestrate(self, tasks: List[Dict]) -> None:
        try:
            self.logger.info('Orchestrating tasks')
            for task in tasks:
                self.execute(task)
        except Exception as e:
            self.logger.error(f'Error orchestrating tasks: {e}')
            raise EngineException('Failed to orchestrate tasks')

    def is_running(self) -> bool:
        return all([component.is_running() for component in [self.task_scheduler, self.worker_pod, self.event_bus, self.persistent_store, self.analytics_db]])

class CoreException(Exception):
    pass

class EngineException(CoreException):
    pass

try:
    engine = Engine(
        AgentRuntime(),
        TaskScheduler(),
        WorkerPod(),
        EventBus(),
        PersistentStore(),
        AnalyticsDB()
    )
    engine.start()
    print(engine.is_running())
    engine.orchestrate([{'task_id': 1, 'task_name': 'task_1'}, {'task_id': 2, 'task_name': 'task_2'}])
except EngineException as e:
    logging.error(f'Engine exception: {e}')
except CoreException as e:
    logging.error(f'Core exception: {e}')
