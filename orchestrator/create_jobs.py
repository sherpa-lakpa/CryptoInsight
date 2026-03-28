import json
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import CronSchedule, Task, NotebookTask, TaskDependency

w = WorkspaceClient()

def create_job(entity):

    tasks = [
        Task(
            task_key="bronze",
            notebook_task=NotebookTask(
                notebook_path=f"/Workspace/Repos/sherpalakpa18@gmail.com/CryptoInsight/pipelines/{entity['name']}/bronze"
            )
        ),
        Task(
            task_key="silver",
            depends_on=[TaskDependency(task_key="bronze")],
            notebook_task=NotebookTask(
                notebook_path=f"/Workspace/Repos/sherpalakpa18@gmail.com/CryptoInsight/pipelines/{entity['name']}/silver"
            )
        )
    ]

    for level in entity.get("gold_tables", {}):
        tasks.append(
            Task(
                task_key=f"gold_{level}",
                depends_on=[TaskDependency(task_key="silver")],
                notebook_task=NotebookTask(
                    notebook_path=f"/Workspace/Repos/sherpalakpa18@gmail.com/CryptoInsight/pipelines/{entity['name']}/gold_{level}"
                )
            )
        )
    
    w.jobs.create(
        name=f"{entity['name']}_pipeline",
        tasks=tasks,
        schedule=CronSchedule(
            quartz_cron_expression="0 0 * * * ?",
            timezone_id="UTC"
        )
    )

with open("configs/entities.json") as f:
    config = json.load(f)

for entity in config["entities"]:
    create_job(entity)