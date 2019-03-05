from diploma import create_app


app = create_app()
app.task_queue.enqueue('diploma.subscriber.subscribe', 'iot.eclipse.org')
