from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

k = KubernetesPodOperator(
    name="kubernetes-without-template",
    image="debian",
    cmds=["bash", "-cx"],
    arguments=["echo", "10"],
    labels={"foo": "bar"},
    task_id="dry_run_demo",
    # It is set to be able to receive logs, since after the pod has worked and is deleted, the logs are also deleted
    # Save logs in S3
    get_logs=True,
)

k.dry_run()