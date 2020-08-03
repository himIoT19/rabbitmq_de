import pika
import pika.exceptions
import random
import string


def publisher(message):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='127.0.0.1',
                port=5672,
                credentials=pika.PlainCredentials(username='username', password='password')
            )
        )
        channel = connection.channel()
        channel.queue_declare(queue='mm_queue', passive=False, durable=False,
                              exclusive=False, auto_delete=False, arguments=None)
        channel.basic_publish(exchange='', routing_key='mm_queue',
                              body=message, properties=None, mandatory=False)
        print(f'[x] Sent => {message}')
    except pika.exceptions.AMQPConnectionError as e:
        print(f'Error => {e}')


def main():
    # Initializing size of strings
    len_msg = 120
    count = 0

    while True:
        res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=len_msg))
        publisher(message=res)
        count += 1
        print(f'Count => {count}')


if __name__ == '__main__':
    main()
