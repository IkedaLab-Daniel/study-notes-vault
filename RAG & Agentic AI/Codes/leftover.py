# leftovers.py
from crewai import Agent, Task
from crewai.project import CrewBase
from crewai.project.annotations import agent, task

@CrewBase
class LeftoversCrew:
    def __init__(self, llm):
        self.llm = llm

    @agent
    def leftover_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["leftover_manager"],
            llm=self.llm,
            verbose=True
        )

    @task
    def leftover_task(self) -> Task:
        return Task(
            config=self.tasks_config["leftover_task"],
            agent=self.leftover_manager()
        )
