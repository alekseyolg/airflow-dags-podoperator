from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from airflow import DAG

with DAG(
    dag_id="kubernetes-without-template",
    schedule=None,
    start_date=datetime.now(),
    catchup=False,
    tags=["example"],
) as dag:
  example_kubernetes_operator = KubernetesPodOperator(
    name="kubernetes_operator", 
    image="debian",
    cmds=["bash", "-cx"],
    arguments=["echo 'Hello, world!' && sleep 600"],
    labels={"foo": "bar"},
    task_id="dry_run_demo",
    # It is set to be able to receive logs, since after the pod has worked and is deleted, the logs are also deleted
    # Save logs in S3
    get_logs=True,
)

example_kubernetes_operator.dry_run()
