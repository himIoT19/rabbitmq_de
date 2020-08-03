import pika
import pika.exceptions


def callback(ch, method, properties, method_signature):
    print(f'[x] Received => {method_signature}')


def consumer():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='127.0.0.1',
                port=5672,
                credentials=pika.PlainCredentials(username='username', password='password')
            )
        )
        channel = connection.channel()
        channel.queue_purge(queue='mm_queue')
        channel.queue_declare(queue='mm_queue')
        channel.basic_consume(queue='mm_queue', on_message_callback=callback, auto_ack=True)
        print(f'[*] Receiving Messages...')
        channel.start_consuming()
    except pika.exceptions.ConnectionClosed as e:
        print(f'Error => {e}')


if __name__ == '__main__':
    consumer()
